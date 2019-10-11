import sys
from PyQt5.QtWidgets import QApplication
from Menu_window import MenuWindow
from game_window import GameWindow





if __name__ == '__main__':
    app = QApplication([])

    Menu_window = MenuWindow()
    game_window = GameWindow()

    Menu_window.show_game_signal = game_window.show_game_signal

    Menu_window.show()
    
    sys.exit(app.exec_())