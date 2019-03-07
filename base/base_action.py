import time
import unittest
class base_action():

    def __init__(self, driver):

        self.driver = driver


    def click(self, loc):

        self.find_element(loc).click()


    def send_key(self, loc, param):

        self.find_element(loc).send_keys(param)


    def find_element(self, loc):

        return self.driver.find_element(loc[0], loc[1])

    def assert_method(self, param, message):
        try:
            text = self.driver.find_element_by_css_selector(param).text
            if message in text:
                return True

            else:
                nowtime = time.strftime("%Y_%m_%d %H_%M_%S")
                self.driver.get_screenshot_as_file('./image/%s.jpg' % nowtime)
                return False

        except Exception:
            nowtime = time.strftime("%Y_%m_%d %H_%M_%S")
            self.driver.get_screenshot_as_file('./image/%s.jpg' % nowtime)
            return False
