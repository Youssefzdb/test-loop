import socket
import logging

class DNSRecon:
    @staticmethod
    def get_ip_address(domain):
        try:
            return socket.gethostbyname(domain)
        except socket.gaierror:
            return None

    @staticmethod
    def run_recon(domain):
        print(f'[*] Running DNS Reconnaissance for: {domain}...')
        ip = DNSRecon.get_ip_address(domain)
        if ip:
            return {
                'domain': domain,
                'ip_address': ip,
                'status': 'RESOLVED'
            }
        else:
            return {
                'domain': domain,
                'status': 'COULD_NOT_RESOLVE'
            }
