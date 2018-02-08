# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import credentials


class SearchTestSuite(unittest.TestCase):
    """
    1.      Open any browser
    2.      Navigate to stackoverflow website - https://stackoverflow.com/
    3.      Press on “log in”
    4.      Insert “email”
    5.      Insert “password”
    6.      Press on “log in”
    7.      Insert string “python” to search box
    8.      Access first search result.
    """

    def setUp(self):
        logging.basicConfig(level=logging.DEBUG, filename="1.log")
        logging.debug('This message should go to the log file')
        logging.info('So should this')
        logging.warning('And this, too')
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_search(self):
        """
        test
        """

        # Home page:
        driver = self.driver
        driver.get("https://stackoverflow.com/")
        driver.find_element_by_xpath(".//a[contains(text(), 'Log In')]").click()

        # Login page:
        # We should be sure that we are on correct page:
        WebDriverWait(driver, 10).until(EC.title_contains("Log In"))

        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(credentials['login'])

        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(credentials['password'])

        driver.find_element_by_id("submit-button").click()

        # Search result page:
        # We should be sure that we are on correct page:
        WebDriverWait(driver, 10).until(EC.title_contains("Stack Overflow - Where Developers Learn"))

        search_word = "python"
        self.print_input(xpath='//*[@id="search"]/input', text=search_word)

        driver.find_element_by_css_selector("button.btn-topbar-primary.js-search-submit").click()

        search_result = driver.find_element_by_class_name("question-summary").text

        self.assertIn(search_word, search_result, "Can't find the correct result during the search!")

    def print_input(self, xpath, text):
        self.driver.find_element_by_xpath(xpath).click()
        self.driver.find_element_by_xpath(xpath).clear()
        self.driver.find_element_by_xpath(xpath).send_keys(text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    suite = unittest.TestLoader().loadTestsFromTestCase(SearchTestSuite)
    unittest.TextTestRunner(verbosity=4).run(suite)
