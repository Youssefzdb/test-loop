import os

# Configuration settings for the Advanced OSINT Framework
TIMEOUT = 10
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

# Target sites for username enumeration
TARGET_PLATFORMS = {
    'GitHub': 'https://github.com/{}',
    'Twitter': 'https://x.com/{}',
    'Instagram': 'https://www.instagram.com/{}/',
    'Reddit': 'https://www.reddit.com/user/{}/',
    'Pinterest': 'https://www.pinterest.com/{}/'
}
