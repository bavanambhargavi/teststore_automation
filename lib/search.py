from playwright.sync_api import Page


class SearchPage:

    loc_1 = "//input[@title='Search']"
    loc_2 = "//h3[normalize-space()='Automation Test Store']"


class Gotopage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.google.com/")

    def gotowebsite(self):
        self.page.wait_for_timeout(5000)
        self.page.locator(SearchPage.loc_1).fill("Automationteststore")
        self.page.locator(SearchPage.loc_1).press("Enter")
        self.page.locator(SearchPage.loc_2).click()
