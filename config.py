"""
Configuration module for the Advanced OSINT Framework.
Contains target platforms, DNS record types, and global application settings.
"""

# Global HTTP Settings
TIMEOUT = 10
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Social Media Platforms Mapping
# {} will be replaced by the target username
SOCIAL_PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "Reddit": "https://www.reddit.com/user/{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "GitLab": "https://gitlab.com/{}"
}

# DNS Record Types to Scan
DNS_RECORD_TYPES = ["A", "AAAA", "MX", "TXT", "NS", "CNAME"]
