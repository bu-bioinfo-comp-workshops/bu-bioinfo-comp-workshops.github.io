# Jekyll Docker Development Environment

This setup lets you build and serve your Jekyll site locally using Docker, so you don't need to install Ruby or Jekyll directly on your system.

## 1. Dockerfile (optional, for full customization)
For most users, the official Jekyll Docker image is sufficient and you do not need a custom Dockerfile.

## 2. docker-compose.yml
Create this file in your project root:

```yaml
version: '3.8'
services:
  jekyll:
    image: jekyll/jekyll:4.2.2
    command: jekyll serve --watch --host 0.0.0.0
    ports:
      - "4000:4000"
    volumes:
      - .:/srv/jekyll
    environment:
      - JEKYLL_ENV=development
```

## 3. .dockerignore (recommended)
To avoid copying unnecessary files into the container:

```dockerignore
_site
.bundle
Gemfile.lock
```

## 4. Usage

- **Start the development server:**
  ```sh
  docker-compose up
  ```
- **Visit your site:**
  Open [http://localhost:4000](http://localhost:4000) in your browser.
- **Stop the server:**
  Press `Ctrl+C` in the terminal, or run `docker-compose down`.

## 5. Notes
- Any changes you make to your source files will be reflected live, thanks to the volume mount and `--watch`.
- If you add new gems, update your `Gemfile` and run:
  ```sh
  docker-compose run --rm jekyll bundle install
  ```

---

This setup is robust for local development and requires only Docker and Docker Compose installed on your machine.
