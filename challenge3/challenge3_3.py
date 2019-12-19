import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

class Challenge3(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()
    def test_challenge3whileloop(self):
        self.driver.get("https://www.copart.com")
        #link = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")
        link = self.driver.find_elements_by_xpath("//*[@id=\"tabTrending\"]/div[1]//a")
        i = 0
        while(i<len(link)):
            print(link[i].text + ":" + link[i].get_property("href"))
            # i = i+1
            i += 1

if __name__ == '__main__':
    unittest.main()