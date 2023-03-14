from base_app import BasePage
from selenium.webdriver.common.by import By
import random
import string


class SearchLocators:
    LOCATOR_USER_NAME = (By.ID, "userName")
    LOCATOR_USER_EMAIL = (By.ID, "userEmail")
    LOCATOR_USER_CURRENT_ADDRESS = (By.ID, "currentAddress")
    LOCATOR_PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    LOCATOR_BUTTON_SUBMIT = (By.ID, "submit")


class SearchOutputLocators:
    LOCATOR_USER_NAME = (By.XPATH, "//*[@id=\"output\"]//*[@id=\"name\"]")
    LOCATOR_USER_EMAIL = (By.XPATH, "//*[@id=\"output\"]//*[@id=\"email\"]")
    LOCATOR_USER_CURRENT_ADDRESS = (By.XPATH, "//*[@id=\"output\"]//*[@id=\"currentAddress\"]")
    LOCATOR_PERMANENT_ADDRESS = (By.XPATH, "//*[@id=\"output\"]//*[@id=\"permanentAddress\"]")


class SearchText(BasePage):
    
    def generate_text(texts):
        if texts == "full_name":
            full_text = {1: "Иван Петрович", 2: "Петр Иванович", 3: "Сидоров Иван", 4: "Евгений петрович"}
        if texts == "email":
            full_text = {1: "ivan@mail.ru", 2: "petr@yandex.ru", 3: "ivan@mail.ru", 4: "eugen@mail.ru"}
        if texts == "current_address":
            full_text = {1: "г.Санкт-Петербург, ул.Василия_гаврилина, д.4", 2: "г.Иванова, ул.Стаханова, д.45",
                         3: "г.Москва, ул.Героев, д.23", 4: "г.Самара, ул.Революции, д.1"}
        if texts == "permanent_address":
            full_text = {1: "г.Санкт-Петербург, ул.Василия-Гаврилина, д.4, кв.74",
                         2: "г.Иванова, ул.Стаханова, д.45, кв.704",
                         3: "г.Москва, ул.Героев, д.23, кв.89",
                         4: "г.Самара, ул.Революции, д.1, кв.90"}
            
        return full_text.get(random.randint(1, 4))
    
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
    
    def enter_word(self, locator, text):
        search_field = self.find_element(locator)
        random_string = SearchText.generate_text(text)
        search_field.send_keys(random_string)
        return random_string
    
    def search_word(self, locator):
        return self.find_element(locator).text.split(":")[1]
    
    def click_on_the_search_button(self):
        return self.find_element(SearchLocators.LOCATOR_BUTTON_SUBMIT, time=2).click()

