from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_create_list_and_retrieve_it_later(self):

		#Open Homepage
		self.browser.get('http://localhost:8000')

		#Check page title for Django
		self.assertIn ('To-Do', self.browser.title)
		self.fail('Finish the test')
		#Create a to do item

		#Type "buy something" into the text-box

		#Hitting enter, should update the page and page lists
		#"buy something as to-do item"

		#Blackbox shows and invites to add another item.
		#Enter "buy another item"

		#Page should update again and both items show on list

		#Check if unique URL was created to store list

		#Visit unique URL and check if items are still there

if __name__ == '__main__':
	unittest.main()