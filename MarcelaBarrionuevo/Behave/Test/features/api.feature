Feature: API

  Scenario: API example
    Given I have connection to "http://todo.ly"
    When I GET my request
    Then I receive status code 200
 