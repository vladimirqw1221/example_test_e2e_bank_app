import time
from selenium.common import TimeoutException
import allure
from selenium.webdriver.support import expected_conditions as EC
from base_class.base_class import BaseClass
from locators.locators import LocatorsBankManagerLogin
from generator.generator_data import generate_data


class BankManagerLogin(BaseClass):
    locator = LocatorsBankManagerLogin()

    @allure.step("Create a new user in system ")
    def create_new_account_user(self):
        add_data = next(generate_data())
        self.first_name = add_data.first_name
        self.last_name = add_data.last_name
        self.post_code = add_data.post_code
        self.select_element_is_clickable(self.locator.MANAGER_LOGIN_BTN).click()
        self.select_element_is_clickable(self.locator.ADD_CUSTUMER_BTN_LOGIN).click()
        word = self.select_element_is_visibility(self.locator.INPUT_FIRST_NAME)
        self.assert_title(word, "First Name :")
        self.select_element_is_visibility(self.locator.INPUT_DATA_FIRT_NAME).send_keys(self.first_name)
        self.select_element_is_visibility(self.locator.INPUT_DATA_LAST_NAME).send_keys(self.last_name)
        self.select_element_is_visibility(self.locator.INPUT_DATA_POST_COSE).send_keys(self.post_code)
        self.select_element_is_clickable(self.locator.ADD_CUSTUNER_BTN).click()
        time.sleep(5)
        alert = self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert
        assert alert.text.split()[2] == "successfully", "This costumer not is added in base"
        alert.accept()


    @allure.step("Checking account for created new user in base list")
    def checking_account_for_new_user(self):
        try:
            self.select_element_is_clickable(self.locator.OPEN_ACCOUNT_BTN).click()
            time.sleep(4)
            account_list = self.wait.until(EC.presence_of_all_elements_located(self.locator.ACCOUNT_LIST))
            assert self.first_name in account_list[5].text, "First name is not show in dropdown list "
            assert self.last_name in account_list[5].text, "Last name is not show in dropdown list "
        except AssertionError:
            self.make_screenshoin_in_report(f"Issue param in not list ")
            assert False, "Issue param in not list"

    @allure.step("Choose a new user in list")

    def switch_to_account(self):
        self.select_element(self.locator.SELECT_ACCOUNT_LIST, "5")
        self.select_element(self.locator.CURRENCY_LIST, "Dollar")
        self.select_element_is_clickable(self.locator.PROCESS_BTN).click()
        alert = self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert
        assert alert.text.split()[5] == "Number", "This alert in not show word Number"
        alert.accept()

    @allure.step("Checking new user in customer list")
    def check_new_user_in_customer_list(self):
        self.select_element_is_clickable(self.locator.CUSTUMER_LIST_BTN).click()

        list_customer = self.wait.until(EC.presence_of_all_elements_located(self.locator.CUSTUNER_LIST))

        assert self.first_name in list_customer[5].text, "Firs name in not view in created new user"
        assert self.last_name in list_customer[5].text, "FLast name in not view in created new user"
        assert self.post_code in list_customer[5].text, "Post code in not view in created new user"

    @allure.step("Search new user in customer list")
    def search_new_user(self):
        self.select_element_is_clickable(self.locator.CUSTUMER_LIST_BTN).click()
        self.select_element_is_visibility(self.locator.SEARCH_INPUT).send_keys(self.first_name)

        list_customer = self.wait.until(EC.presence_of_all_elements_located(self.locator.CUSTUNER_LIST))
        assert self.first_name in list_customer[0].text, "Firs name in not view in created new user"
        assert self.last_name in list_customer[0].text, "FLast name in not view in created new user"
        assert self.post_code in list_customer[0].text, "Post code in not view in created new user"

    def delete_user_in_customer_list(self):
        try:
            self.select_element_is_clickable(self.locator.CUSTUMER_LIST_BTN).click()
            self.select_element_is_visibility(self.locator.SEARCH_INPUT).send_keys(self.first_name)
            if self.first_name:
                self.select_element_is_clickable(self.locator.DELETE_BTN).click()

            else:
                self.make_screenshoin_in_report("Issue data not delete")
                assert False, "Data not delete"
                list_customer = self.wait.until(EC.presence_of_all_elements_located(self.locator.CUSTUNER_LIST))
                assert list_customer == False, "Test Fail"
        except TimeoutException:
            self.select_element_is_clickable(self.locator.HOME_BTN).click()
