



use_step_matcher("re")


@when('I enter (?P<role>.+)login')
def enter_login(context, role):
    page = LoginPage(context.driver)
    page.specify_login(Configurator(),define_user_role(role))


@step('Enter Company admin (?P<password>.+)')
def enter_password(context, password):
    page = LoginPage(context.driver)
    page.specify_password(Configurator(),default_password(password))

@step('I click "Continue" button')
def click_on_continue(context)
    page = LoginPage(context.driver)
    page.click_continue()

@step('I proceed two factor auth with (?P<code>.+)code')
def two_factor(context, code)
    page = LoginPage(context.driver)
    page.specify_2fa_code(code)

@step('Click on "Sign In" button')
def click_on_signin(context)
    page = LoginPage(context.driver)
    page.click_signin()

@step('I can see (?P<text>.+) message')
def user_see_success_message(context):
    page = LoginPage(context.driver)
    assert page.is_visible('successful_message') == text, "success message is not visible"

