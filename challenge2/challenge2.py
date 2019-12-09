import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Challenge2(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()
        print('in tear down method')

    def test_challenge2(self):
        # code for our test steps
        # self.driver.get("https://www.google.com")
        # self.assertIn("Google", self.driver.title)
        # print(self.driver.title)
        self.driver.get("https://www.copart.com")
        # html = self.driver.page_source
        # print(html)
        element = self.driver.find_element(By.ID, "input-search")
        element.send_keys("exotic")
        searchBtn = self.driver.find_element(By.XPATH, "//button[@data-uname='homepageHeadersearchsubmit']")
        searchBtn.click()
        datawait = WebDriverWait(self.driver, 10)
        element = datawait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//td[5]")))
        print(element.text)
        element = self.driver.find_element(By.XPATH, "//span[contains(.,'PORSCHE')]")
        print(element.text)
        datatable = self.driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable\"]")

        # element = self.driver.find_element(By.XPATH, "//*[@name='q']")
        # element = self.driver.find_element(By.ID, 'foo')
        # print('go to google')

        # print (html)
        self.assertIn("PORSCHE", datatable.text)
        result_element = datawait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//td//span[@data-uname=\"lotsearchLotmake\"]")))
        for item in result_element:
            print("Model  " + item.text)

if __name__ == '__main__':
    unittest.main()

