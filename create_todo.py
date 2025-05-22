from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QMessageBox, QLabel, QLineEdit,
    QCheckBox, QPushButton, QGroupBox, QFormLayout
)
from PyQt6.QtGui import QFont, QPalette, QColor
from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlQuery

class TodoForm(QWidget):
    def __init__(self, onsubmit_todo_callback):
        super().__init__()

        self.onsubmit_todo_callback = onsubmit_todo_callback
        self.setWindowTitle("Add Todo Item")
        self.setFixedWidth(400)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Group Box for inputs
        form_group = QGroupBox("Todo Details")
        form_group.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        form_layout = QFormLayout()

        # Name input
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter todo name...")
        form_layout.addRow(QLabel("Todo Name:"), self.name_input)

        # Completed checkbox
        self.completed_checkbox = QCheckBox("Mark as Completed")
        form_layout.addRow(QLabel("Completed:"), self.completed_checkbox)

        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: #2563eb;
                color: white;
                font-weight: bold;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #1e40af;
            }
        """)
        self.submit_button.clicked.connect(self.submit_todo)
        main_layout.addWidget(self.submit_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(main_layout)

    def submit_todo(self):
        name = self.name_input.text()
        completed = self.completed_checkbox.isChecked()

        if name:
            query = QSqlQuery()
            query.prepare('INSERT INTO todos (name, completed) VALUES (?, ?)')
            query.addBindValue(name)
            query.addBindValue(completed)
            ok = query.exec()

            if ok:
                self.onsubmit_todo_callback(name, completed)
                QMessageBox.information(self, "Success", "Todo added successfully.")
                self.name_input.clear()
                self.completed_checkbox.setChecked(False)
            else:
                QMessageBox.critical(self, "Error", "Something went wrong. Please try again.")
        else:
            QMessageBox.warning(self, "Validation Error", "Todo Name is required.")
