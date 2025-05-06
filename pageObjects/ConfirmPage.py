from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ConfirmPage:
    """
    Page Object Model for the Confirm Page in the application.
    Provides methods to interact with elements on the Confirm Page.
    """

    def __init__(self, driver):
        """
        Initializes the ConfirmPage object.

        Args:
            driver: The WebDriver instance used to interact with the browser.
        """
        self.driver = driver

    # Locators for elements on the Confirm Page
    deliveryLocation = (By.ID, "country")  # Locator for the country search field
    dropdownIndia = (By.LINK_TEXT, "India")  # Locator for the 'India' link in the dropdown
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")  # Locator for the checkbox
    purchaseBtn = (By.XPATH, "//input[@class='btn btn-success btn-lg']")  # Locator for the purchase button
    success = (By.CLASS_NAME, "alert-success")  # Locator for the success message

    def getDeliveryLocation(self):
        """
        Gets the delivery location input field element.

        Returns:
            WebElement: The delivery location input field.
        """
        return self.driver.find_element(*ConfirmPage.deliveryLocation)

    # def getDropdownIndia(self):
    #     """
    #     Waits for and gets the 'India' link in the dropdown.

    #     Returns:
    #         WebElement: The 'India' link element.
    #     """
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
    #     return self.driver.find_element(*ConfirmPage.dropdownIndia)

    def getCheckBox(self):
        """
        Gets the checkbox element.

        Returns:
            WebElement: The checkbox element.
        """
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getPurchaseButton(self):
        """
        Gets the purchase button element.

        Returns:
            WebElement: The purchase button element.
        """
        return self.driver.find_element(*ConfirmPage.purchaseBtn)

    def getSuccessMessage(self):
        """
        Gets the success message element.

        Returns:
            WebElement: The success message element.
        """
        return self.driver.find_element(*ConfirmPage.success)