from selenium.webdriver.common.by import By
from pageObjects.ShopPage import ShopPage

class HomePage:
    """
    Page Object Model for the Home Page in the application.
    Provides methods to interact with elements on the Home Page.
    """

    def __init__(self, driver):
        """
        Initializes the HomePage object.

        Args:
            driver: The WebDriver instance used to interact with the browser.
        """
        self.driver = driver

    # Locators for elements on the Home Page
    shop = (By.CSS_SELECTOR, "a[href='/angularpractice/shop']")  # Locator for the 'Shop' link
    name = (By.CSS_SELECTOR, "[name='name']")  # Locator for the name input field
    email = (By.NAME, "email")  # Locator for the email input field
    checkbox = (By.ID, "exampleCheck1")  # Locator for the checkbox
    gender = (By.ID, "exampleFormControlSelect1")  # Locator for gender dropdown
    submit = (By.XPATH, "//input[@type='submit']")  # Locator for the submit button
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")  # Locator for success message
    
    def shopItems(self):
        """
        Navigates to the shop page by clicking on the shop element.

        Returns:
            ShopPage: An instance of the ShopPage class initialized with the current driver.
        """
        self.driver.find_element(*HomePage.shop).click()
        shopPage = ShopPage(self.driver)
        return shopPage
    
    def getName(self):
        """
        Retrieves the name input field element.

        Returns:
            WebElement: The name input field element.
        """
        return self.driver.find_element(*HomePage.name)
    
    def getEmail(self):
        """
        Retrieves the email input field element.

        Returns:
            WebElement: The email input field element.
        """
        return self.driver.find_element(*HomePage.email)

    def getCheckbox(self):
        """
        Retrieves the checkbox element.

        Returns:
            WebElement: The checkbox element.
        """
        return self.driver.find_element(*HomePage.checkbox)
    
    def getGender(self):
        """
        Retrieves the gender dropdown element.
        Returns:
            WebElement: gender dropdown element.
        """
        return self.driver.find_element(*HomePage.gender)
    
    def submitForm(self):
        """
        Retrieves the submit button element.
        Returns:
            WebElement: The submit button element.
        """
        return self.driver.find_element(*HomePage.submit)
    
    def getSuccessMessage(self):
        """
        Retrieves the success message element.

        Returns:
            WebElement: The success message element.
        """
        return self.driver.find_element(*HomePage.successMessage)

    
    

