from lib.search import Gotopage
from lib.login import LoginPage
from lib.addtocart import Gotocart
from playwright.sync_api import Page
import time


class TestReview:

    def test_reviewthebook(self, page: Page):
        search = Gotopage(page)
        search.navigate()
        search.gotowebsite()
        log = LoginPage(page)
        log.loginpage()
        e = Gotocart(page)
        e.clickbooks()
        e.review()
        time.sleep(4)
