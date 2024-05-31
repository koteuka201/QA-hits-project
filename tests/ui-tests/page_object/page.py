from .locators import MainPageLocators, ResultPageLocators

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def is_title_matches(self):
        return 'This is demo app' == self.driver.title

    def fill_data(self,data):
        element = self.driver.find_element(*MainPageLocators.NUM_INPUT)
        element2=self.driver.find_element(*MainPageLocators.PREREQUISISTES_INPUT)
        element.send_keys(data.get('numCourses'))
        element2.send_keys(data.get('prerequisites'))

    def click_send_button(self):
        element=self.driver.find_element(*MainPageLocators.SEND_BUTTON)
        element.click()

class ResultPage(BasePage):
    def is_result_found(self):
        '''
            в виду специфичности моей задачи, функция возвращает лишь true/false,
            поэтому тут описана логика проверки что false нет в ответе
        '''
        return "fasle" not in self.driver.page_source

    def get_result(self):
        result = self.driver.find_element(*ResultPageLocators.RESULT)
        return result.text

class ErrorPage(BasePage):
    def is_title_matches(self, title):
        return title == self.driver.title