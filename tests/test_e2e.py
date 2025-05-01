import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.ShopPage import ShopPage
from pageObjects.HomePage import HomePage
from pageObjects.ConfirmPage import ConfirmPage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        """
        This script automates a series of actions using Selenium WebDriver with Chrome browser, including:

        1. Navigating to the specified URL.
        2. Interacting with elements such as buttons, links, and input fields.
        3. Adding a specific product (Blackberry) to the cart by iterating through product cards.
        4. Proceeding to checkout and filling out the form to complete the purchase.
        5. Selecting the delivery location (India) from a dropdown.
        6. Verifying the success message upon successful form submission.

        The script uses the Page Object Design Pattern to organize and encapsulate webpage elements and actions, improving maintainability and reusability. 
        The path to the ChromeDriver is fetched from the environment variable 'CHROMEDRIVER_PATH', allowing flexibility in specifying the path based on the user's system configuration.

        Usage:
        - This test is useful for automating shopping cart interactions, form submissions, and verifying success messages in a web application.
        - It demonstrates the use of explicit waits, parameterized locators, and modularized test code.
        """

        # Set an implicit wait time of 15 seconds for all elements
        self.driver.implicitly_wait(15)

        # Create an instance of the HomePage object
        homePage = HomePage(self.driver)

        shopPage = homePage.shopItems()
    

        # # Click on the 'shop' link on the home page
        # homePage.shopItems().click()
        # # Create an instance of the ShopPage object
        # shopPage = ShopPage(self.driver)

        # Get the list of product cards on the shop page
        cards = shopPage.getCardTitles()

        # Initialize a counter to track the index of the product card
        i = -1
        # Iterate through the product cards to find the one with the name "Blackberry"
        for card in cards:
            i = i + 1  # Increment the counter
            # Extract the text from the current product card
            cardText = card.text

            # Check if the current product card matches the desired product name
            if cardText == "Blackberry":
                # Click the 'Add to Cart' button for the matching product
                shopPage.getCardFooter()[i].click()

        # Click the 'Checkout' button to proceed to the cart
        shopPage.shopCheckoutItems().click()
        # Click the 'Cart Checkout' button to proceed to the confirmation page
        shopPage.cartCheckoutItems().click()

        # Create an instance of the ConfirmPage object
        confirmPage = ConfirmPage(self.driver)
        # Enter the delivery location by typing 'Ind' in the country search field
        confirmPage.getDeliveryLocation().send_keys("Ind")

        # Select 'India' from the dropdown list
        confirmPage.getDropdownIndia().click()

        # Click the checkbox to agree to the terms and conditions
        confirmPage.getCheckBox().click()

        # Click the 'Purchase' button to complete the transaction
        confirmPage.getPurchaseButton().click()

        # Capture the success message displayed after the purchase
        success_message = confirmPage.getSuccessMessage().text
        # Print the success message to the console
        print(success_message)

        # Assert that the success message contains the expected text
        assert "Success! Thank you!" in success_message
