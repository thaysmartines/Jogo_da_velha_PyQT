import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Jogo_da_velha(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Vamos começar? Jogo da Velha')
        self.setGeometry(100, 100, 300, 400)

        self.turn = 'X'
        self.board = [''] * 9
        self.buttons = [QPushButton('', self) for _ in range(9)]

        layout = QGridLayout()

        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                self.buttons[index].setFixedSize(100, 100)
                button_font = QFont()
                button_font.setPointSize(20)
                self.buttons[index].setFont(button_font)
                self.buttons[index].clicked.connect(lambda _, button=self.buttons[index], index=index: self.make_move(button, index))
                layout.addWidget(self.buttons[index], i, j)

        self.status_label = QLabel(self)
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label, 3, 0, 1, 3)

        self.reset_button = QPushButton('Reset', self)  # Adicione o botão de reset
        self.reset_button.clicked.connect(self.reset_game)  # Conecte o botão à função de reset
        layout.addWidget(self.reset_button, 4, 0, 1, 3)

        self.setLayout(layout)
        self.reset_game()

    def reset_game(self):
        for i in range(9):
            self.board[i] = ''
            self.buttons[i].setText('')
            self.buttons[i].setEnabled(True)

        self.turn = 'X'
        self.status_label.setText('Vez do X')

    def make_move(self, button, index):
        if self.board[index] == '':
            self.board[index] = self.turn
            button.setText(self.turn)
            button.setEnabled(False)
            if self.verificar():
                self.status_label.setText(f'{self.turn} ganhou!')
                for b in self.buttons:
                    b.setEnabled(False)
            elif '' not in self.board:
                self.status_label.setText('Empate!')
            else:
                self.turn = 'O' if self.turn == 'X' else 'X'
                self.status_label.setText(f'Vez do {self.turn}')

    def verificar(self):
        for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '':
                return True
        return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Jogo_da_velha()

    # Estilos CSS para melhorar a aparência
    app.setStyleSheet("""
    QWidget {
        background-color: #303030;
        color: white;
    }
    QPushButton {
        background-color: #007bff;
        border: none;
        font-size: 30px;
        color: white;
        border-radius: 15px;
    }
    QPushButton:disabled {
        background-color: #ccc;
        color: black;
    }
    QPushButtonresetButton {  
        background-color: red;
        color: white;
        font-size: 20px;
        border: none;
        border-radius: 15px;
    }
    QLabel {
        font-size: 24px;
        color: white;
    }
    """)

    window.show()
    sys.exit(app.exec_())
