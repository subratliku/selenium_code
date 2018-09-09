import time

from selenium.webdriver import Chrome,ActionChains


driver=Chrome('C:\selenium-Project-Training\Drivers\chromedriver.exe')

driver.implicitly_wait(30)
driver.get('https://www.flipkart.com')
time.sleep(5) #this 5 sec sleep to close the pop up so that we can prform move_to_element Electronics
dropmenu_element=driver.find_element_by_xpath("//span[contains(text(),'Electronics')]")
act = ActionChains(driver=driver)
act.move_to_element(dropmenu_element).perform()
driver.find_element_by_link_text('Samsung').click()
time.sleep(5)
driver.close()