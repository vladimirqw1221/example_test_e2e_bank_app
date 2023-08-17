from feature_pages.costumer_login_page import CostumerLogin
import pytest
from data.data_site import DataSite
from feature_pages.bank_manager_login_page import BankManagerLogin


class BaseTest:
    costumer_login_page: CostumerLogin
    bank_manager_login_page: BankManagerLogin

    @pytest.fixture(autouse=True)
    def setup(self, driver, request):
        request.cls.costumer_login_page = CostumerLogin(driver, DataSite.BASE_URL)

        request.cls.bank_manager_login_page = BankManagerLogin(driver, DataSite.BASE_URL)
