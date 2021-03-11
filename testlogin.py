from selenium import webdriver
import unittest
import HtmlTestRunner

class testlogin(unittest.TestCase):

    def setUpClass(cls) :
        cls.driver=webdriver.chrome()
        
