import asyncio
import argparse
import sys
from core.engine import AsyncOSINTEngine
from modules.social import SocialScanner
from modules.dns_recon import DNSRecover

def print_banner():
    banner = """
    ==================================================
    * ADVANCED OSINT FRAMEWORK            *
    * Automated Recon & Intelligence       *
    ==================================================
    """
    print(banner)

async def main_async(args):
    engine = AsyncOSINTEngine()
    
    if args.username:
        print(f"[*] Starting social media enumeration for username: {args.username}\n")
        scanner = SocialScanner(engine)
        results = await scanner.scan_username(args.username)
        print("\n[+] Scan Results:")
        for platform, status in results.items():
            print(f"  [-] {platform}: {status}")
            
    if args.domain:
        print(f"\n[*] Starting DNS reconnaissance for domain: {args.domain}\n")
        dns_recon = DNSRecover()
        dns_results = dns_recon.scan_domain(args.domain)
        print("\n[+] DNS Records Found:")
        for record_type, records in dns_results.items():
            print(f"  [-] {record_type}: {', '.join(records) if records else 'None'}")

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Advanced OSINT Command Line Tool")
    parser.add_argument("-u", "--username", help="Username to search across social networks", required=False)
    parser.add_argument("-d", "--domain", help="Domain name to perform DNS reconnaissance", required=False)
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
        
    args = parser.parse_args()
    
    if not args.username and not args.domain:
        print("[-] Error: Please specify either a username (-u) or a domain (-d).")
        sys.exit(1)
        
    asyncio.run(main_async(args))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Operation cancelled by user.")
        sys.exit(0)