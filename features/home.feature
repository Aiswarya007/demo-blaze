
Feature: Selection functionality


  @select
  Scenario: Selecting phone
    Given Navigate to home page
    When Select a phone
    And Add the phone to cart
    And Navigate to cart
    Then Item should be available in the cart


  @purchase
  Scenario: Purchase the phone
    Given Navigate to cart
    When Select Place Order
    And Enter the details
        |name|country|city|credit_card|month|year|
        |Ash |India  |Tvm |aaa        |Apr  |2024|
    And Select purchase
    Then Shows Confirmation

