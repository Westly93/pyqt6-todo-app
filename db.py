from PyQt6.QtSql import QSqlDatabase


def open_connection()->bool:
    conn= QSqlDatabase.addDatabase('QSQLITE')
    conn.setDatabaseName('todos.sqlite')
    return conn.open()