import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, quote
import json
import time
import os
import hashlib
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

BASE_URL = "https://www.bu.edu/tech/support/research/"
SCRAPED_DIR = "scraped_pages"

if not os.path.exists(SCRAPED_DIR):
    os.makedirs(SCRAPED_DIR)

visited = set()
pages = []


def is_valid(url):
    parsed = urlparse(url)
    return parsed.netloc.endswith("bu.edu") and \
           parsed.scheme in ("http", "https") and \
           url.startswith(BASE_URL)


def extract_links(soup, base_url):
    links = set()
    for a in soup.find_all("a", href=True):
        href = urljoin(base_url, a["href"])
        if is_valid(href):
            links.add(href.split("#")[0])  # Remove fragment
    return links


def extract_visible_text(soup):
    # Remove script, style, nav, footer, header, aside, and noscript
    for tag in soup(["script", "style", "nav", "footer", "header", "aside", "noscript"]):
        tag.decompose()
    # Get visible text
    text = soup.get_text(separator="\n", strip=True)
    # Remove excessive blank lines
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return "\n".join(lines)


def url_to_filename(url):
    # Use SHA256 hash for uniqueness and filesystem safety
    url_hash = hashlib.sha256(url.encode("utf-8")).hexdigest()
    return f"{url_hash}.json"

def crawl(url):
    to_visit = [url]
    while to_visit:
        curr_url = to_visit.pop(0)
        fname = url_to_filename(curr_url)
        fpath = os.path.join(SCRAPED_DIR, fname)
        if os.path.exists(fpath):
            logging.info(f"[SKIP] Already scraped: {curr_url}")
            visited.add(curr_url)
            continue
        try:
            logging.info(f"[VISIT] {curr_url}")
            resp = requests.get(curr_url, timeout=10)
            if resp.status_code != 200:
                logging.info(f"[WARN] Non-200 status code for {curr_url}: {resp.status_code}")
                continue
            soup = BeautifulSoup(resp.text, "html.parser")
            text = extract_visible_text(soup)
            page_data = {"url": curr_url, "text": text}
            with open(fpath, "w", encoding="utf-8") as f:
                json.dump(page_data, f, ensure_ascii=False, indent=2)
            logging.info(f"[SAVE] {curr_url} -> {fpath}")
            visited.add(curr_url)
            pages.append(page_data)
            # Find new links
            links = extract_links(soup, curr_url)
            new_links = 0
            for link in links:
                if link not in visited and link not in to_visit:
                    to_visit.append(link)
                    new_links += 1
            logging.info(f"[LINKS] Found {len(links)} links, {new_links} new links queued. {len(to_visit)} pages in queue.")
            time.sleep(0.5)  # Be polite
        except Exception as e:
            logging.info(f"[ERROR] Failed to fetch {curr_url}: {e}")
    logging.info(f"[DONE] Crawl finished. {len(visited)} total pages visited.")


def main():
    global pages, visited
    # Resume support: scan scraped_pages for existing files
    if not os.path.exists(SCRAPED_DIR):
        os.makedirs(SCRAPED_DIR)
    scraped_files = os.listdir(SCRAPED_DIR)
    visited = set()
    pages.clear()
    for fname in scraped_files:
        if fname.endswith(".json"):
            fpath = os.path.join(SCRAPED_DIR, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    page = json.load(f)
                    visited.add(page["url"])
                    pages.append(page)
            except Exception as e:
                print(f"Warning: Failed to load {fpath}: {e}")
    print(f"Loaded {len(pages)} previously scraped pages from {SCRAPED_DIR}.")
    crawl(BASE_URL)
    print(f"Total unique pages scraped: {len(pages)}.")


if __name__ == "__main__":
    main()
