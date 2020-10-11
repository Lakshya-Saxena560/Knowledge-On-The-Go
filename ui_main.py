import time
import socket

from PySide2.QtCore import QCoreApplication, QMetaObject, QSize, Qt, QUrl
from PySide2.QtGui import QFont
from PySide2.QtWidgets import *
import wikipedia
from PySide2.QtWebEngineWidgets import QWebEngineView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 600)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        MainWindow.setFont(QFont('Roboto', 10))
        MainWindow.setWindowTitle('Nel')

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(110, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                      "border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)

        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)

        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(110, 0))
        self.frame_left_menu.setMaximumSize(QSize(110, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)

        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)


        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "	background-color: rgb(35, 35, 35);\n"
                                      "	border: 0px solid;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "	background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.btn_page_1.setFont(QFont('Roboto', 10))
        self.verticalLayout_4.addWidget(self.btn_page_1)


        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "	background-color: rgb(35, 35, 35);\n"
                                      "	border: 0px solid;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "	background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.btn_page_2.setFont(QFont('Roboto', 10))
        self.verticalLayout_4.addWidget(self.btn_page_2)


        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "	background-color: rgb(35, 35, 35);\n"
                                      "	border: 0px solid;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "	background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.btn_page_3.setFont(QFont('Roboto', 10))
        self.verticalLayout_4.addWidget(self.btn_page_3)



        self.btn_page_4 = QPushButton(self.frame_top_menus)
        self.btn_page_4.setObjectName(u"btn_page_4")
        self.btn_page_4.setMinimumSize(QSize(0, 40))
        self.btn_page_4.setStyleSheet(u"QPushButton {\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "	background-color: rgb(35, 35, 35);\n"
                                      "	border: 0px solid;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "	background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.btn_page_4.setFont(QFont('Roboto', 10))
        self.verticalLayout_4.addWidget(self.btn_page_4)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.frame_left_menu)


        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")


        #DICTIONARY
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_1 = QLabel(self.page_1)
        self.label_1.setObjectName(u"label_1")

        self.label_1.setFixedHeight(30)
        self.label_1.setText('Dictionary (Be Patient)')
        self.label_1.setFont(QFont('Roboto', 15))
        self.label_1.setStyleSheet("color: #FFF;")
        self.label_1.setAlignment(Qt.AlignHCenter)

        self.dictionary = QWebEngineView()
        self.dictionary.setUrl(QUrl("http://www.dictionary.com"))

        self.verticalLayout_7.addWidget(self.label_1)
        self.verticalLayout_7.addWidget(self.dictionary)
        self.stackedWidget.addWidget(self.page_1)




        #WIKIPEDIA
        self.page_2 = QWidget()
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.label_2 = QLabel(self.page_2)
        self.label_2.setFont(QFont('Roboto', 15))
        self.label_2.setStyleSheet(u"color: #FFF;")
        self.label_2.setAlignment(Qt.AlignTop)

        self.wikipedia_query = QLineEdit()
        self.wikipedia_query.setPlaceholderText('Wikipedia: Type in the topic you wanna know about and press Enter: ')
        self.wikipedia_query.setFixedHeight(60)
        self.wikipedia_query.setFont(QFont('Roboto', 16))
        self.wikipedia_query.setStyleSheet(u"color: #FFF;")

        self.wikipedia_query.returnPressed.connect(lambda: on_enter_wikipedia())
        self.wikipedia_query.returnPressed.connect(lambda: clear_text_wikipedia())

        def clear_text_wikipedia():
            self.wikipedia_query.clear()

        self.verticalLayout_6.addWidget(self.wikipedia_query)
        self.verticalLayout_6.addWidget(self.label_2)
        self.stackedWidget.addWidget(self.page_1)

        def on_enter_wikipedia():
            user_query = self.wikipedia_query.text().lower()
            try:
                self.label_2.setText('Searching Wikipedia. Please Wait...')
                time.sleep(2)
                self.label_2.setText('')
                user_query = user_query.replace('wikipedia', '')
                result = wikipedia.summary(user_query, sentences=6)
                self.label_2.setText(f'\n\n{result}')
                self.label_2.setWordWrap(True)
            except Exception as e:
                self.label_2.setText(e)

        self.stackedWidget.addWidget(self.page_2)




        #HOST MESSAGING
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.host_label_1 = QLabel(self.page_3)
        self.host_label_1.setFixedHeight(30)
        self.host_label_1.setFont(QFont('Roboto', 15))
        self.host_label_1.setStyleSheet("color: #FFF;")
        self.host_label_1.setAlignment(Qt.AlignLeft)

        self.host_label_4 = QLabel(self.page_3)
        self.host_label_4.setFixedHeight(30)
        self.host_label_4.setFont(QFont('Roboto', 15))
        self.host_label_4.setStyleSheet("color: #FFF;")
        self.host_label_4.setAlignment(Qt.AlignLeft)

        self.host_label_5 = QLabel(self.page_3)
        self.host_label_5.setFixedHeight(30)
        self.host_label_5.setFont(QFont('Roboto', 15))
        self.host_label_5.setStyleSheet("color: #FFF;")
        self.host_label_5.setAlignment(Qt.AlignLeft)

        self.host_type = QLineEdit()
        self.host_type.setFixedHeight(40)
        self.host_type.setPlaceholderText('Type in your message and hit Enter: ')
        self.host_type.setFixedHeight(60)
        self.host_type.setFont(QFont('Roboto', 16))
        self.host_type.setStyleSheet(u"color: #FFF;")

        self.host_type.returnPressed.connect(lambda: on_enter_host())
        self.host_type.returnPressed.connect(lambda: clear_text_host())

        s_host = socket.socket()
        hostname = socket.gethostname()

        self.host_label_1.setText(f'Server will start on host: {hostname}\n Server bounded to host and port '
                                  f'successfully \n Waiting for incoming connections')
        port = 2020
        s_host.bind((hostname, port))

        s_host.listen(1)
        conn, addr = s_host.accept()

        self.host_label_4.setText(f'IP Address {addr} connected to the server')

        def on_enter_host():
            host = self.host_type.text()

            while True:
                message = host
                message = message.encode()
                conn.send(message)

                incoming_message = conn.recv(512)
                incoming_message = incoming_message.decode()
                self.host_label_5.setText(f'Client: {incoming_message}')


        def clear_text_host():
            self.host_type.clear()

        self.verticalLayout_8.addWidget(self.host_label_1)
        self.verticalLayout_8.addWidget(self.host_label_4)
        self.verticalLayout_8.addWidget(self.host_label_5)
        self.verticalLayout_8.addWidget(self.host_type)
        self.stackedWidget.addWidget(self.page_3)





        #CLIENT MESSAGING
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_9 = QVBoxLayout(self.page_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.client_label_1 = QLabel(self.page_3)
        self.client_label_1.setFixedHeight(30)
        self.client_label_1.setFont(QFont('Roboto', 15))
        self.client_label_1.setStyleSheet("color: #FFF;")
        self.client_label_1.setAlignment(Qt.AlignLeft)

        self.client_label_5 = QLabel(self.page_3)
        self.client_label_5.setFixedHeight(30)
        self.client_label_5.setFont(QFont('Roboto', 15))
        self.client_label_5.setStyleSheet("color: #FFF;")
        self.client_label_5.setAlignment(Qt.AlignLeft)

        self.client_type = QLineEdit()
        self.client_type.setFixedHeight(40)
        self.client_type.setPlaceholderText('First type in the server IP Address to which you wanna connect then Type in your message and hit Enter: ')
        self.client_type.setFixedHeight(60)
        self.client_type.setFont(QFont('Roboto', 16))
        self.client_type.setStyleSheet(u"color: #FFF;")

        self.client_type.returnPressed.connect(lambda: on_enter_client())
        self.client_type.returnPressed.connect(lambda: clear_text_client())

        def on_enter_client():
            client = self.host_type.text()
            s_client = socket.socket()
            host = client
            port = 2020


            if s_client.connect((host, port)):
                self.client_label_1.setText('Connection succesfully established')
            else:
                self.client_label_1.setText('Could not establish connection. Please try again or see if the server is'
                                            ' even working or not.')


            while True:
                incoming_message = s_client.recv(512)
                incoming_message = incoming_message.decode()
                self.client_label_5.setText(f'Host: {incoming_message}')

                message = client
                message = message.encode()
                s_client.send(message)

        def clear_text_client():
            self.client_type.clear()

        self.verticalLayout_9.addWidget(self.client_label_1)
        self.verticalLayout_9.addWidget(self.client_label_5)
        self.verticalLayout_9.addWidget(self.client_type)

        self.stackedWidget.addWidget(self.page_4)



        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.horizontalLayout_2.addWidget(self.frame_pages)

        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"Menu", None))

        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Dictionary", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Wikipedia", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Message-Host", None))
        self.btn_page_4.setText(QCoreApplication.translate("MainWindow", u"Message-Client", None))
    # retranslateUi
