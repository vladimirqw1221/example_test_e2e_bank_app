from base_class.base_test import BaseTest
import allure
import pytest


@allure.feature("Cteate new user")
class TestCreateCostuner(BaseTest):

    @allure.title("Create new user in data base")
    @allure.severity("CRITICAL")
    @pytest.mark.smoke
    def test_create_new_user(self):
        self.bank_manager_login_page.open()
        self.bank_manager_login_page.is_open_browser()
        self.bank_manager_login_page.create_new_account_user()
        self.bank_manager_login_page.checking_account_for_new_user()
        self.bank_manager_login_page.switch_to_account()
        self.bank_manager_login_page.check_new_user_in_customer_list()

    @allure.title("Search new user in data base")
    @allure.severity("NORMAL")
    @pytest.mark.smoke
    def test_search_new_user_in_list(self):
        self.bank_manager_login_page.open()
        self.bank_manager_login_page.is_open_browser()
        self.bank_manager_login_page.create_new_account_user()
        self.bank_manager_login_page.checking_account_for_new_user()
        self.bank_manager_login_page.switch_to_account()
        self.bank_manager_login_page.search_new_user()

    @allure.title("Delete new user in data base")
    @allure.severity("NORMAL")
    @pytest.mark.smoke
    def test_delete_new_user_in_list(self):
        self.bank_manager_login_page.open()
        self.bank_manager_login_page.is_open_browser()
        self.bank_manager_login_page.create_new_account_user()
        self.bank_manager_login_page.checking_account_for_new_user()
        self.bank_manager_login_page.switch_to_account()
        self.bank_manager_login_page.delete_user_in_customer_list()

