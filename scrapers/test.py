import asyncio
import os
import sys

# Adiciona o diretório raiz ao sys.path para permitir importações absolutas de 'scrapers' e 'core'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scrapers.factories.platform_factory import PlatformFactory
from scrapers.browsers.playwright_automation import AsyncPlaywrightAutomation

async def main():
    url_ml = "https://www.amazon.com.br/Apple-iPhone-15-128-GB/dp/B0CP6CR795/ref=sr_1_5?adgrpid=133609000532&dib=eyJ2IjoiMSJ9.j_8U5FP9COx2j0LCC_xx7AjJvlK5F3AKDmmsNvaTrvqOVoU3wTWE8QgnfchAHb3A9FcZ8jXIQNExXKVFKU7_PEZr58gEB1ytryTB7xwUBPvuSLMIXghX_gjDN9QfKseYAJMmT237SD5Oz6V"

    url_az = "https://www.amazon.com.br/Masculina-Feminina-Notebook-Refor%C3%A7ada-Resistente/dp/B0FVN2PH3Y/?_encoding=UTF8&pd_rd_w=Tm37D&content-id=amzn1.sym.50d3bdbc-5ffb-4e8f-830f-890881f5c373&pf_rd_p=50d3bdbc-5ffb-4e8f-830f-890881f5c373&pf_rd_r=TC3EYGREF4AY9CEMZRDX&pd_rd_wg=j92KP&pd_rd_r=2e3c6305-d577-4451-a6cd-0d1769d87540&ref_=pd_hp_d_atf_dealz_cs&th=1"

    url_magalu = "https://www.magazineluiza.com.br/smart-tv-50-semp-4k-uhd-led-50s62-google-tv-aipq-google-assistente-3-hdmi/p/240428500/et/tves/?seller_id=magazineluiza"
    try:
        engine = AsyncPlaywrightAutomation(headless=False)

        automation = PlatformFactory(automation=engine).get_by_url(url_magalu)
        result_magalu = await automation.get_info(url_magalu)
        print(result_magalu)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        print("Automação finalizada!")

if __name__ == "__main__":
    asyncio.run(main())
