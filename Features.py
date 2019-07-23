from selenium.webdriver.common.by import By
from features.lib.pages import BasePage


class SignIn(BasePage):
    dict_login = {
        'email_field': [By.Id, 'Login)username'],
        'password_field': [By.Xpath, '//div[@class="g-page-boxcontant"'],
        'continue_button': [By.Id, 'continue_button'],
        't_fa_field': [By.Id, 'Code'],
        'sign_in_button': [By.Id, 'sign_button']
    }

    def __init__(self,driver):
        super(SignIn).__init__(driver)
        self.base_url = '{}{}{}'.format(self.config_env.url, self.config_env.language_url, self.config_env.login_url)
        self.timeout = 15

    def input_id(self, Id):
        self.email_field.clear()
        self.email_field.send_keys(Id)

    def input_password(self, password):
        self.password_field.clear()
        self.password_field.send_keys(password)

    def click_on_button(self):
        self.continue_button.click()

    def input_2fa_(self, code='0000'):
        self.t_fa_field.clear()
        self.t_fa_field.send_keys(code)

    def click_on_sign_in(self):
        self.sign_in_button.click()
