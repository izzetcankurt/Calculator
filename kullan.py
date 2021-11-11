from PyQt5 import QtWidgets
from HesapTasarım2 import Ui_MainWindow

class Arayüz(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.sayi1 = None
        self.sayi2 = False
        super().__init__()
        self.setupUi(self)
        self.show()
        self.label.clear()
        self.buton0.clicked.connect(self.bas)
        self.buton1.clicked.connect(self.bas)
        self.buton2.clicked.connect(self.bas)
        self.buton3.clicked.connect(self.bas)
        self.buton4.clicked.connect(self.bas)
        self.buton5.clicked.connect(self.bas)
        self.buton6.clicked.connect(self.bas)
        self.buton7.clicked.connect(self.bas)
        self.buton8.clicked.connect(self.bas)
        self.buton9.clicked.connect(self.bas)

        self.nokta.clicked.connect(self.ondalik)

        self.yuzde.clicked.connect(self.yuzdelik)

        self.arti.clicked.connect(self.aritmetik)
        self.eksi.clicked.connect(self.aritmetik)
        self.carpi.clicked.connect(self.aritmetik)
        self.bolu.clicked.connect(self.aritmetik)

        self.arti.setCheckable(True)
        self.eksi.setCheckable(True)
        self.carpi.setCheckable(True)
        self.bolu.setCheckable(True)

        self.esittir.clicked.connect(self.sonuc)
        self.esittir.setCheckable(True)

        self.clear.clicked.connect(self.temizle)

    def bas(self):
        olay = self.sender()

        if (self.arti.isChecked() or self.eksi.isChecked() or self.carpi.isChecked() or self.bolu.isChecked()) and (not self.sayi2):
            self.label.setText(format(float(olay.text()), ".15g"))
            self.sayi2 = True
        elif self.esittir.isChecked() and (self.sayi2):
            self.label.setText(format(float(olay.text()), ".15g"))
            self.sayi2 = True
            self.esittir.setChecked(False)
        else:
            if (('.' in self.label.text()) and olay.text() == "0"):
                self.label.setText(format(float(self.label.text() + olay.text()), ".15"))
            else:
                self.label.setText(format(float(self.label.text() + olay.text()), ".15g"))
    def ondalik(self):
        self.label.setText(self.label.text() + ".")

    def aritmetik(self):
        buton = self.sender()
        self.sayi1 = float(self.label.text())
        buton.setChecked(True)

    def yuzdelik(self):
        a = float(self.label.text())
        a = a*0.01
        #self.label.setText(str(a))
        self.label.setText(format(a,".15g"))

    def sonuc(self):
        ikinci = float(self.label.text())
        if self.arti.isChecked():
            yeni = float(self.sayi1) + ikinci
            self.label.setText(format(yeni, ".15g"))
            self.arti.setChecked(False)
        if self.eksi.isChecked():
            yeni = float(self.sayi1) - ikinci
            self.label.setText(format(yeni, ".15g"))
            self.eksi.setChecked(False)
        if self.carpi.isChecked():
            yeni = float(self.sayi1) * ikinci
            self.label.setText(format(yeni, ".15g"))
            self.carpi.setChecked(False)
        if self.bolu.isChecked():
            yeni = float(self.sayi1) / ikinci
            self.label.setText(format(yeni, ".15g"))
            self.bolu.setChecked(False)
        self.esittir.setChecked(True)
    def temizle(self):
        self.label.clear()
        self.sayi1 = 0
        self.sayi2 = False
        self.arti.setChecked(False)
        self.eksi.setChecked(False)
        self.carpi.setChecked(False)
        self.bolu.setChecked(False)
        self.esittir.setChecked(False)