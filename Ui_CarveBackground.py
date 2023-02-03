from PyQt5.QtCore import QSize, QRect, QMetaObject, QCoreApplication    #For Qt
from PyQt5.QtWidgets import QLabel, QCheckBox, QLineEdit, QPushButton, QMessageBox
from ListWidget import ListWidget

from tkinter import *
from tkinter import filedialog

from pathlib import Path
from PIL import Image
from rembg import remove

import os                   #For email
import smtplib 
import mimetypes                                            
from email import encoders                                  
from email.mime.base import MIMEBase                        
from email.mime.multipart import MIMEMultipart              
import datetime
from email_validate import validate
import zipfile

class Ui_CarveBackground(object):
    save_puth_flag = False
    def setupUi(self, CarveBackground):
        self.__mail_address = "fromme@google.com"
        self.__mail_password = "qwert123"
        self.__default_save_puth = "forarchive/"
        self.__default_img_extension = "_out.png"
        self.__default_archive_extension = ".zip"
        self.__default_archive_name = "carvebackground_arch_result"
        
        if not CarveBackground.objectName():
            CarveBackground.setObjectName(u"CarveBackground")
        CarveBackground.resize(430, 480)
        CarveBackground.setMinimumSize(QSize(430, 465))
        CarveBackground.setMaximumSize(QSize(430, 8888))
        CarveBackground.setStyleSheet(u"color: black;\n"
"font: 63 11pt \"URW Bookman\";")
        
        self.FixedLabel = QLabel(CarveBackground)
        self.FixedLabel.setObjectName(u"FixedLabel")
        self.FixedLabel.setGeometry(QRect(9, 9, 411, 21))
        
        self.puthList = ListWidget(CarveBackground)
        self.puthList.setObjectName(u"puthList")
        self.puthList.setGeometry(QRect(-1, 36, 431, 261))
        
        self.puth_save_label = QLabel(CarveBackground)
        self.puth_save_label.setObjectName(u"puth_save_label")
        self.puth_save_label.setGeometry(QRect(0, 420, 430, 29))
        
        self.mailBox = QCheckBox(CarveBackground)
        self.mailBox.setObjectName(u"mailBox")
        self.mailBox.setGeometry(QRect(0, 360, 215, 29))
        
        self.mailEdit = QLineEdit(CarveBackground)
        self.mailEdit.setObjectName(u"mailEdit")
        self.mailEdit.setGeometry(QRect(215, 360, 215, 29))
        
        self.save_puthButton = QPushButton(CarveBackground)
        self.save_puthButton.setObjectName(u"save_puthButton")
        self.save_puthButton.setGeometry(QRect(0, 390, 430, 29))
        
        self.ApplyButton = QPushButton(CarveBackground)
        self.ApplyButton.setObjectName(u"ApplyButton")
        self.ApplyButton.setGeometry(QRect(0, 450, 430, 29))
        
        self.open_select_puthButton = QPushButton(CarveBackground)
        self.open_select_puthButton.setObjectName(u"open_select_puthButton")
        self.open_select_puthButton.setGeometry(QRect(0, 330, 431, 29))
        
        self.deleteButton = QPushButton(CarveBackground)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(0, 299, 215, 29))
        
        self.deleteallButton = QPushButton(CarveBackground)
        self.deleteallButton.setObjectName(u"deleteallButton")
        self.deleteallButton.setGeometry(QRect(215, 299, 215, 29))

        self.retranslateUi(CarveBackground)

        self.connect_signal()
        
        QMetaObject.connectSlotsByName(CarveBackground)

    def new_method(self):
        self.puthList.setAcceptDrops(True)
    # setupUi

    def retranslateUi(self, CarveBackground):
        CarveBackground.setWindowTitle(QCoreApplication.translate("CarveBackground", u"\u0412\u044b\u0440\u0435\u0437\u043a\u0430 \u0444\u043e\u043d\u0430", None))
        self.FixedLabel.setText(QCoreApplication.translate("CarveBackground", u"\u0412\u044b\u0431\u0438\u0440\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u0438\u043b\u0438 \u043f\u0435\u0440\u0435\u0442\u0430\u0449\u0438\u0442\u0435 \u0441\u044e\u0434\u0430 \u043d\u0443\u0436\u043d\u044b\u0435 \u0444\u0430\u0439\u043b\u044b", None))
        self.puth_save_label.setText(QCoreApplication.translate("CarveBackground", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))
        self.mailBox.setText(QCoreApplication.translate("CarveBackground", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043d\u0430 \u043f\u043e\u0447\u0442\u0443", None))
        self.save_puthButton.setText(QCoreApplication.translate("CarveBackground", u"\u041f\u0430\u043f\u043a\u0430 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))
        self.ApplyButton.setText(QCoreApplication.translate("CarveBackground", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.open_select_puthButton.setText(QCoreApplication.translate("CarveBackground", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.deleteButton.setText(QCoreApplication.translate("CarveBackground", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.deleteallButton.setText(QCoreApplication.translate("CarveBackground", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u0441\u0435", None))
    # retranslateUi
    
    def connect_signal(self):
        self.deleteButton.clicked.connect(lambda: self.deleteButton_clicked())
        self.deleteallButton.clicked.connect(lambda: self.deleteallButton_clicked())
        self.open_select_puthButton.clicked.connect(lambda: self.open_select_puthButton_clicked())
        self.save_puthButton.clicked.connect(lambda: self.save_puthButton_clicked())
        self.mailBox.stateChanged.connect(lambda: self.mailBox_changed())
        self.ApplyButton.clicked.connect(lambda: self.ApplyButton_clicked())
     
    def deleteallButton_clicked(self):
        self.puthList.clear()
        
    def deleteButton_clicked(self):
        self.puthList.takeItem(self.puthList.currentRow())
    
    def open_select_puthButton_clicked(self):
        ftypes =  [('image ', '.png .jpg')]
        filepath = filedialog.askopenfilenames(filetypes = ftypes)
        if filepath != "":
            self.puthList.addItems(filepath)
        
    def mailBox_changed(self):
        self.mailEdit.setEnabled(self.mailBox.checkState())
        
    def save_puthButton_clicked(self):
        directorypath = filedialog.askdirectory()
        
        if str(directorypath) != "()":
            self.puth_save_label.setText(str(directorypath))
            self.save_puth_flag = True
        
    def ApplyButton_clicked(self):
        if self.puthList.count() != 0 and (self.save_puth_flag != False or self.mailBox.checkState() != False):
            if self.mailBox.checkState():
                if validate(email_address= self.mailEdit.text()):   
                    zip_arch = zipfile.ZipFile(self.__default_archive_name + self.__default_archive_extension, mode='w')
                    for item in range(self.puthList.count()):
                        input_path = Path(self.puthList.item(item).text())
                        file_name = input_path.stem
                        output_path = self.__default_save_puth + file_name + self.__default_img_extension
                        input_img = Image.open(input_path)
                        output_img = remove(input_img)
                        output_img.save(output_path)
                        zip_arch.write(output_path)
                        os.remove(output_path)
                    
                    
                    zip_arch.close()
                    os.remove(self.__default_archive_name + self.__default_archive_extension)
                    
                    message_mail = MIMEMultipart()
                    message_mail['From'] = self.__mail_address
                    message_mail['To'] = self.mailEdit.text()
                    now_date_time = datetime.datetime.now()
                    message_mail['Subject'] = "Архив с обрезаным фоном" + now_date_time.strftime("%d-%m-%Y %H:%M")
                
                    ctype, encoding = mimetypes.guess_type(self.__default_archive_name + self.__default_archive_extension)
                    maintype, subtype = ctype.split('/', 1)
                    with open(self.__default_archive_name + self.__default_archive_extension, 'rb') as fp:
                        file = MIMEBase(maintype, subtype)              
                        file.set_payload(fp.read())                     
                        fp.close()
                        encoders.encode_base64(file)
                    file.add_header('Content-Disposition', 'attachment', filename='carvebackground_arch_result') 
                    message_mail.attach(file)
                
                    server = smtplib.SMTP_SSL('smtp.server.ru', 465)        
                    server.starttls()                                      
                    server.set_debuglevel(True)                            
                    server.login(self.__mail_address, self.__mail_password)                       
                    server.send_message(message_mail)                                
                    server.quit()
                else:
                    message_warning = "Не корректная почта!"
                    msg = QMessageBox()
                    msg.setWindowTitle("Ошибка!")
                    msg.setText(message_warning)
                    msg.setIcon(QMessageBox.Warning)

                    msg.exec_()
            if self.save_puth_flag != False:
                for item in range(self.puthList.count()):
                    input_path = Path(self.puthList.item(item).text())
                    file_name = input_path.stem
                    output_path = f'{self.puth_save_label.text()}/{file_name}_out.png'
                    input_img = Image.open(input_path)
                    output_img = remove(input_img)
                    output_img.save(output_path)        
        else:
            message_warning = "Вы не выполнили пункт(ы):"
            if self.puthList.count() == 0: message_warning += "\n-Не выбрали файлы"
            if self.save_puth_flag == False and self.mailBox.checkState() == False: message_warning += "\n-Не выбрали способ сохранения(почта или локальная папка)"
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка!")
            msg.setText(message_warning)
            msg.setIcon(QMessageBox.Warning)

            msg.exec_()
