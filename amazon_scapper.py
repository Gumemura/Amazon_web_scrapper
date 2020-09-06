import time 
from selenium import webdriver

'''
# Importar a classe WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
# Importar a classe que contém as funções e aplicar um alias
from selenium.webdriver.support import expected_conditions as EC
# Importar classe para ajudar a localizar os elementos
from selenium.webdriver.common.by import By
'''

url = 'https://www.amazon.com.br/'

class amazon_scraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()
        self.search_bar = 'twotabsearchtextbox'     # search box id
        self.button_search = 'nav-input' # search button class
        self.product_div_class = 'a-size-base-plus' #product name div class
    
    def enter_site(self):
        '''
        Opens the browser on url page
        '''
        self.driver.get(self.url)
    
    def search_and_enter(self, word = 'None'):
        '''
        Type desired word in search box then hits search
        
        :Args:
        word -> the word to be searched
        '''
        self.driver.find_element_by_id(self.search_bar).send_keys(word)
        for elem in self.driver.find_elements_by_class_name(self.button_search):
            if elem.get_attribute("type") == "submit":
                elem.click()
                break
    
    def grab_product(self):
        '''
        
        '''
        for elem in self.driver.find_elements_by_class_name(self.product_div_class):
            print(elem.text)

        
    def time_break(self, break_time):
        '''
        Gives the execution a break
        :Args:
        time -> amount of seconds the break will last
        '''
        time.sleep(break_time)

a = amazon_scraper(url)
a.enter_site()
a.search_and_enter('banana')
a.time_break(2)
a.grab_product()