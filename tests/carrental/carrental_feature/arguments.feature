@all_arguments
Feature: Step Arguments


    Scenario: Arguments for given, when and Then

        Given there are 5 cucumbers
        When I eat 3 cucumbers
        And I eat 2 cucumbers
        Then I should have 0 cucumbers

    @bdd_outline
    Scenario Outline: Outlined given,when and Then

        Given there are <begin> kiwi
        *     I bought <add> kiwi

        When I ate <eat> kiwi
        *    My bro <bro_eat> kiwi

        Then There should left <left> kiwi

        @small_numbers
        Examples: small numbers

        |begin|add|eat|bro_eat|left|
        |10   |5  |3  |7      | 5  |
        |30   |13 |8  |10     | 25 |
        |8    |5  |2  |4      | 7  |


        @big_numbers
        Examples: big numbers

        |begin|add|eat|bro_eat|left|
        |100  |50 |30 |70     | 50 |
        |30   |13 |8  |10     | 25 |
        