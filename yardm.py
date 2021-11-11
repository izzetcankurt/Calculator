import sys
from PyQt5.QtWidgets import QApplication
from kullan import Arayüz

uygulama = QApplication(sys.argv)

hesap = Arayüz()

sys.exit(uygulama.exec_())