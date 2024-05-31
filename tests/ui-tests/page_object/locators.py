from selenium.webdriver.common.by import By

class MainPageLocators(object):
    NUM_INPUT=(By.NAME, 'numCourses')
    PREREQUISISTES_INPUT=(By.NAME, 'prerequisites')
    SEND_BUTTON=(By.ID, 'go')

class ResultPageLocators(object):
        RESULT=(By.TAG_NAME, 'pre')