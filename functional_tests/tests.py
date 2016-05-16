from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(StaticLiveServerTestCase):
	
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
		self.browser.get(self.live_server_url)

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
		my_list_url = self.browser.current_url
		self.assertRegex(my_list_url, 'lists/.+')
		self.check_for_row_in_list_table('1: Buy something')

		#Blackbox shows and invites to add another item.
		#Enter "buy another item"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('buy another item')
		inputbox.send_keys(Keys.ENTER)

		#Page should update again and both items show on list
		self.check_for_row_in_list_table('1: Buy something')
		self.check_for_row_in_list_table('2: buy another item')

		#A new User is using the site - Patrick

		## We need a new browser session to make sure no information
		## is shown from lasts session
		self.browser.quit()
		self.browser = webdriver.Firefox()

		#Patrick checks the new website and tehre is no sign of my old list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy something', page_text)
		self.assertNotIn('buy another item', page_text)

		#Patrick enters a new item to the list
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)

		#Patrick gets his own unique ID
		patrick_list_url = self.browser.current_url
		self.assertRegex(patrick_list_url, 'lists/.+')
		self.assertNotEqual(patrick_list_url, my_list_url)

		#Again not trace of my list left
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy something', page_text)
		self.assertIn('Buy milk', page_text)

	def test_layout_and_styling(self):
		#User goes to the homepage
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024, 768)

		#Check if input box is nicely centered for home_page
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2, 
			512, 
			delta = 5
		)

		#Check if input box is nicely centered for list view
		inputbox.send_keys('testing\n')
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2, 
			512, 
			delta = 5
		)