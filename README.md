# Exam-Results
It is just a python _web automation_ code.
We will be using selenium 3.141.0
By this we can just login into the results portal and will be trying to login using multiple date of births as for each reg no:

# Getting Started
we import necessary libraries and packages required for it; such as:
```bash
from time import sleep
from selenium import webdriver
from datetime import timedelta, date
from selenium.webdriver.firefox.options import Options
```
we will be using sleep() for the possibilities if refresh rate and delay possibilities...

we will create individual methods for it to access, and the loop for it to iteratively check with each date for the perticular registeration number.

# Fetching Data
For fetching the data we use:
```bash
meta = driver.find_element_by_id("tblInfo").find_elements_by_tag_name("td")
	for item in meta:
		f.write('{}\t'.format(item.text))
	f.write('\n')

	datatable = driver.find_element_by_id("tblDisplay")
```
Then we take out the col and rows in order and we log out..:
```bash
col = datatable.find_element_by_tag_name("thead").find_elements_by_tag_name("tr")[0].find_elements_by_tag_name("th")
	for item in col:
		f.write('{}\t'.format(item.text))
	f.write('\n')

rows = datatable.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
	for row in rows:
		items = row.find_elements_by_tag_name("td")
		for item in items:
			f.write('{}\t'.format(item.text))
		f.write('\n')
    ```
Thats it ... in this way we can use web automation to get every result of every person...
