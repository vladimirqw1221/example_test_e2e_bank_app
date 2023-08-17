import time
import allure
from selenium.common import TimeoutException

from base_class.base_class import BaseClass
from locators.locators import LocatorsCostumerLogin
import random
from selenium.webdriver.support import expected_conditions as EC



class CostumerLogin(BaseClass):
    locator = LocatorsCostumerLogin()

    @allure.step("Login your account and checking welcome title")
    def navigate_to_costumer_login(self):
        self.select_element_is_clickable(self.locator.COSTUNER_LOGIN_BTN).click()
        self.select_element(self.locator.YOUR_NAME_LIST, "2")
        self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
        word = self.select_element_is_present(self.locator.WELCOME_TITLE)

        self.assert_title(word, "Welcome Harry Potter !!")

    @allure.step("Replenishment deposit and checking balance")
    def replenishment_deposit(self):
        self.select_element_is_clickable(self.locator.DEPOSIT_BTN).click()
        self.randon_balance = random.randint(1000, 5000)
        self.select_element_is_visibility(self.locator.AMOUNT_INPUT).send_keys(f"{self.randon_balance}")
        self.select_element_is_clickable(self.locator.BTN_DONE).click()
        word = self.select_element_is_present(self.locator.WRONG_MSG)
        self.assert_title(word, "Deposit Successful")
        self.balance_info = self.select_element_is_present(self.locator.BALANCE_INFO).text

        assert str(self.randon_balance) == self.balance_info, "This balance in not  the equal current deposit"

    @allure.step("Transfer sum")
    def withdrawn_sum(self):
        self.random_sum = random.randint(1, 999)

        self.select_element_is_clickable(self.locator.WITHDRAWL_BTN).click()
        self.select_element_is_visibility(self.locator.AMOUNT_INPUT).click()
        time.sleep(1)  # if time sleep  need for input (value AMOUNT_INPUT) to he was clickable
        self.select_element_is_visibility(self.locator.AMOUNT_INPUT).send_keys(f"{self.random_sum}")
        self.select_element_is_clickable(self.locator.BTN_DONE_WITHDRAWN).click()
        word = self.select_element_is_present(self.locator.WRONG_MSG)
        self.assert_title(word, "Transaction successful")
        self.balance_info_result = self.select_element_is_present(
            self.locator.BALANCE_INFO).text  # getting current balance\
        # after transfer sum

        result = int(self.balance_info) - self.random_sum  # getting result sum

        assert self.balance_info_result == str(result), "This balance is not equal sum "

    @allure.step("Pay transfer list")
    def transaction_checking(self):
        self.select_element_is_clickable(self.locator.TRANSACTION_BTN).click()
        try:
            result = self.wait.until(EC.presence_of_all_elements_located(self.locator.LIST_TRANSACTION))


            assert str(self.randon_balance) in result[0].text, f"This result in not the value {self.randon_balance}\
            current value {result[0].text}"
            assert str(self.random_sum) in result[1].text, f"This result in not the value {self.random_sum}\
            current value {result[1].text}"
        except TimeoutException:
            self.make_screenshoin_in_report(f"issue: This transactions not available ")
            assert False, "This transactions is not show the list"

    @allure.step("Clear transfer list")
    def reset_transfer_list(self):
        try:
            self.select_element_is_clickable(self.locator.RESET_BTN).click()
            new_list_result = self.wait.until(EC.presence_of_all_elements_located(self.locator.LIST_TRANSACTION))
            if isinstance(new_list_result, list):
                self.make_screenshoin_in_report("Issue list is not clear")
                assert False, "transactions  is not clear"

        except TimeoutException:
            self.select_element_is_clickable(self.locator.HOME_BTN).click()
            word = self.select_element_is_present(self.locator.COSTUNER_LOGIN_BTN)
            self.assert_title(word, "Customer Login")

    @allure.step("Login your account for randon user")
    def navigate_to_costumer_login_in_select_randon_user(self):
        self.select_element_is_clickable(self.locator.COSTUNER_LOGIN_BTN).click()
        user = random.randint(1,5)
        self.select_element(self.locator.YOUR_NAME_LIST, str(user))
        self.select_element_is_clickable(self.locator.LOGIN_BTN).click()
        word = self.select_element_is_present(self.locator.WELCOME_TITLE).text
        assert word.split()[0] == "Welcome", "Header is not show in dashboard"


























