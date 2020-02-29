Feature: Login

    Allows users to login to our systems.

    Scenario: User logins with correct username and password
        Given our service is running correctly
        When the users tries to login with correct credentials
        Then the user gets back a token
        And the status code is "200"

    Scenario: User logins with incorrect username and password
        Given our service is running correctly
        When the users tries to login with incorrect credentials
        Then the user doesn't get back a token
        And the status code is "401"