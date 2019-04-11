# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '27March02.10.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets 
from difflib import SequenceMatcher
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog ,QMessageBox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class Ui_Dialog(QWidget):
   
    def setupUi(self, Dialog):
        Dialog.setObjectName("mail")
        Dialog.resize(754, 429)
        self.gonder_text = QtWidgets.QLineEdit(Dialog)
        self.gonder_text.setGeometry(QtCore.QRect(40, 60, 311, 31))
        self.gonder_text.setInputMask("")
        self.gonder_text.setText("")
        self.gonder_text.setFrame(True)
        self.gonder_text.setObjectName("gonder_text")
        self.alici_text = QtWidgets.QLineEdit(Dialog)
        self.alici_text.setGeometry(QtCore.QRect(370, 60, 350, 31))
        self.alici_text.setObjectName("alici_text")
        self.konu = QtWidgets.QLineEdit(Dialog)
        self.konu.setGeometry(QtCore.QRect(40, 130, 180, 31))
        self.konu.setObjectName("konu")
        self.mesaj = QtWidgets.QTextEdit(Dialog)
        self.mesaj.setGeometry(QtCore.QRect(40, 170, 681, 181))
        self.mesaj.setObjectName("mesaj")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(380, 30, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.add_alici_b = QtWidgets.QPushButton(Dialog)
        self.add_alici_b.setGeometry(QtCore.QRect(550, 100, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_alici_b.setFont(font)
        self.add_alici_b.setObjectName("add_alici_b")
        self.add_alici_b.clicked.connect(self.alici_ekle) 
        
        self.dekle=QtWidgets.QPushButton(Dialog)
        self.dekle.setGeometry(QtCore.QRect(600,380,100,41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dekle.setFont(font)
        self.dekle.setObjectName("dosya_ekle")
        self.dekle.clicked.connect(self.dosya_ekle)
        font = QtGui.QFont()
        font.setPointSize(12)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sifre_text = QtWidgets.QLineEdit(Dialog)
        self.sifre_text.setGeometry(QtCore.QRect(170, 100, 181, 25))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.sifre_text.setFont(font)
        self.sifre_text.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.sifre_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sifre_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sifre_text.setPlaceholderText("Sifre")
        self.sifre_text.setObjectName("sifre_text")
        self.gonder_b = QtWidgets.QPushButton(Dialog)
        self.gonder_b.setGeometry(QtCore.QRect(100, 380, 111, 41))
        self.gonder_b.setObjectName("gonder_b")
        self.gonder_b.clicked.connect(self.gonder)
        self.temizle_b = QtWidgets.QPushButton(Dialog)
        self.temizle_b.setGeometry(QtCore.QRect(230, 380, 111, 41))
        self.temizle_b.setObjectName("temizle_b")
        self.temizle_b.clicked.connect(self.temizle) 
        self.mesaj.setPlaceholderText("Mesaj")
        self.konu.setPlaceholderText("Konu")
        self.gonder_text.setPlaceholderText("example@gmail.com")
        self.alici_text.setPlaceholderText("example@hotmail.com")
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.gonder_text, self.mesaj)
        Dialog.setTabOrder(self.mesaj, self.add_alici_b)
        Dialog.setTabOrder(self.add_alici_b, self.alici_text)
        Dialog.setTabOrder(self.alici_text, self.konu)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Gönderen"))
        self.label_2.setText(_translate("Dialog", "Alıcı"))
        self.add_alici_b.setText(_translate("Dialog", "Alıcı Ekle"))
        self.sifre_text.setInputMask(_translate("Dialog",""))
        self.gonder_b.setText(_translate("Dialog", "Gonder"))
        self.temizle_b.setText(_translate("Dialog", "Temizle"))  
        self.dekle.setText(_translate("Dialog","Dosya Ekle"))



    alicilar=[]
    def alici_ekle(self):
        if self.alici_text.text()=='' or self.alicilar=='' :
            self.empty_text("Alici Girmediniz.")               
        else:
            if self.alici_text.text() in self.alicilar:  
                self.bli(self.alici_text.text()+" Kişisi Zaten Listeye Ekli")            
            else:   
                self.alicilar.append(self.alici_text.text())
                self.alici_text.clear()

    def temizle(self):
        self.alici_text.clear()
        self.konu.clear()
        self.gonder_text.clear()
        self.mesaj.clear()
        self.sifre_text.clear()
        self.alicilar.clear()
        self.FileName=''   

    def bli(self,gelen_isim):
        QMessageBox.about(self,"Işlem Başarılı",gelen_isim)

    def bsiz(self,gelen_isim):
        QMessageBox.about(self,"Işlem Başarısız",gelen_isim)

    def empty_text(self,gelen_isim):
        QMessageBox.about(self, "Hata",gelen_isim) 
        
    def kntrl_text(self):
         if self.gonder_text.text() == '' or self.sifre_text.text()=='' or  self.konu.text()=='' or self.mesaj.toPlainText() =='':
            return True
    FileName=""
    def dosya_ekle(self):
        options = QFileDialog.Option()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self,"","", options=options)
        if filename:
            self.bli(filename+" Dosyası Eklendi " )
            self.FileName=filename
           
             
    def gonder(self):
        if (self.kntrl_text() != True):  # Gelenin boş olup olmamasını kontrol eder 
            if self.alicilar !='' or self.alici_text.text()!='': #alicilarin boş olup olmamasını kontrol eder
                gonderici_mail = self.gonder_text.text()
                gonderici_sifre = self.sifre_text.text()
                konu=self.konu.text()
                mesaj=self.mesaj.toPlainText()
                newAlicilar= ','.join(self.alicilar)
                try:
                    msg = MIMEMultipart()
                    msg['From'] = gonderici_mail
                    msg['To'] = newAlicilar     
                    msg['Subject'] = konu
                    body = mesaj
                    msg.attach(MIMEText(body,'plain'))
                    if self.FileName:
                        filename=self.FileName
                        attachment =open(filename,'rb')
                        part = MIMEBase('application','octet-stream')
                        part.set_payload((attachment).read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition',"attachment; filename= "+filename.split('/')[-1]) #Filaname için split yapmadıgımız zaman belgenin bulundugu dizinlerin yolunuda dosya ismi olarak eklemektedir bu yüzden split yaparak belgenin adını /lara göre böldük ve list haline getirdik listenin son elemanını çagırdık.
                        msg.attach(part)
                    text = msg.as_string() 
                    server = smtplib.SMTP('smtp-mail.outlook.com',587)   # smtp-mail.outlook.com      smtp.gmail.com
                    server.starttls()
                    server.login(gonderici_mail,gonderici_sifre)
                    server.sendmail(gonderici_mail,self.alicilar,text)
                    self.bli(newAlicilar+" Kişisine Gönderim Yapıldı") 
                    server.quit()
                except Exception as a : 
                    self.bsiz("Gönderme İşlemi Başarısız oldu Lütfen Bilgilerinizi Kontrol ediniz.") 
                    print(a)
            else:
                self.empty_text("Gönderici Girmediniz.")  
        else:
            self.empty_text("Lütfen Tüm Girişleri Doldurunuz")
           

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())