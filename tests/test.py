import os
import sys
from selenium import webdriver
from unittest import TestCase
from xvfbwrapper import Xvfb


class SeleniumTest(TestCase):

    def setUp(self):
        if sys.platform.startswith('linux') and not os.environ.get('DISPLAY'):
            self.xvfb = Xvfb(width=1280, height=720)
            self.xvfb.start()
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_app(self):
        self.driver.get("http://{}".format(os.environ.get('APP_HOST', 'web')))
        header = self.driver.find_element_by_tag_name('h3').text
        self.assertEquals(header, "Hello World!")
        visits_before_refresh = int(self.driver.find_element_by_id('visits').text)
        self.driver.refresh()
        visits_after_refresh = int(self.driver.find_element_by_id('visits').text)
        self.assertEquals(visits_after_refresh, visits_before_refresh + 1)
