from playwright.sync_api import Page
import time


class Checkthecart:

    quantity = "#cart_quantity114"
    cart = "#cart_checkout1"
    # cou = "//select[@id='estimate_country']"
    # state = "//select[@id='estimate_country_zones']"
    # code = "//input[@id='estimate_postcode']"
    # shippment = "//select[@id='shippings']"
    # order = "//button[@id='checkout_btn']"


class Cart:

    def __init__(self, page: Page):
        self.page = page

    def thecart(self):
        self.page.locator(Checkthecart.quantity).fill("1")
        self.page.locator(Checkthecart.cart).click()
    

    # def detials(self):
    #     self.page.locator(Checkthecart.cou).click()
    #     self.page.locator(Checkthecart.cou).select_option(label="India")
    #     self.page.locator(Checkthecart.state).click()
    #     self.page.locator(Checkthecart.state).select_option("Andhra Pradesh")
    #     self.page.locator(Checkthecart.code).fill("600096")
    #     self.page.locator(Checkthecart.shippment).click()
    #     self.page.locator(Checkthecart.order).click()
    #     self.page.screenshot(path="\\Screenshots\\order.png", full_page=True)
    #     time.sleep(2)
        
