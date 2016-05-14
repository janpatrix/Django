from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])


	def test_create_list_and_retrieve_it_later(self):

		#Open Homepage
		self.browser.get('http://localhost:8000')

		#Check page title for Django
		self.assertIn ('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)		

		#Create a to do item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)

		#Type "buy something" into the text-box
		inputbox.send_keys('Buy something')

		#Hitting enter, should update the page and page lists
		#"buy something as to-do item"
		inputbox.send_keys(Keys.ENTER)
		self.check_for_row_in_list_table('1: Buy something')

		#Blackbox shows and invites to add another item.
		#Enter "buy another item"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('buy another item')
		inputbox.send_keys(Keys.ENTER)

		#Page should update again and both items show on list
		self.check_for_row_in_list_table('1: Buy something')
		self.check_for_row_in_list_table('2: buy another item')

		#Check if unique URL was created to store list
		self.fail('Finish the test')
		#Visit unique URL and check if items are still there

if __name__ == '__main__':
	unittest.main()