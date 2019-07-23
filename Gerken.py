Feature: sign in and access to workspace feature

    Background: on login page
        Given I am on Login page

    Scenario: sign in with valid account
        When I input my ID
        And I input my password
        And I click on continue button
        And I input t_fa_code
        And I click on "Sign In"
        Then user is logged in the system