from lib.search import Gotopage
from playwright.sync_api import Page
import time


class TestSearchwebsite:

    def test_search_website(self, page: Page):
        s = Gotopage(page)
        s.navigate()
        s.gotowebsite()
        time.sleep(2)
