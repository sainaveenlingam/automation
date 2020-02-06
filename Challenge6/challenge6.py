import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.headerSearch import headerSearch
from common.filters import filters
from common.screenshot import screenshot
from common.searchresults import searchResults

class Challenge6(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.get("https://www.copart.com")
    def tearDown(self):
        # code to close webdriver
        self.driver.close()
        print('in tear down method')

    def test_challenge6(self):
        hs = headerSearch(self.driver)
        hs.serachFor("nissan")
        f = filters()
        f.clickFilter("Model")
        s = screenshot()
        s.takescreenshot("Skyline")
        sr = searchResults()
        sr.changeDropDown("100")


if __name__ == '__main__':
    unittest.main()

