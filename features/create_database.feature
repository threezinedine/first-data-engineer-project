Feature: Create database
    Scenario: Create non-existed database
        Given the database connector with host: 127.0.0.1, username: root, password: NnTeTo@Ml171002
        When create the database named "testing_database"
        Then the database is created
        And the database points directly to the new database
        And the database is deleted

    Scenario: Connect directly to the database
        Given the database connector with host: 127.0.0.1, username: root, password: NnTeTo@Ml171002
        And the database named "created_database" is created
        When create the database named "created_database"
        Then the database points directly to the new database
        And the database is deleted

    Scenario: Create a table from a table setup
        Given the database connector with host: 127.0.0.1, username: root, password: NnTeTo@Ml171002
        And create a database object named "create_table_test"
        When create a table named "test_table" object with "id" column
        Then the table is existed
        And the database is deleted
