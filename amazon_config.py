from selenium import webdriver
import os

DIRECTORY = 'reports'
NAME = 'PS4'
CURRENCY = '€'
MIN_PRICE = '275'
MAX_PRICE = '650'
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}
BASE_URL = "http://www.amazon.de/"


def get_chrome_web_driver(options):
    return webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()

def set_binary_location(options):
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")


def set_ignore_certificate_errors(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito(options):
    options.add_argument('--incognito')

def set_headless(options):
    options.add_argument('--headless')

def set_dev_usage(options):
    options.add_argument('--disable-dev-shm-usage')

def set_sandbox(options):
    options.add_argument('--no-sandbox')