## SeleniumTests

This project contains automated tests for order processing on a web application https://tapsshop.pl/.


## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command:
'pip install -r requirements.txt'
3. Ensure you have the Chrome web browser installed on your machine.

## Configuration

The test configuration is stored in the 'config/config.yml' file. The configuration options include:
- 'base_url': The base URL of the web application to be tested.
- 'headless': Boolean value indication whether to run the tests in headless mode.
- 'fullscreen': Boolean value indication whether to start the Chrome browser in fullscreen mode.
- 'max_wait': Maximum wait time (in seconds) for elements to lead on web pages.
- 'rerun': Number of times to rerun failed tests.

Feel free to modify these settings according to your test requirements.

## Running Tests

To run tests, you can use the pytest framework. To run all tests, navigate to the project root directory and run: 
'pytest'

## Test Cases

The 'test_order_processing.py' module contains test cases for the order processing functionality of the web application.

## Test Reports and Screenshots

When a test fails, a screenshot of the web page at the time of failure is captures and saved in the screenshots directory.

If a report is generated, the screenshot is then attached to the test report.

The 'conftest.py' file contains the necessary hooks and logic to capture and attach the screenshots to the test reports.

To create test report, you can run following command:
'pytest --html=report.html'
