# GitHub Actions CI/CD Setup

This repository now uses a custom GitHub Actions workflow to build and deploy the Jekyll site instead of the default GitHub Pages build process.

## Workflow Overview

The workflow (`.github/workflows/jekyll.yml`) performs the following steps:

1. **Triggers**: Runs on pushes to `main`/`master` branches, pull requests, and manual dispatch
2. **Build Job**: 
   - Sets up Ruby 3.1 environment
   - Installs dependencies using Bundler
   - Builds the Jekyll site with production settings
   - Uploads the built site as an artifact
3. **Deploy Job**: 
   - Deploys the built site to GitHub Pages
   - Only runs for pushes to main/master branches

## Required Repository Settings

To enable this workflow, you need to configure your repository settings:

1. Go to your repository's **Settings** → **Pages**
2. Under "Source", select **GitHub Actions**
3. The workflow will automatically deploy to GitHub Pages on successful builds

## Dependencies

The `Gemfile` has been updated to include:
- Jekyll 4.3.x for compatibility
- `github-pages` gem for GitHub Pages compatibility
- All necessary Jekyll plugins for the minimal-mistakes theme

## Local Development

To test builds locally:

```bash
# Install dependencies
bundle install

# Build the site
bundle exec jekyll build

# Serve locally (for development)
bundle exec jekyll serve
```

## Troubleshooting

- **Build failures**: Check the Actions tab for detailed error logs
- **Missing dependencies**: Ensure all required gems are listed in the Gemfile
- **Theme issues**: Verify the minimal-mistakes-jekyll theme is properly configured

## Benefits of Custom Workflow

- Full control over the build environment
- Ability to use any Jekyll plugins (not limited to GitHub Pages whitelist)
- Better error reporting and debugging
- Faster builds with dependency caching
- Support for custom build steps if needed
