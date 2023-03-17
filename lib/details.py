from playwright.sync_api import Page
import time


class Details:
    fir_name = "//input[@id='AccountFrm_firstname']"
    Last_name = "//input[@id='AccountFrm_lastname']"
    Email_loc = "//input[@id='AccountFrm_email']"
    tel_loc = "//input[@id='AccountFrm_telephone']"
    Adress = "#AccountFrm_address_1"
    city = "//input[@id='AccountFrm_city']"
    state = "//select[@name='zone_id']"
    Zipcode = "//input[@id='AccountFrm_postcode']"
    country = "//select[@id='AccountFrm_country_id']"
    Login_name = "//input[@id='AccountFrm_loginname']"
    password = "//input[@id='AccountFrm_password']"
    conf_pass = "//input[@id='AccountFrm_confirm']"
    check_box = "(//input[@id='AccountFrm_newsletter0'])"
    policy_check = "//input[@id='AccountFrm_agree']"
    con_button = "//button[normalize-space()='Continue']"


class FillDetails:
    fir_name = "Bavanam"
    Last_name = "Bhargavi"
    Email = "bavanambhargavi1@gmail.com"
    tel = "7673959974"
    Add = "plot no: 25 , srilakshmi ladies pg"
    city = "OMR"
    code = "600096"
    name = "Bhargavi4444"
    password = "Abhirama@1994"
    c_password = "Abhirama@1994"

    def __init__(self, page: Page):
        self.page = page

    def fillthedetails(self):
        self.page.locator(Details.fir_name).fill(FillDetails.fir_name)
        self.page.locator(Details.Last_name).fill(FillDetails.Last_name)
        self.page.locator(Details.Email_loc).fill(FillDetails.Email)
        self.page.locator(Details.tel_loc).fill(FillDetails.tel)

    def details(self):
        self.page.locator(Details.Adress).fill(FillDetails.Add)
        self.page.locator(Details.city).fill(FillDetails.city)
        # self.page.locator(Details.state).click()
        # self.page.keyboard.down("End")
        self.page.locator(Details.country).click()
        self.page.locator(Details.country).select_option("India")
        self.page.locator(Details.state).click()
        self.page.locator(Details.state).select_option(label="Andhra Pradesh")
        time.sleep(4)
        self.page.locator(Details.Zipcode).fill(FillDetails.code)
        # self.page.locator(Details.country).select_option("India")
        self.page.locator(Details.Login_name).fill(FillDetails.name)
        self.page.locator(Details.password).fill(FillDetails.password)
        self.page.locator(Details.conf_pass).fill(FillDetails.c_password)
        self.page.locator(Details.check_box).click()
        self.page.locator(Details.policy_check).click()
        time.sleep(2)
        self.page.locator(Details.con_button).click()
        time.sleep(2)
