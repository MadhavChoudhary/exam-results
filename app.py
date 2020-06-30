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

# main page for resutls
driver.get("http://cloudportal.sathyabama.ac.in/sist_results_may_2020/login.php")

#given regno and dob
regno = "39111041"
dob = "20/01/2002"

# important fields
regfield = driver.find_element_by_name("regno")
dobfield = driver.find_element_by_name("dob")
loginbtn = driver.find_element_by_id("btnLogin")

regfield.send_keys(regno)
dobfield.send_keys(dob)
loginbtn.click()

## now you are inside resutls

metatable = driver.find_element_by_id("tblInfo")
meta = metatable.find_elements_by_tag_name("td")

datatable = driver.find_element_by_id("tblDisplay")
col = datatable.find_element_by_tag_name("thead").find_elements_by_tag_name("tr")[0].find_elements_by_tag_name("th")
rows = datatable.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")

for row in rows:
	row.find_elements_by_tag_name("th")

# driver.close()
# exit()