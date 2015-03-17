from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User goes to homepage
        self.browser.get('http://localhost:8000')

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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy dat good gud gud', [row.text for row in rows])
        self.assertIn('2: JaRule', [row.text for row in rows])
        # there is still a text box for user to enter more items
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')