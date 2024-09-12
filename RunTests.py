# This class will make our lives easier once running test suites
import os

"""Run tests_end2end """

suite = "regression"
os.system(f'pytest -v -s --alluredir=./allure-results/')

# --dist=loadfile -n=4
