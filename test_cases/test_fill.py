from lib.search import Gotopage
from lib.login import LoginPage
from lib.details import FillDetails
from playwright.sync_api import Page
import time


class Testfilldetails:

    def test_account(self, page: Page):
        search = Gotopage(page)
        search.navigate()
        search.gotowebsite()
        log = LoginPage(page)
        log.loginpage()
        time.sleep(2)
        d = FillDetails(page)
        d.fillthedetails()
        time.sleep(3)
        d.details()
        time.sleep(2)
