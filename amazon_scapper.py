from selenium import webdriver

url = 'https://www.amazon.com.br/'

class amazon_scraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()
        self.search_bar = 'twotabsearchtextbox'     # search box id
        self.button_search = 'nav-search-submit-text'  # search button id
        self.product_div_class = 'a-size-base-plus a-color-base a-text-normal' #product name div class
    
    def enter_site(self):
        self.driver.get(self.url)
    
    def search_and_enter(self, word = 'None'):
        self.driver.find_element_by_id(self.search_bar).send_keys(word)
        self.driver.find_element_by_id(self.button_search).click()
    
    def grab_product(self):
        self.driver.find_elements_by_class_name(self.product_div_class)
    
a = amazon_scraper(url)
a.enter_site()
a.search_and_enter('banana')