import unittest
import json
import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Disabling warning messages when running unit test
def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", 'ResourceWarning')
            test_func(self, *args, **kwargs)
    return do_test


class Test_RJEMS(unittest.TestCase):
	driver2 = webdriver.Chrome(executable_path='./chromedriver')
	driver = webdriver.Chrome(executable_path='./chromedriver')



	def test01_setup_selenium(self):
		self.driver.implicitly_wait(30)
		self.driver.get("https://localhost:80")
		self.assertEqual("https://localhost:80/", self.driver.current_url)

	def test02_login_page(self):
		assert "Welcome to RJEMS Enterprise" in self.driver.title
		self.assertEqual(self.driver.title, "Welcome to RJEMS Enterprise")

	def test03_nav_to_okta(self):
		login = self.driver.find_element_by_xpath("//a[1]")
		login.click()
		#login.click()
		time.sleep(.5)
		assert "SJSU" in self.driver.title
		self.assertIn("SJSU", self.driver.title)

	def test04_login(self):
		username = self.driver.find_element_by_name("username")
		password = self.driver.find_element_by_name("password")

		username.clear()
		username.send_keys("jonathan.gee@sjsu.edu")
		password.clear()
		password.send_keys("Abcd1234")

		self.driver.find_element_by_id("okta-signin-submit").click()

		time.sleep(2)

		assert "RJEMS Enterprise" in self.driver.title
		self.assertEqual("RJEMS Enterprise | Profile", self.driver.title)

	def test05_update_info(self):
		phone = self.driver.find_element_by_name("input_phone")
		bio = self.driver.find_element_by_name("input_bio")
		address1 = self.driver.find_element_by_name("input_address_line1")
		address2 = self.driver.find_element_by_name("input_address_line2")
		city = self.driver.find_element_by_name("input_city")
		state = Select(self.driver.find_element_by_name("input_state"))

		phone.clear()
		phone.send_keys("911")
		bio.clear()
		bio.send_keys("Test Bio")
		address1.clear()
		address1.send_keys("1600 Pennsylvania Ave NW, Washington, DC 20500")
		address2.clear()
		address2.send_keys("1 Washington Sq, San Jose, CA 95192")
		city.clear()
		city.send_keys("San Jose")
		state.select_by_visible_text("NV")


		self.driver.find_element_by_class_name("btn").click()

		assert "Profile was updated successfully." in self.driver.find_element_by_class_name("success").text 		
		self.assertEqual("Profile was updated successfully.", self.driver.find_element_by_class_name("success").text)

	def test06_dashboard(self):
		self.driver.find_element_by_link_text("Dashboard").click()
		self.assertEqual("RJEMS Enterprise | Dashboard", self.driver.title)

		training_doc = self.driver.find_element_by_xpath("//div[3]/button[1]")
		photos = self.driver.find_element_by_xpath("//div[3]/button[2]")
		news = self.driver.find_element_by_xpath("//div[3]/button[3]")

		assert "Training Documents" in training_doc.text
		assert "Photos" in photos.text
		assert "News/Updates" in news.text
		self.assertEqual("Training Documents", training_doc.text)
		self.assertEqual("Photos", photos.text)
		self.assertEqual("News/Updates", news.text)

	def test07_search(self):		
		self.driver.find_element_by_link_text("Search").click()
		self.assertEqual("RJEMS Enterprise | Search", self.driver.title)

		table = self.driver.find_element_by_class_name("table")

		assert "First Name" in table.text


		search_name = self.driver.find_element_by_name("input_first_name")
		search_name.clear()
		search_name.send_keys("RJEMS")

		self.driver.find_element_by_class_name("btn").click()
		table = self.driver.find_element_by_class_name("table")

		assert "Jonathan" not in table.text
		assert "RJEMS" in table.text
		self.assertNotIn("Jonathan", table.text)
		self.assertIn("RJEMS", table.text)


	def test08_logout(self):
		logout = self.driver.find_element_by_link_text("Logout")
		logout.click()
		assert "Welcome to RJEMS Enterprise" in self.driver.title
		self.assertEqual(self.driver.title, "Welcome to RJEMS Enterprise")

	def test09_shutdown_selenium(self):
		self.driver.close()
		self.assertEqual(1,1)

	def test10_login_with_admin(self):
		self.driver2.implicitly_wait(30)
		self.driver2.get("https://localhost:80")

		login = self.driver2.find_element_by_xpath("//a[1]")
		login.click()
		#login.click()
		time.sleep(.5)
		assert "SJSU" in self.driver2.title
		self.assertIn("SJSU", self.driver2.title)

		username = self.driver2.find_element_by_name("username")
		password = self.driver2.find_element_by_name("password")

		username.clear()
		username.send_keys("rjems2018@gmail.com")
		password.clear()
		password.send_keys("Projects@SJSU1")

		self.driver2.find_element_by_id("okta-signin-submit").click()

		time.sleep(2)

		self.assertEqual("RJEMS Enterprise | Profile", self.driver2.title)

	def test11_admin_search(self):
		self.driver2.find_element_by_link_text("Search").click()
		self.assertEqual("RJEMS Enterprise | Search", self.driver2.title)

		search_name = self.driver2.find_element_by_name("input_first_name")
		search_name.clear()
		search_name.send_keys("Jonathan")

		self.driver2.find_element_by_class_name("btn-lg").click()
		view_payslip = self.driver2.find_element_by_xpath("//a[contains(text(), 'View Payslip')]")
		view_payslip.click()
		time.sleep(1)

		payslip = self.driver2.find_element_by_xpath("//div[@class='modal-body']/p[1]/span[1]")
		assert "Jonathan Gee" in payslip.text
		self.assertIn("Jonathan Gee", payslip.text)

		self.driver2.find_element_by_class_name("close").click()
		time.sleep(1)

	def test12_admin_upload(self):
		self.driver2.find_element_by_link_text("Upload").click()
		self.assertEqual("RJEMS Enterprise | Upload", self.driver2.title)

		upload = Select(self.driver2.find_element_by_id("input_upload_type"))
		upload.select_by_visible_text("News/Updates")
		time.sleep(1)

		text = self.driver2.find_element_by_name("input_upload_text")
		text.send_keys("Unit test update")

		self.driver2.find_element_by_class_name("btn").click()
		assert "News/Updates was uploaded successfully." in self.driver2.find_element_by_class_name("success").text 		
		self.assertEqual("News/Updates was uploaded successfully.", self.driver2.find_element_by_class_name("success").text)

	def test13_check_update(self):
		self.driver2.find_element_by_link_text("Dashboard").click()
		self.assertEqual("RJEMS Enterprise | Dashboard", self.driver2.title)
		news = self.driver2.find_element_by_xpath("//div[3]/button[3]")
		news.click()

		update = self.driver2.find_element_by_xpath("//html/body/div[3]/div[3]/table/tbody/tr[1]/td/h3")
		print(update.text)
		assert "Unit test update" in update.text
		self.assertEqual("Unit test update", update.text)

	def test14_admin_logout(self):
		logout = self.driver2.find_element_by_link_text("Logout")
		logout.click()
		assert "Welcome to RJEMS Enterprise" in self.driver2.title
		self.assertEqual(self.driver2.title, "Welcome to RJEMS Enterprise")

	def test15_final_shutdown(self):
		self.driver2.close()
		self.assertEqual(1,1)




 
if __name__ == '__main__':
    unittest.main()

