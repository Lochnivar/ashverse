# GitHub API Rate Limit Monitoring Guide

This guide helps you monitor GitHub API rate limit usage to avoid hitting limits during development.

## Quick Check Script

Use the included `check-github-rate-limit.py` script to check your current rate limit status:

```bash
# Unauthenticated (60 requests/hour)
python scripts/check-github-rate-limit.py

# Authenticated (5,000 requests/hour) - requires GitHub token
python scripts/check-github-rate-limit.py --token YOUR_GITHUB_TOKEN

# Or use environment variable (Windows PowerShell)
$env:GITHUB_TOKEN="your_token"
python scripts/check-github-rate-limit.py --token-env

# Or use environment variable (Linux/Mac)
export GITHUB_TOKEN=your_token
python scripts/check-github-rate-limit.py --token-env
```

**Note:** This script uses Python's standard library (`urllib`) - no additional packages required!

## VS Code / Cursor Extensions

### 1. GitHub Rate Limit Monitor (Recommended)
- **Extension ID:** `justin-grote.github-ratelimit`
- **What it does:** Shows GitHub API rate limit status in the status bar
- **Install:** Search "GitHub Rate Limit Monitor" in VS Code/Cursor extensions
- **Note:** Requires GitHub sign-in in VS Code/Cursor

### 2. GitLens
- **Extension ID:** `eamodio.gitlens`
- **What it does:** Comprehensive Git tooling (may make API calls)
- **Settings:** Can configure to reduce API call frequency
- **Note:** Check settings to limit background API calls

## Online Tools

### GitHub Rate Limit Checker
- **URL:** https://tools.simonwillison.net/github-ratelimit
- **What it does:** Quick web-based rate limit checker
- **Use case:** Quick checks without installing anything

## Command Line Methods

### Using curl (Quick Check)
```bash
# Unauthenticated
curl -i https://api.github.com/rate_limit

# Authenticated (replace YOUR_TOKEN)
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/rate_limit
```

### Using GitHub CLI
```bash
# If you have GitHub CLI installed
gh api rate_limit
```

## Understanding Rate Limits

### Unauthenticated Requests
- **Limit:** 60 requests per hour per IP address
- **Reset:** Every hour
- **Use case:** Basic API queries

### Authenticated Requests
- **Limit:** 5,000 requests per hour per token
- **Reset:** Every hour
- **Use case:** Development tools, extensions, scripts

### Search API
- **Limit:** 30 requests per minute (authenticated)
- **Limit:** 10 requests per minute (unauthenticated)
- **Use case:** Code search, repository search

### GraphQL API
- **Limit:** 5,000 points per hour
- **Use case:** Complex queries, GitHub's GraphQL API

## What Causes Rate Limit Usage

### ✅ Does NOT Use Rate Limits
- Local file edits
- Local git operations (`git add`, `git commit`, `git status`)
- Running local scripts
- Code refactoring
- Building/compiling code

### ⚠️ DOES Use Rate Limits
- Cursor/VS Code checking repository status
- GitHub extensions syncing data
- Git operations that query GitHub (`git fetch`, `git pull`)
- API calls from scripts/tools
- GitHub Copilot (if enabled)

## Reducing Rate Limit Usage

### 1. Disable Auto-Sync in Cursor/VS Code
- Settings → Git → Auto Fetch: Disable or increase interval
- Settings → GitHub → Auto Sync: Disable or reduce frequency

### 2. Review Extensions
- Check which extensions use GitHub API
- Disable or configure extensions that make frequent API calls
- Common culprits: GitLens, GitHub Pull Requests, GitHub Copilot

### 3. Use Authenticated Requests
- Create a GitHub Personal Access Token
- Use it in scripts and tools for higher limits (5,000 vs 60)

### 4. Batch Operations
- Group multiple operations together
- Use GraphQL for complex queries (more efficient)

## Monitoring Best Practices

1. **Check regularly:** Run the rate limit checker script periodically
2. **Set up alerts:** Use the script's exit codes for automation
3. **Track usage:** Note when you hit warnings (75%+) to identify patterns
4. **Review extensions:** Periodically audit which extensions are making API calls

## Exit Codes (for Scripting)

The `check-github-rate-limit.py` script returns:
- `0` - OK (usage < 75%)
- `1` - Warning (usage 75-89%)
- `2` - Critical (usage ≥ 90%)
- `3` - Error (could not check)

## Getting a GitHub Token

1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scopes: `repo` (for private repos) or `public_repo` (for public repos)
4. Copy token and store securely
5. Use in scripts: `--token YOUR_TOKEN` or set `GITHUB_TOKEN` environment variable

## Troubleshooting

### "Rate limit exceeded" error
- Check current usage with the script
- Wait for reset (usually on the hour)
- Review what's making API calls
- Consider using authenticated requests for higher limits

### High usage but not sure why
- Check Cursor/VS Code settings for auto-sync
- Review enabled extensions
- Check if any background processes are running
- Use GitHub's audit log to see API usage

---

**Remember:** Your code refactoring and local work don't affect rate limits. Only external API calls do.

