import os
import sys
import requests
from bs4 import BeautifulSoup

def banner():
    print("=" * 50)
    print("        Advanced OSINT Tool v1.0")
    print("=" * 50)

def check_username(username):
    print(f'\n[*] Searching for username: {username}')
    # Example placeholder for social media audit
    urls = {
        'GitHub': f'https://github.com/{username}',
        'Twitter': f'https://twitter.com/{username}'
    }
    for platform, url in urls.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f'[+] Found on {platform}: {url}')
            else:
                print(f'[-] Not found on {platform}')
        except Exception as e:
            print(f'[!] Error checking {platform}')

def main():
    banner()
    if len(sys.argv) < 2:
        print('Usage: python osint_tool.py <target_username>')
        sys.exit(1)
    
    target = sys.argv[1]
    check_username(target)

if __name__ == '__main__':
    main()