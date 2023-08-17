from selenium.webdriver.common.by import By


class LocatorsCostumerLogin:
    COSTUNER_LOGIN_BTN = (By.CSS_SELECTOR, "button[ng-click='customer()']")
    YOUR_NAME_LIST = (By.CSS_SELECTOR, "select[id='userSelect']")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    WELCOME_TITLE = (By.XPATH, "//strong[text()=' Welcome ']")
    DEPOSIT_BTN = (By.XPATH, "//button[normalize-space()='Deposit']")
    AMOUNT_INPUT = (
    By.XPATH, "//input[@placeholder='amount']")  # //input[@placeholder='amount'] #//input[@placeholder='amount']
    BTN_DONE = (By.XPATH, "//button[text()='Deposit']")
    WRONG_MSG = (By.CSS_SELECTOR, "span[class='error ng-binding']")
    BALANCE_INFO = (By.XPATH, "(//strong[@class='ng-binding'])[2]")
    WITHDRAWL_BTN = (By.XPATH, "//button[normalize-space()='Withdrawl']")
    AMOUNT_INPUT_WITHDRAWN = (By.XPATH, "//input[@placeholder='amount']")
    BTN_DONE_WITHDRAWN = (By.CSS_SELECTOR, "button[type='submit']")
    LIST_TRANSACTION = (By.XPATH, "//tr[@class='ng-scope']")
    TRANSACTION_BTN = (By.XPATH, "//button[normalize-space()='Transactions']")
    RESET_BTN = (By.CSS_SELECTOR, "button[class='btn']:nth-child(3)")
    HOME_BTN = (By.CSS_SELECTOR, "button[class='btn home']")


class LocatorsBankManagerLogin:
    MANAGER_LOGIN_BTN = (By.XPATH, "(//button[@class='btn btn-primary btn-lg'])[2]")
    ADD_CUSTUMER_BTN_LOGIN = (By.XPATH, "//button[normalize-space()='Add Customer']")
    INPUT_FIRST_NAME = (By.XPATH, "//label[text()='First Name :']")
    INPUT_DATA_FIRT_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    INPUT_DATA_LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    INPUT_DATA_POST_COSE = (By.XPATH, "//input[@placeholder='Post Code']")
    ADD_CUSTUNER_BTN = (By.XPATH, "//button[@type='submit']")
    ACCOUNT_LIST = (By.XPATH, "//option[@class='ng-binding ng-scope']")
    SELECT_ACCOUNT_LIST = (By.XPATH, "//select[@id='userSelect']")
    OPEN_ACCOUNT_BTN = (By.XPATH, "//button[normalize-space()='Open Account']")
    CURRENCY_LIST = (By.XPATH, "//select[@id='currency']")
    PROCESS_BTN = (By.XPATH, "//button[@type='submit']")
    CUSTUMER_LIST_BTN = (By.XPATH, "//button[normalize-space()='Customers']")
    CUSTUNER_LIST = (By.XPATH, "//tr[@class='ng-scope']")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search Customer']")
    DELETE_BTN = (By.XPATH, "//button[normalize-space()='Delete']")
    HOME_BTN = (By.XPATH, "//button[normalize-space()='Home']")

