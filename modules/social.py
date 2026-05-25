import asyncio
from config import SOCIAL_PLATFORMS
from core.engine import AsyncOSINTEngine

class SocialScanner:
    def __init__(self):
        self.engine = AsyncOSINTEngine()

    async def scan_username(self, username):
        print(f'[*] Scanning for username: {username}...')
        results = {}
        
        async def check_platform(session, platform, url_template):
            url = url_template.format(username)
            status = await self.engine.fetch_status(session, url)
            if status == 200:
                results[platform] = {'status': 'FOUND', 'url': url}
            elif status == 404:
                results[platform] = {'status': 'NOT_FOUND'}
            else:
                results[platform] = {'status': f'ERROR ({status})'}

        import aiohttp
        async with aiohttp.ClientSession() as session:
            tasks = [check_platform(session, plat, url) for plat, url in SOCIAL_PLATFORMS.items()]
            await asyncio.gather(*tasks)
        
        return results
