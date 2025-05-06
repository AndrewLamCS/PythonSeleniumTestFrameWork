from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

import pytest


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["firstName"])
        homePage.getEmail().send_keys(getData["lastName"])
        self.selectOptionByText(homePage.getGender(), getData["gender"])

        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        alertText = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text

        assert "Success" in alertText
        self.driver.refresh()

    @pytest.fixture(params=[
        {"firstName": "Rahul", "lastName": "Shetty", "gender": "Male"},
        {"firstName": "Andrew", "lastName": "Lam", "gender": "Male"}
    ])
    def getData(self, request):
        """
        Fixture to provide test data for form submission.

        Returns:
            dict: A dictionary containing test data for the form.
        """
        return request.param