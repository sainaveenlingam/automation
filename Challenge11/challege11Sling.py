import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# define a site to crawl
# whatever I'm crawling, I don't leave that site
# sling.com -> youtube.com protect against this
# list of the URL's to go to
# <a href


class challenge11(unittest.TestCase):
    newurls = []
    visitedUrls = []
    baseURL = "https://wwww.sling.com"
    baseURL = []


    def setup(self):
        print ('in setup method')
        self.driver = webdriver.chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()
        print('in tear down method')

    def test_challenge11crawler(self):
        UrlPair = [self.baseURL, self.baseURL]
        self.newurls.append(UrlPair)
        while (len(self.newurls) > 0):
            currentURL = self.newurls.pop()
            self.driver.get(currentURL[0])
            time.sleep(1)
            self.visitedUrls.append(currentURL)
            print ("have" + str(len(self.newurls)) + "left to visit")
            print(currentURL[0])
            print (self.driver.current_url)
            self.currentPageURLs = self.driver.find_element(By.Tag_Name, "a")
            for c in self.currentPageURLs:
                c_url = c.get_attribute("href")
                if c_url != None:
                   if self.baseURL in c_url:
                       if c_url not in self.visitedUrls:
                           if c_url not in self.newurls:
                               UrlPair = [c_url, self.driver.current_url]
                               self.newurls.append(UrlPair)
            self.currentPageURLs.clear()
            self.currentPageURLs = []
            page = self.driver.find_element(By.Tag_Name, "body")
            if "404" in page.text:
                self.baseURL.append(self.driver.current_url)
                file = open("BrokenPages.txt", "a")
                file.write(currentURL[0] + " has a 404. ling was found on page " + currentURL[1] + "\n")
                file.close()
                # file.writelines(currentURL + " has a 404\n")
            images = self.driver.find_element(By.Tag_Name, "img")
            for i in images:
                    if i.get_attributes("alt") == None:
                        file = open("ImagesWOalt.txt", "a")
                        file.write(i.get_attributes("src") + "found on: " + currentURL[0] + "does not have alt tag\n")
                        file.close()

    if __name__ == '__main__':
        unittest.main()