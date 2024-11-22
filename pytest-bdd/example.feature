Feature: Go to on test page on login

  Scenario Outline: Open website and check its title
    Given I want to launch the browser
    When I enter the <website> in the navegation bar and go there
    Then I verify that page by its title

    Examples:
      | website | https://practicetestautomation.com/practice-test-login/ |