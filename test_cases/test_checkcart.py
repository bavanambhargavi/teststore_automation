from lib.search import Gotopage
from lib.login import LoginPage
from lib.addtocart import Gotocart
from lib.checkthecart import Cart
from playwright.sync_api import Page
import time


class TestCheckcart:

    def test_checkthecart(self, page: Page):
        search = Gotopage(page)
        search.navigate()
        search.gotowebsite()
        log = LoginPage(page)
        log.loginpage()
        e = Gotocart(page)
        e.clickbooks()
        e.addcart()
        check = Cart(page)
        check.thecart()
        # check.detials()
        time.sleep(5)
