import pytest
import subprocess
import time


import pytest



BASE_URL = "https://api.example.com"




def pytest_addoption(parser):
    parser.addoption(
        "--site_code", action="store", default="chrome", help="Returning name of browser")

    parser.addoption(
        "--attraction", action="store", default=None, help="Returning name of the domain")

    parser.addoption(
        "--developer", action="store", default="production", help="Returning Headless status")

    parser.addoption(
        "--env", action="store", default="test", help="Returning Headless status")




# POST SESSION actions - HTML report sending by email, Allure report auto open
def pytest_unconfigure(config) -> None:
    """ Open Allure report """
    # filepath = "C:\\AllureReports\\RunAllureLocally.bat"
    # p = subprocess.Popen(filepath, shell=True, stdout=subprocess.PIPE)
    # stdout, stderr = p.communicate()


