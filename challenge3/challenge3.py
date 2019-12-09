import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


class Challenge3(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()
        print('in tear down method')

    def test_challenge3forloop(self):
        self.driver.get("https://www.copart.com")
        element = self.driver.find_element(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]")
        link = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/../div[1]//a")
        for item in link:
        #print(element.text)
            print(item.text + ":" + item.get_property("href"))

    #def test_challenge3whileloop(self):
        #self.driver.get("https://www.copart.com")
        #element = self.driver.find_element(By.ID, "input-search")

if __name__ == '__main__':
    unittest.main()



