from lib.search import Gotopage
from lib.login import LoginPage

from lib.addtocart import Gotocart
from playwright.sync_api import Page


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
