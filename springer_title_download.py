from selenium import webdriver
browser = webdriver.Firefox(executable_path='C:\Program Files\geckodriver.exe') # if system path edit doesn't work, use the 'executable_path' arg as here
browser.get('http://www.springernature.com/gp/librarians/manage-your-account/marc-records/title-list-downloader')

bsp = browser.find_element_by_class_name('gwt-CheckBox')
print(bsp)
