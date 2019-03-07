import os,sys
sys.path.append(os.getcwd())
from time import sleep
from base.base_driver import Base_driver
from page.page_signup import test_page
import pytest
from base.base_read import read_file
class Test():


    def setup(self):

        self.driver = Base_driver()
        self.method = test_page(self.driver)

    @pytest.mark.parametrize('proper', read_file())
    def test(self, proper):
        username = proper['username']
        password = proper['password']
        assertmetheod = proper["assert"]
        message = proper["message"]
        self.method.click_signin()
        self.method.send_user(username)
        self.method.send_password(password)
        self.method.click_sign()
        sleep(5)
        assert self.method.assert_method(assertmetheod, message)

    def teardown(self):

        self.driver.quit()