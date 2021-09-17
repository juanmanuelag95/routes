Feature: Taco Truck Part 2
  There are tree new functionality that need to be added to the current project:
    - Restock supplies after at least 80 tacos are ordered.
    - Fresh groceries near the end of the working day.
    - Products that are left at the end of the day he will take home.

@TacoTruck_1
Scenario Outline: Stop for groceries
  Given I have enought supplies to make <stock> tacos
  When I get an order for <number> of tacos
  Then Ask if need to go for supplies
  And The response code is equal to "200"
  And The response body should contain the message <message>
  
  Examples: 
    | stock | number | message  |
    | 100   | 79     | false    |
    | 100   | 80     | true     |
    | 100   | 81     | true     |

@TacoTruck_2
Scenario Outline: Check if in time to stop for groceries
  Given I have enought supplies to make <stock> tacos
  When I check if have to go to the store <hours> before the end of shift
  Then The response code is equal to "200"
  And The response body should contain the message <message>

  Examples: 
    | stock | hours  | message  |
    | 19    | 2      | true     |
    | 19    | 3      | true     |
    | 19    | 4      | false    |

@TacoTruck_3
Scenario: Restock supplies
  Given There are products left by end of day
  When Is the following day
  Then The stock should be enought to make "100" tacos

@E2E
Scenario: E2E on groceries restock
  Given I have enought supplies to make <stock> tacos
  When I get an order for <number> of tacos
  And I check if have to go to the store <hours> before the end of shift
  Then The response code is equal to "200"
  And The response body should contain the message <message>

  Examples: 
    | stock | hours  | number | message  |
    | 100   | 2      | 81     | true     |
    | 100   | 2      | 80     | true     |
    | 100   | 2      | 79     | false    |
    | 100   | 3      | 81     | true     |
    | 100   | 3      | 80     | true     |
    | 100   | 3      | 79     | false    |
    | 100   | 4      | 81     | false    |
    | 100   | 4      | 80     | false    |
    | 100   | 4      | 79     | false    |
    