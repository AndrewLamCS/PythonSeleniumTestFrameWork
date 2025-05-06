import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pytest_addoption(parser):
    """
    Adds a custom command-line option to the pytest framework.

    This function allows the user to specify the browser name to be used during testing
    by adding a `--browser_name` option to the pytest command-line interface. If no value
    is provided, the default browser is set to "chrome".

    Args:
        parser (pytest.Parser): The pytest parser object used to add custom command-line options.
    """
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    """
    This pytest fixture sets up a WebDriver instance for browser automation based on the browser name 
    provided via command-line options. It supports Chrome, Firefox, and Edge browsers. The corresponding 
    driver paths are retrieved from environment variables. The fixture initializes the browser, navigates 
    to a specified URL, and assigns the WebDriver instance to the test class. After the test execution, 
    the browser is closed.
    Args:
        request: A pytest request object that provides access to the test context, including command-line options.
    Yields:
        None: The fixture yields control back to the test, and cleanup (browser closure) is performed after the test.
    """
    browser_name = request.config.getoption("browser_name")  # Get the browser name from command line options

    if browser_name == 'chrome':
        # Get the path to the ChromeDriver from environment variables
        chromedriver_path = os.getenv('CHROMEDRIVER_PATH') 
        # Initialize the Chrome driver with the specified service
        service_obj = Service(chromedriver_path)  
        driver = webdriver.Chrome(service=service_obj)  # Initialize the Chrome WebDriver with the service object

    elif browser_name == 'firefox':
        # Get the path to the GeckoDriver from environment variables
        geckodriver_path = os.getenv('GECKODRIVER_PATH')  
        # Initialize the Firefox driver with the specified service
        service_obj = Service(geckodriver_path)  
        driver = webdriver.Firefox(service=service_obj)

    elif browser_name == 'edge':
        # Get the path to the EdgeDriver from environment variables
        edgedriver_path = os.getenv('EDGEDRIVER_PATH')  
        # Initialize the Edge driver with the specified service
        service_obj = Service(edgedriver_path)  
        driver = webdriver.Edge(service=service_obj)

    # Open the specified URL in the browser
    driver.get("https://rahulshettyacademy.com/angularpractice/")  # Open the webpage
    
    #driver refers to local driver and cls.driver is the class driver
    request.cls.driver = driver

    #Anything after yield will be executed at the end
    yield
    
    # Close the browser after the test execution
    driver.close()

@pytest.fixture()
def dataLoad():
    """
    Fixture to load data for testing.
    This fixture can be used to set up any necessary data or state before running tests.
    """
    print("User profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]

