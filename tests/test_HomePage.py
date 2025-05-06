from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self):

        homePage = HomePage(self.driver)
        homePage.getName().send_keys("Rahul Shetty")

        self.driver.get("https://rahulshettyacademy.com/angularpractice")
        #driver.maximize_window()
        self.driver.find_element(By.NAME, "email").send_keys("shetty")
        self.driver.find_element(By.ID, "exampleCheck1").click()
        sel = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        sel.select_by_visible_text("Male")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        alertText = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text

        assert "Success" in alertText