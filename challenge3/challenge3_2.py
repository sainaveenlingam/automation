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
        print('in tear down method')

    def test_challenge3forloopsecondsection(self):
        self.driver.get("https://www.copart.com")
        # link = self.driver.find_elements_by_xpath("//*[@id=\"tabTrending\"]/div[3]//a")
        link = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]/../div[3]//a")

        for item in link:
        #print(element.text)
            print(item.text + ":" + item.get_property("href"))


if __name__ == '__main__':
    unittest.main()



