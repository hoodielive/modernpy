import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

# Function to load statements from the file
def load_statements(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        statements = file.readlines()
    return statements

class QuizApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quiz App")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel(self)
        self.layout.addWidget(self.label)

        self.entry = QLineEdit(self)
        self.layout.addWidget(self.entry)

        self.check_button = QPushButton("Check Answer", self)
        self.check_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.check_button)

        self.result_label = QLabel(self)
        self.layout.addWidget(self.result_label)

        self.tracker_label = QLabel(self)
        self.layout.addWidget(self.tracker_label)

        self.central_widget.setLayout(self.layout)

        # Load statements
        self.statements = load_statements("odus.txt")
        random.shuffle(self.statements)
        self.current_statement = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        self.statement_word = ""
        self.queries_left = len(self.statements)

        # Display the first statement
        self.next_statement()

    def check_answer(self):
        user_answer = self.entry.text().strip()

        if user_answer == self.statement_word:
            self.correct_answers += 1
            self.result_label.setText("Correct!")
            self.result_label.setStyleSheet("color: green;")
        else:
            self.wrong_answers += 1
            self.result_label.setText(f"Wrong. The correct word (Odu) is: {self.statement_word}")
            self.result_label.setStyleSheet("color: red;")

        self.next_statement()

    def update_tracker(self):
        self.tracker_label.setText(f"Queries Left: {self.queries_left} | Correct: {self.correct_answers} | Wrong: {self.wrong_answers}")

    def next_statement(self):
        if self.current_statement < len(self.statements):
            statement = self.statements[self.current_statement].strip()
            number, statement_text = statement.split('. ', 1)
            self.statement_word = statement_text.split(' ', 1)[0]
            statement_text_hidden = statement_text.replace(self.statement_word, "[Hidden]", 1)

            self.label.setText(f"Oracle #{number}: {statement_text_hidden}")
            self.entry.clear()
            self.current_statement += 1
            self.queries_left -= 1
            self.update_tracker()
        else:
            self.result_label.setText(f"Quiz Completed! You got {self.correct_answers} correct and {self.wrong_answers} wrong.")
            self.result_label.setStyleSheet("color: blue;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuizApp()
    window.show()
    sys.exit(app.exec_())

