# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGroupBox, QLabel, QPlainTextEdit, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1049, 524)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(False)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-210, 0, 1321, 181))
        self.label.setPixmap(QPixmap(u"48975688-cf92-4b36-9fe1-fbe0a492a74b.png"))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(70, 230, 661, 281))
        font = QFont()
        font.setFamilies([u"RobotoMono Nerd Font Propo Md [GOOG]"])
        font.setPointSize(18)
        self.groupBox.setFont(font)
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(220, 40, 258, 211))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TextEdit = QPlainTextEdit(self.verticalLayoutWidget)
        self.TextEdit.setObjectName(u"TextEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TextEdit.sizePolicy().hasHeightForWidth())
        self.TextEdit.setSizePolicy(sizePolicy1)
        self.TextEdit.setMaximumSize(QSize(16777215, 35))
        font1 = QFont()
        font1.setFamilies([u"RobotoMono Nerd Font Propo Md [GOOG]"])
        font1.setPointSize(15)
        self.TextEdit.setFont(font1)

        self.verticalLayout.addWidget(self.TextEdit)

        self.plainTextEdit_2 = QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy2)
        self.plainTextEdit_2.setMaximumSize(QSize(16777215, 35))
        self.plainTextEdit_2.setFont(font1)

        self.verticalLayout.addWidget(self.plainTextEdit_2)

        self.plainTextEdit_3 = QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        sizePolicy2.setHeightForWidth(self.plainTextEdit_3.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_3.setSizePolicy(sizePolicy2)
        self.plainTextEdit_3.setMaximumSize(QSize(16777215, 35))
        self.plainTextEdit_3.setFont(font1)

        self.verticalLayout.addWidget(self.plainTextEdit_3)

        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 50, 204, 191))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777198, 16777215))

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.buttonBox = QDialogButtonBox(self.groupBox)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(480, 250, 171, 26))
        font2 = QFont()
        font2.setFamilies([u"RobotoMono Nerd Font Propo Md [GOOG]"])
        font2.setPointSize(12)
        self.buttonBox.setFont(font2)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(750, 350, 261, 61))
        font3 = QFont()
        font3.setFamilies([u"RobotoMono Nerd Font Propo Md [GOOG]"])
        font3.setPointSize(17)
        font3.setBold(False)
        font3.setKerning(False)
        self.textBrowser.setFont(font3)
        self.textBrowser.setAutoFillBackground(False)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Database Credentials", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Hostname / Url", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Password", None))
    # retranslateUi

