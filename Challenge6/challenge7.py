import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from common.navigateTo import naviagateTo
class Challenge7(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()
        print('in tear down method')

    def test_challenge7(self):
        try:
            elements = self.driver.find_element(By.XPATH, '//*[@id="tabTrending"]//a')
            ng = naviageteTo(self.driver)
            for count in elements:

                if ng.goTo(count.get_attribute("href"), count.text):
                    print ("test")
                else:
                    print("test")
        except:
            print("create your own action")
if __name__ == '__main__':
    unittest.main()



