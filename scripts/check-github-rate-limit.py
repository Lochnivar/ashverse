#!/usr/bin/env python3
"""
GitHub API Rate Limit Checker
Checks your current GitHub API rate limit status
"""

import json
import sys
import urllib.request
import urllib.error
from datetime import datetime, timedelta

def check_rate_limit(token=None):
    """
    Check GitHub API rate limit status.
    
    Args:
        token: Optional GitHub personal access token for authenticated requests
              (provides higher rate limits)
    """
    url = 'https://api.github.com/rate_limit'
    
    # Build request
    req = urllib.request.Request(url)
    if token:
        req.add_header('Authorization', f'token {token}')
    req.add_header('Accept', 'application/vnd.github.v3+json')
    req.add_header('User-Agent', 'GitHub-RateLimit-Checker')
    
    try:
        # Make request
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
        
        # Core API rate limits
        core = data.get('resources', {}).get('core', {})
        search = data.get('resources', {}).get('search', {})
        graphql = data.get('resources', {}).get('graphql', {})
        
        # Set UTF-8 encoding for Windows compatibility
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        
        print("=" * 60)
        print("GitHub API Rate Limit Status")
        print("=" * 60)
        print()
        
        # Core API
        limit = core.get('limit', 0)
        remaining = core.get('remaining', 0)
        reset_time = datetime.fromtimestamp(core.get('reset', 0))
        used = limit - remaining
        percentage = (used / limit * 100) if limit > 0 else 0
        
        print("[CORE API]")
        print(f"   Limit:     {limit:,} requests/hour")
        print(f"   Used:      {used:,} requests")
        print(f"   Remaining: {remaining:,} requests")
        print(f"   Usage:     {percentage:.1f}%")
        print(f"   Resets at: {reset_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Warning levels
        if percentage >= 90:
            print("   [WARNING] Rate limit nearly exhausted!")
        elif percentage >= 75:
            print("   [CAUTION] Rate limit usage is high")
        elif percentage >= 50:
            print("   [INFO] Moderate usage")
        else:
            print("   [OK] Low usage")
        
        print()
        
        # Search API
        if search:
            search_limit = search.get('limit', 0)
            search_remaining = search.get('remaining', 0)
            search_reset = datetime.fromtimestamp(search.get('reset', 0))
            search_used = search_limit - search_remaining
            search_pct = (search_used / search_limit * 100) if search_limit > 0 else 0
            
            print("[SEARCH API]")
            print(f"   Limit:     {search_limit:,} requests/hour")
            print(f"   Used:      {search_used:,} requests")
            print(f"   Remaining: {search_remaining:,} requests")
            print(f"   Usage:     {search_pct:.1f}%")
            print(f"   Resets at: {search_reset.strftime('%Y-%m-%d %H:%M:%S')}")
            print()
        
        # GraphQL API
        if graphql:
            graphql_limit = graphql.get('limit', 0)
            graphql_remaining = graphql.get('remaining', 0)
            graphql_reset = datetime.fromtimestamp(graphql.get('reset', 0))
            graphql_used = graphql_limit - graphql_remaining
            graphql_pct = (graphql_used / graphql_limit * 100) if graphql_limit > 0 else 0
            
            print("[GRAPHQL API]")
            print(f"   Limit:     {graphql_limit:,} requests/hour")
            print(f"   Used:      {graphql_used:,} requests")
            print(f"   Remaining: {graphql_remaining:,} requests")
            print(f"   Usage:     {graphql_pct:.1f}%")
            print(f"   Resets at: {graphql_reset.strftime('%Y-%m-%d %H:%M:%S')}")
            print()
        
        # Time until reset
        time_until_reset = reset_time - datetime.now()
        if time_until_reset.total_seconds() > 0:
            hours, remainder = divmod(int(time_until_reset.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f"[RESET] Rate limit resets in: {hours}h {minutes}m {seconds}s")
        else:
            print("[RESET] Rate limit has reset!")
        
        print()
        print("=" * 60)
        
        # Return status code for scripting
        if percentage >= 90:
            return 2  # Critical
        elif percentage >= 75:
            return 1  # Warning
        else:
            return 0  # OK
            
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error {e.code}: {e.reason}", file=sys.stderr)
        if e.code == 401:
            print("   Hint: Invalid token or token expired", file=sys.stderr)
        return 3
    except urllib.error.URLError as e:
        print(f"❌ Network Error: {e.reason}", file=sys.stderr)
        return 3
    except Exception as e:
        print(f"❌ Error checking rate limit: {e}", file=sys.stderr)
        return 3

def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Check GitHub API rate limit status',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Check rate limit (unauthenticated - 60 requests/hour)
  python check-github-rate-limit.py
  
  # Check rate limit (authenticated - 5,000 requests/hour)
  python check-github-rate-limit.py --token YOUR_GITHUB_TOKEN
  
  # Use token from environment variable
  export GITHUB_TOKEN=your_token
  python check-github-rate-limit.py --token-env
        """
    )
    
    parser.add_argument(
        '--token',
        help='GitHub personal access token (for authenticated requests)'
    )
    parser.add_argument(
        '--token-env',
        action='store_true',
        help='Use GITHUB_TOKEN environment variable'
    )
    
    args = parser.parse_args()
    
    token = None
    if args.token_env:
        import os
        token = os.environ.get('GITHUB_TOKEN')
        if not token:
            print("❌ Error: GITHUB_TOKEN environment variable not set", file=sys.stderr)
            sys.exit(1)
    elif args.token:
        token = args.token
    
    exit_code = check_rate_limit(token)
    sys.exit(exit_code)

if __name__ == '__main__':
    main()

