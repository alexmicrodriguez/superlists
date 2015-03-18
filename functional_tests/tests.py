from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest
import time


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User goes to homepage
        self.browser.get(self.live_server_url)

        # User notices page title and header mention to do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # User is invited to enter item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # User enters "Buy dat good gud gud"
        inputbox.send_keys('Buy dat good gud gud')
        # User hits enter, page updates, and now page lists the item on table
        inputbox.send_keys(Keys.ENTER)
        # User enters another item to the list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('JaRule')
        inputbox.send_keys(Keys.ENTER)
        # Page updates, now displaying two items on list
        self.check_for_row_in_list_table('1: Buy dat good gud gud')
        self.check_for_row_in_list_table('2: JaRule')
        # there is still a text box for user to enter more items
        self.fail('Finish the test!')