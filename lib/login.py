from playwright.sync_api import Page
from data import config
import time


class Login:

    name = config.Loginname
    passw = config.password

    Login_loc = "//a[normalize-space()='Login or register']"
    login_name = "//input[@id='loginFrm_loginname']"
    password = "//input[@id='loginFrm_password']"
    login_button = "//button[normalize-space()='Login']"


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def loginpage(self):
        self.page.locator(Login.Login_loc).click()
        self.page.locator(Login.login_name).fill(Login.name)
        self.page.locator(Login.password).fill(Login.passw)
        self.page.locator(Login.login_button).click()
        self.page.go_back()
        self.page.keyboard.type(Login.login_button, delay=10)
        time.sleep(4)
