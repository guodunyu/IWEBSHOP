from selenium.webdriver.common.by import By

from base.base_action import base_action


class test_page(base_action):

    sign_up = By.LINK_TEXT, '登录'
    user = By.CSS_SELECTOR, "[type ='text']"
    password = By.CSS_SELECTOR, "[type = 'password']"
    sign = By.CSS_SELECTOR, "[type ='submit']"

    def __init__(self, driver):
        base_action.__init__(self, driver)


    def send_user(self, param):

        self.send_key(self.user, param)

    def send_password(self, param):

        self.send_key(self.password, param)

    def click_signin(self):

        self.click(self.sign_up)

    def click_sign(self):

        self.click(self.sign)