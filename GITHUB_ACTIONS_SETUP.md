# GitHub Actions CI/CD Setup

This repository now uses GitHub's auto-generated Jekyll workflow to build and deploy the site instead of the default GitHub Pages build process.

## Workflow Overview

GitHub automatically created a Jekyll workflow that:

1. **Triggers**: Runs on pushes to the main branch and can be manually triggered
2. **Build Process**: 
   - Sets up the appropriate Ruby environment
   - Installs Jekyll and dependencies
   - Builds the site with Jekyll
   - Uploads the built site as a Pages artifact
3. **Deploy Process**: 
   - Automatically deploys to GitHub Pages
   - Updates the live site at your GitHub Pages URL

## Repository Configuration

The workflow was enabled when you:

1. Went to your repository's **Settings** → **Pages**
2. Selected **GitHub Actions** as the source
3. GitHub automatically detected your Jekyll site and created the appropriate workflow

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

## Benefits of GitHub Actions Workflow

- **Automatic setup**: GitHub detected your Jekyll site and created the optimal workflow
- **Plugin support**: Can use any Jekyll plugins (not limited to GitHub Pages whitelist)
- **Better reliability**: More robust than the legacy GitHub Pages build process
- **Detailed logging**: Clear build logs and error reporting in the Actions tab
- **Dependency caching**: Faster builds through automatic dependency caching
- **Maintenance-free**: GitHub maintains and updates the workflow template
