import sys
from PyQt6.QtWidgets import QApplication
from winds import SingInWind

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SingInWind()
    ex.show()

    sys.exit(app.exec())
