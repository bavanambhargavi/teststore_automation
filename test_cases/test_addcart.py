from lib.search import Gotopage
from lib.login import LoginPage

from lib.addtocart import Gotocart
from playwright.sync_api import Page, expect


class Testaddcart:

    def test_addcart(self, page: Page):
        search = Gotopage(page)
        search.navigate()
        search.gotowebsite()
        log = LoginPage(page)
        log.loginpage()
        e = Gotocart(page)
        e.clickbooks()
        e.addcart()
        expect(page).not_to_have_title("")
