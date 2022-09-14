from behave import given, when, then
from mysql.connector import connect
from src.main.cores import Database



@given("the database connector with host: {host}, username: {username}, password: {password}")
def given_a_connection_to_mysql_server(context, host, username, password):
    context.conn = connect(host=host, user=username, password=password)
    context.cursor = context.conn.cursor()

@given("the database named \"{database_name}\" is created")
def given_a_database_is_created(context, database_name):
    context.database_name = database_name
    context.cursor.execute(f"CREATE DATABASE {database_name}") 

@given("create a database object named \"{database_name}\"")
def given_a_created_database_obj(context, database_name):
    context.database = Database(context.conn, database_name)

@given("create a table named \"{table_name}\" object with \"{column_name}\" column")
def given_a_table_obj_with_a_column(context, table_name, column_name, column_type):
    context.table_name = table_name
    context.table = Table(name=table_name, columns=[
            IntColumn(name=column_name)
        ])

@when("the database creates the table")
def when_the_database_creates_the_table(context):
    context.database.create(context.table)

@when("create the database named \"{database_name}\"")
def when_creating_the_database_name(context, database_name):
    context.database_name = database_name
    context.testing_database = Database(context.conn, database_name)

@then("the database points directly to the new database")
def then_the_database_points_directly_to_the_new_database(context):
    assert context.conn.database == context.database_name

@then("the database is created")
def then_the_database_is_created(context):
    context.cursor.execute("SHOW DATABASES")
    databases = context.cursor.fetchall()

    assert (context.database_name,) in databases

@then("the table is existed")
def then_the_table_is_existed(context):
    context.cursor.execute("SHOW TABLES")
    tables = context.cursor.fetchall()

    assert (context.table_name, ) in tables

@then("the database is deleted")
def then_the_database_is_deleted(context):
    context.cursor.execute(f"DROP DATABASE {context.database_name}")
