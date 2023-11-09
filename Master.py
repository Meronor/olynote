import sys
from PyQt5.QtWidgets import QApplication
from winds import Sing_IN_Wind

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Sing_IN_Wind()
    ex.show()
    sys.exit(app.exec_())