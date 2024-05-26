#Bibliotecas

import pytest
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

class Teste_Produtos():

    def setup_method(self,method):                          # Método de inicialização dos testes
        self.driver = webdriver.Chrome()             # instancia o objeto do selenium webdriver como chrome
        vars = {}

    def teardown_method(self,method):
        self.driver.quit()

    def test_selecionar_produto(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.set_window_size(1382,784)
        self.driver.find_element(By.ID, "user-name").click() #
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.NAME, "login-button").click()
        


    



