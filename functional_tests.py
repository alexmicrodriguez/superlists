from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		slef.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#User goes to homepage
		self.browser.get('http://localhost:8000')
		
		#User notices page title and header mention to do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		#User is invited to enter item right away
if __name__=='__main__':
	unittest.main(warnings='ignore')