from lib.search import Gotopage
from lib.login import LoginPage
from playwright.sync_api import Page, expect
import time


class Testlogin:

    def test_login(self, page: Page):
        search = Gotopage(page)
        search.navigate()
        search.gotowebsite()
        log = LoginPage(page)
        log.loginpage()
        time.sleep(4)
        expect(page).to_have_title("My Account")
