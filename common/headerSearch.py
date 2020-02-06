from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class headerSearch:
    def __init__(self, driver):
        self.driver = driver
        print("initializing headerSearch")

    def searchFor(self, query):
        print("search for " + query)

        element = self.driver.find_element(By.ID, "input-search")
        element.send_keys(query)
        searchBtn = self.driver.find_element(By.XPATH, "//button[@data-uname='homepageHeadersearchsubmit']")
        searchBtn.click()
        datawait = WebDriverWait(self.driver, 10)
        element = datawait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//td[5]")))
        tabledata = self.driver.find_element (By.XPATH, "//*[@id=\"serverSideDataTable\"]//td[5]")
        visible = tabledata.text
        print(visible);
