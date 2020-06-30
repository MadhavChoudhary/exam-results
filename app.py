import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)

def login(regno, dob):
	# to try to login the results page with the given
	# registration number and date of birth

def iterate():
	# iterate through possible regno and dob
	# collect data first to get some information
	# about boundaries
