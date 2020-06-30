import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False

driver = webdriver.Firefox(options=options)

def login(regno, dob):
	# to try to login the results page with the given
	# registration number and date of birth
	return

driver.get("http://cloudportal.sathyabama.ac.in/sist_results_may_2020/login.php")

regno = "39111041"
dob = "20/01/2002"

regfield = driver.find_element_by_name("regno")
dobfield = driver.find_element_by_name("dob")
loginbtn = driver.find_element_by_id("btnLogin")

regfield.send_keys(regno)
dobfield.send_keys(dob)
loginbtn.click()

# driver.close()
# exit()