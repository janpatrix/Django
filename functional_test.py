from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

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

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
				any(row.text == '1: Buy something' for row in rows)
			)

		#Blackbox shows and invites to add another item.
		#Enter "buy another item"
		self.fail('Finish the test')

		#Page should update again and both items show on list

		#Check if unique URL was created to store list

		#Visit unique URL and check if items are still there

if __name__ == '__main__':
	unittest.main()