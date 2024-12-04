from playwright.sync_api import Playwright, sync_playwright, expect
from pages.GetVersion import VersionFetcher
from pages.ConsultPage import ConsultPage


def run(playwright: Playwright) -> None:
  browser = playwright.chromium.launch(headless=False)
  context = browser.new_context()
  page = context.new_page()
  
  consult_page = ConsultPage(page)
  version_fetcher = VersionFetcher(page)

  search = consult_page.handle_consultation()
  if search['error']:
    return search
  
  
  version = version_fetcher.retrieve_version()
  if version["error"]:
    return version


  # ---------------------
  context.close()
  browser.close()


with sync_playwright() as playwright:
  run(playwright)