from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import allure
from allure import attachment_type
from src.wrongs.wrong_errors import GlobalWrong


class BaseClass:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = wait(self.driver, timeout=10, poll_frequency=1)

    def open(self):
        with allure.step(f"Open  browser and navigate to {self.url}"):
            """This method for open the browser"""
            self.driver.get(self.url)

    def is_open_browser(self):
        """This method for checking navigate to url"""
        return self.wait.until(EC.url_to_be(self.url))

    def make_screenshoin_in_report(self, new_name):
        """This method for added screenshot in allure report """
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=new_name,
            attachment_type=attachment_type.PNG
        )

    def select_element_is_visibility(self, locator):
        """This method for select one element if element visibility"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def select_element_is_present(self, locator):
        """This method for select one element if element presence"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def select_element_is_clickable(self, locator):
        """This method for select one element if element clickable"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_to(self, locator):
        """This method use JavaScript function, after getting
         locator and scroll to element"""
        element = self.select_element_is_present(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def select_element(self, locator, key_value):
        """This method for select element in dropdown list """
        option = self.select_element_is_present(locator)
        options_value = Select(option)
        return options_value.select_by_value(key_value)

    def assert_title(self, word, result):
        """This method for checking title in web pages"""
        value_word = word.text
        if value_word != result:
            self.make_screenshoin_in_report(f"Issue  Current word: {value_word}")
            assert False, GlobalWrong.WRONG_TITLE.value

    def assert_url(self, result):
        """This method for checking url in web pages"""
        if self.driver.current_url != result:
            self.make_screenshoin_in_report(f"Issue url is not current. view URL {self.driver.current_url}")
            assert False, GlobalWrong.WRONG_URL.value

    def add_js(self, element):
        """This method for use JavaScript"""
        return self.driver.execute_script(element)


    



