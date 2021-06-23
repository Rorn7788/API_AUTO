# -*- coding:utf-8 -*-
# author:jasmine xie

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestDemo():
    def setup_method(self,method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}

    def teardown_method(self,method):
        self.driver.quit()

    def test_demo(self):
        #self.driver.get("https://home.testing-studio.com/")
        self.driver.find_element(By.LINK_TEXT,"分类").click()
        sleep(5)