import page_object.page as page
from page_object.locators import MainPageLocators

class TestAppUI:
    def test_app_title_matches(self,browser):
        main_page=page.MainPage(browser)

        assert main_page.is_title_matches()

    def test_app_main_page_has_numCourses_input(self,browser):
        main_page=page.MainPage(browser)

        assert main_page.driver.find_element(*MainPageLocators.NUM_INPUT)

    def test_app_main_page_has_prerequisites_input(self,browser):
        main_page=page.MainPage(browser)

        assert main_page.driver.find_element(*MainPageLocators.PREREQUISISTES_INPUT)

    def test_app_main_page_has_submit_button(self,browser):
        main_page=page.MainPage(browser)

        assert main_page.driver.find_element(*MainPageLocators.SEND_BUTTON)

    def test_app_result_is_true_if_data(self, browser):
        '''
            В виду специфики моей задачи, функция возвращает лишь true/false,
            поэтому в page описана логика проверки что false нет в ответе
        '''
        main_page=page.MainPage(browser)
        main_page.fill_data({
            'numCourses': 2,
            'prerequisites': '1,0'
        })
        main_page.click_send_button()

        result_page=page.ResultPage(browser)

        assert result_page.is_result_found()

    def test_app_error_if_prerequisites_i_equal(self,browser):
        main_page=page.MainPage(browser)
        main_page.fill_data({
            'numCourses': 2,
            'prerequisites': '1,1;1,1'
        })
        main_page.click_send_button()
        error_page=page.ErrorPage(browser)

        assert error_page.is_title_matches("400 Bad Request")