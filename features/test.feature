# -- FILE: features/test.feature
Feature: Testing the fizzbuzz.py script

  Scenario: Check numbers to be multiples of three
    Given range of integer numbers from -100 to 100
    When executing the fizzbuzz.py script with numbers from the given range one by one as its argument to check results
    Then check if all result types are present