import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class SeleniumTest(TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--user-data-dir=/tmp/chrome-user-data")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    def tearDown(self):
        self.driver.close()

    def test_app(self):
        self.driver.get(f"http://{os.environ.get('APP_HOST', 'web')}")
        header = self.driver.find_element(By.TAG_NAME, 'h3').text
        self.assertEqual(header, "Hello World!")
        visits_before_refresh = int(self.driver.find_element(By.ID,'visits').text)
        self.driver.refresh()
        visits_after_refresh = int(self.driver.find_element(By.ID,'visits').text)
        self.assertEqual(visits_after_refresh, visits_before_refresh + 1)
