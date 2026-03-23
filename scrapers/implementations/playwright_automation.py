import asyncio
from scrapers.interfaces.base.automation import AsyncAutomationInterface
from playwright.async_api import async_playwright

class AsyncPlaywrightAutomation(AsyncAutomationInterface):
    def __init__(self) -> None:
        self.browser = None
        self.context = None
        self.page = None
    
    async def start(self, url: str) -> None:
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=False)
        self.context = await self.browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        self.page = await self.context.new_page()
        await self.page.goto(url, timeout=60000, wait_until="domcontentloaded")
        await asyncio.sleep(5)

    async def get_text(self, field: str, timeout: int = 10000) -> str:
        value = await self.page.wait_for_selector(field, timeout=timeout)
        return await value.inner_text()

    async def stop(self) -> None:
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()