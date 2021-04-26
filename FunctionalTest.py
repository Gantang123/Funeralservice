from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):

	
	def setUp(self):
		self.browser = webdriver.Firefox()
		

	def test_browser_title(self):
		self.browser.get('http://localhost:8888')
		self.assertIn('Essential Order Form', self.browser.title)

		Header = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Essential Order Form', Header)

		#Paragraph
		nametag = self.browser.find_element_by_tag_name('p').text
		self.assertIn('Select your essential here', nametag)

		#input
		input1 = self.browser.find_element_by_id('name')  
		self.assertEqual(input1.get_attribute('placeholder'),'Enter your name')
		input2 = self.browser.find_element_by_id('name').send_keys("Mark Gantang")
		time.sleep(1)

		#Paragraph
		nametag1 = self.browser.find_element_by_id('par').text
		self.assertIn('Select your essential here', nametag1)

		#radio1
		Select = self.browser.find_element_by_id('Gloves1').click()
		time.sleep(1)
		Select = self.browser.find_element_by_id('Alcohol2').click()
		time.sleep(1)
		Select = self.browser.find_element_by_id('Facemask3').click()
		time.sleep(1)
		Select = self.browser.find_element_by_id('Faceshield4').click()
		time.sleep(1)
		Select = self.browser.find_element_by_id('SetofPPE5').click()
		time.sleep(1)
		Select = self.browser.find_element_by_id('Handsanitizer6').click()
		time.sleep(1)

		input2 = self.browser.find_element_by_id('Quantity')  
		self.assertEqual(input2.get_attribute('placeholder'),'Quantity')
		input2 = self.browser.find_element_by_id('Quantity').send_keys("3")
		time.sleep(1)

		input3 = self.browser.find_element_by_id('Address')  
		self.assertEqual(input3.get_attribute('placeholder'),'Enter your Address')
		input3 = self.browser.find_element_by_id('Address').send_keys("Dasmarinas City")
		time.sleep(1)
		#Paragraph1
		nametag2 = self.browser.find_element_by_id('pay').text
		self.assertIn('Mode of Payment', nametag2)

		form = self.browser.find_element_by_tag_name('form')
		#radio2
		Payment = self.browser.find_element_by_id('CashonDelivery1').click()
		time.sleep(1)
		Payment = self.browser.find_element_by_id('OnlinePayment2').click()
		time.sleep(1)
		Payment = self.browser.find_element_by_id('Meetup3').click()
		time.sleep(1)
		#submit
		submitbutton = self.browser.find_element_by_name('done').click()
		time.sleep(2)

		self.browser.quit()	
		self.browser = webdriver.Firefox()
		self.browser.get('http://localhost:8888')

		input1 = self.browser.find_element_by_id('name')  
		self.assertEqual(input1.get_attribute('placeholder'),'Enter your name')
		input2 = self.browser.find_element_by_id('name').send_keys("Vincent N. Gantang")
		time.sleep(1)

		Select = self.browser.find_element_by_id('Gloves1').click()
		time.sleep(1)
		Select = self.browser.find_element_by_id('Alcohol2').click()
		time.sleep(1)
		Select = self.browser.find_element_by_id('Facemask3').click()
		time.sleep(1)
		Select = self.browser.find_element_by_id('Faceshield4').click()
		time.sleep(1)
		Select = self.browser.find_element_by_id('SetofPPE5').click()
		time.sleep(1)
		Select = self.browser.find_element_by_id('Handsanitizer6').click()
		time.sleep(1)

		input2 = self.browser.find_element_by_id('Quantity')  
		self.assertEqual(input2.get_attribute('placeholder'),'Quantity')
		input2 = self.browser.find_element_by_id('Quantity').send_keys("3")
		time.sleep(1)

		input3 = self.browser.find_element_by_id('Address')  
		self.assertEqual(input3.get_attribute('placeholder'),'Enter your Address')
		input3 = self.browser.find_element_by_id('Address').send_keys("Dasmarinas City")
		time.sleep(1)
		Payment = self.browser.find_element_by_id('CashonDelivery1').click()
		time.sleep(1)
		Payment = self.browser.find_element_by_id('OnlinePayment2').click()
		time.sleep(1)
		Payment = self.browser.find_element_by_id('Meetup3').click()
		time.sleep(1)
		#submit
		submitbutton = self.browser.find_element_by_name('done').click()
		time.sleep(2)
		self.browser.quit()



if __name__ == '__main__':
	unittest.main()

'''from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')'''
