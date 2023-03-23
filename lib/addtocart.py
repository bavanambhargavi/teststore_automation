from playwright.sync_api import Page
import time


class Addcart:
    book = "nav >> a:is(:text(\"BOOKS\"))"
    click_icon = "//a[normalize-space()='Paperback']"
    img_book = "//div[@class='thumbnails grid row list-inline']//div[3]//div[2]//a[1]//img[1]"
    review = "//a[normalize-space()='Reviews (0)']"
    rating = "//a[@title='4']"
    name = "//input[@id='name']"
    text = "//textarea[@id='text']"
    quantity = "//input[@id='product_quantity']"
    addcart = "//a[normalize-space()='Add to Cart']"


class Gotocart:
    def __init__(self, page: Page):
        self.page = page

    def clickbooks(self):
        self.page.wait_for_timeout(4000)
        self.page.locator(Addcart.book).first.click()
        self.page.locator(Addcart.click_icon).click()
        self.page.locator(Addcart.img_book).click()
        time.sleep(4)

    def review(self):

        self.page.locator(Addcart.review).click()
        self.page.locator(Addcart.rating).click()
        self.page.locator(Addcart.name).fill("Bhargavi")
        self.page.locator(Addcart.text).fill("It is a Goodbook")
        self.page.screenshot(path="..\\Screenshots\\review.png")

    def addcart(self):
        self.page.wait_for_timeout(3000)
        self.page.locator(Addcart.quantity).fill("1")
        self.page.keyboard.press("Backspace")
        time.sleep(4)
        # self.page.locator(Addcart.addcart).click()
        self.page.locator(Addcart.addcart).dispatch_event('click')
        



