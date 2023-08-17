from base_class.base_test import BaseTest
import allure
import pytest


@allure.feature("Login page")
class TestCostumerLogin(BaseTest):

    @allure.title("Bank account transfer for native user")
    @allure.severity("NORMAL")
    @pytest.mark.smoke
    def test_costumer_login_pege(self):
        self.costumer_login_page.open()
        self.costumer_login_page.is_open_browser()
        self.costumer_login_page.navigate_to_costumer_login()
        self.costumer_login_page.replenishment_deposit()
        self.costumer_login_page.withdrawn_sum()
        self.costumer_login_page.transaction_checking()
        self.costumer_login_page.reset_transfer_list()

    @allure.title("Bank account transfer for random user")
    @allure.severity("NORMAL")
    @pytest.mark.smoke
    def test_costumer_login_pege_random_user(self):
        self.costumer_login_page.open()
        self.costumer_login_page.is_open_browser()
        self.costumer_login_page.navigate_to_costumer_login_in_select_randon_user()
        self.costumer_login_page.replenishment_deposit()
        self.costumer_login_page.withdrawn_sum()
        self.costumer_login_page.transaction_checking()
        self.costumer_login_page.reset_transfer_list()






















