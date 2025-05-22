from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QHeaderView
)
from PyQt6.QtGui import QFont, QColor, QBrush
from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlQuery


class TodoTable(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("📋 Todo List")
        self.setFixedWidth(500)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        title = QLabel("📝 All Todos")
        title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        layout.addWidget(title)

        # Table setup
        self.todo_table = QTableWidget()
        self.todo_table.setColumnCount(2)
        self.todo_table.setHorizontalHeaderLabels(['Todo Name', "Completed"])
        self.todo_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.todo_table.setAlternatingRowColors(True)
        self.todo_table.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff;
                alternate-background-color: #f3f4f6;
                border: 1px solid #d1d5db;
                border-radius: 8px;
            }
            QHeaderView::section {
                background-color: #2563eb;
                color: white;
                font-weight: bold;
                padding: 6px;
                border: none;
            }
        """)

        layout.addWidget(self.todo_table)
        self.setLayout(layout)

        self.get_todos()

    def get_todos(self):
        query = QSqlQuery()
        query.exec('SELECT name, completed FROM todos')

        while query.next():
            row = self.todo_table.rowCount()
            self.todo_table.insertRow(row)

            self.todo_table.setItem(row, 0, QTableWidgetItem(query.value(0)))

            status_text = "✅ Completed" if query.value(1) else "⏳ Pending"
            status_item = QTableWidgetItem(status_text)
            status_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.todo_table.setItem(row, 1, status_item)

    def add_todo_item(self, name, completed):
        row_position = self.todo_table.rowCount()
        self.todo_table.insertRow(row_position)

        name_item = QTableWidgetItem(name)
        status_text = "✅ Completed" if completed else "⏳ Pending"
        status_item = QTableWidgetItem(status_text)
        status_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        self.todo_table.setItem(row_position, 0, name_item)
        self.todo_table.setItem(row_position, 1, status_item)
