# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1397, 974)
        self.actioncopyright = QAction(MainWindow)
        self.actioncopyright.setObjectName(u"actioncopyright")
        self.proxySettings = QAction(MainWindow)
        self.proxySettings.setObjectName(u"proxySettings")
        self.engineSettings = QAction(MainWindow)
        self.engineSettings.setObjectName(u"engineSettings")
        self.customEngineSettings = QAction(MainWindow)
        self.customEngineSettings.setObjectName(u"customEngineSettings")
        self.actionedit = QAction(MainWindow)
        self.actionedit.setObjectName(u"actionedit")
        self.actionEnglish = QAction(MainWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionChinese = QAction(MainWindow)
        self.actionChinese.setObjectName(u"actionChinese")
        self.actionJapanese = QAction(MainWindow)
        self.actionJapanese.setObjectName(u"actionJapanese")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.versionLabel = QLabel(self.centralwidget)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setMaximumSize(QSize(91, 16))

        self.gridLayout.addWidget(self.versionLabel, 5, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(600, 310))
        self.translateBtn = QPushButton(self.widget)
        self.translateBtn.setObjectName(u"translateBtn")
        self.translateBtn.setGeometry(QRect(260, 280, 75, 24))
        self.selectFilesBtn = QPushButton(self.widget)
        self.selectFilesBtn.setObjectName(u"selectFilesBtn")
        self.selectFilesBtn.setGeometry(QRect(490, 25, 81, 41))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 102, 61, 31))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 30, 31, 31))
        self.label.setWordWrap(True)
        self.selectFilesText = QTextEdit(self.widget)
        self.selectFilesText.setObjectName(u"selectFilesText")
        self.selectFilesText.setGeometry(QRect(80, 25, 411, 41))
        self.selectDirBtn = QPushButton(self.widget)
        self.selectDirBtn.setObjectName(u"selectDirBtn")
        self.selectDirBtn.setGeometry(QRect(490, 100, 81, 41))
        self.selectDirText = QTextEdit(self.widget)
        self.selectDirText.setObjectName(u"selectDirText")
        self.selectDirText.setGeometry(QRect(80, 100, 411, 41))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 0, 71, 20))
        font = QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 160, 41, 31))
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 205, 41, 31))
        self.targetComboBox = QComboBox(self.widget)
        self.targetComboBox.setObjectName(u"targetComboBox")
        self.targetComboBox.setGeometry(QRect(80, 165, 491, 22))
        self.sourceComboBox = QComboBox(self.widget)
        self.sourceComboBox.setObjectName(u"sourceComboBox")
        self.sourceComboBox.setGeometry(QRect(80, 210, 491, 22))
        self.multiTranslateCheckBox = QCheckBox(self.widget)
        self.multiTranslateCheckBox.setObjectName(u"multiTranslateCheckBox")
        self.multiTranslateCheckBox.setGeometry(QRect(0, 240, 561, 31))
        self.multiTranslateCheckBox.setTristate(False)
        self.backupCheckBox = QCheckBox(self.widget)
        self.backupCheckBox.setObjectName(u"backupCheckBox")
        self.backupCheckBox.setGeometry(QRect(0, 280, 231, 24))

        self.gridLayout.addWidget(self.widget, 0, 0, 2, 1)

        self.copyrightLabel = QLabel(self.centralwidget)
        self.copyrightLabel.setObjectName(u"copyrightLabel")
        self.copyrightLabel.setMaximumSize(QSize(240, 16))

        self.gridLayout.addWidget(self.copyrightLabel, 5, 2, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(600, 220))
        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(260, 0, 60, 20))
        self.label_11.setFont(font)
        self.selectFontText = QTextEdit(self.widget_3)
        self.selectFontText.setObjectName(u"selectFontText")
        self.selectFontText.setGeometry(QRect(80, 100, 411, 41))
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 105, 30, 31))
        self.selectFontBtn = QPushButton(self.widget_3)
        self.selectFontBtn.setObjectName(u"selectFontBtn")
        self.selectFontBtn.setGeometry(QRect(490, 100, 81, 41))
        self.replaceFontBtn = QPushButton(self.widget_3)
        self.replaceFontBtn.setObjectName(u"replaceFontBtn")
        self.replaceFontBtn.setGeometry(QRect(250, 150, 75, 24))
        self.openFontStyleBtn = QPushButton(self.widget_3)
        self.openFontStyleBtn.setObjectName(u"openFontStyleBtn")
        self.openFontStyleBtn.setGeometry(QRect(210, 190, 161, 24))
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 40, 61, 31))
        self.selectDirText_3 = QTextEdit(self.widget_3)
        self.selectDirText_3.setObjectName(u"selectDirText_3")
        self.selectDirText_3.setGeometry(QRect(80, 38, 411, 41))
        self.selectDirBtn_3 = QPushButton(self.widget_3)
        self.selectDirBtn_3.setObjectName(u"selectDirBtn_3")
        self.selectDirBtn_3.setGeometry(QRect(490, 38, 81, 41))

        self.gridLayout.addWidget(self.widget_3, 3, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(600, 340))
        self.selectFilesText_2 = QTextEdit(self.widget_2)
        self.selectFilesText_2.setObjectName(u"selectFilesText_2")
        self.selectFilesText_2.setGeometry(QRect(80, 40, 411, 41))
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 45, 31, 31))
        self.label_5.setWordWrap(True)
        self.selectFilesBtn_2 = QPushButton(self.widget_2)
        self.selectFilesBtn_2.setObjectName(u"selectFilesBtn_2")
        self.selectFilesBtn_2.setGeometry(QRect(490, 40, 81, 41))
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 10, 60, 20))
        self.label_6.setFont(font)
        self.selectDirBtn_2 = QPushButton(self.widget_2)
        self.selectDirBtn_2.setObjectName(u"selectDirBtn_2")
        self.selectDirBtn_2.setGeometry(QRect(490, 160, 81, 41))
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 165, 71, 31))
        self.selectDirText_2 = QTextEdit(self.widget_2)
        self.selectDirText_2.setObjectName(u"selectDirText_2")
        self.selectDirText_2.setGeometry(QRect(80, 160, 411, 41))
        self.extractBtn = QPushButton(self.widget_2)
        self.extractBtn.setObjectName(u"extractBtn")
        self.extractBtn.setGeometry(QRect(250, 310, 75, 24))
        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 235, 61, 31))
        self.tlNameText = QTextEdit(self.widget_2)
        self.tlNameText.setObjectName(u"tlNameText")
        self.tlNameText.setGeometry(QRect(80, 230, 491, 41))
        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 105, 81, 31))
        self.label_13.setWordWrap(True)
        self.selectDirsText = QTextEdit(self.widget_2)
        self.selectDirsText.setObjectName(u"selectDirsText")
        self.selectDirsText.setGeometry(QRect(80, 100, 411, 41))
        self.selectDirsBtn = QPushButton(self.widget_2)
        self.selectDirsBtn.setObjectName(u"selectDirsBtn")
        self.selectDirsBtn.setGeometry(QRect(490, 100, 81, 41))
        self.filterCheckBox = QCheckBox(self.widget_2)
        self.filterCheckBox.setObjectName(u"filterCheckBox")
        self.filterCheckBox.setGeometry(QRect(0, 280, 91, 20))
        self.label_14 = QLabel(self.widget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(100, 282, 131, 16))
        self.filterLengthLineEdit = QLineEdit(self.widget_2)
        self.filterLengthLineEdit.setObjectName(u"filterLengthLineEdit")
        self.filterLengthLineEdit.setGeometry(QRect(230, 280, 61, 20))
        self.emptyCheckBox = QCheckBox(self.widget_2)
        self.emptyCheckBox.setObjectName(u"emptyCheckBox")
        self.emptyCheckBox.setGeometry(QRect(310, 280, 271, 20))

        self.gridLayout.addWidget(self.widget_2, 2, 0, 1, 1)

        self.clearLogBtn = QPushButton(self.centralwidget)
        self.clearLogBtn.setObjectName(u"clearLogBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearLogBtn.sizePolicy().hasHeightForWidth())
        self.clearLogBtn.setSizePolicy(sizePolicy)
        self.clearLogBtn.setMaximumSize(QSize(65535, 24))

        self.gridLayout.addWidget(self.clearLogBtn, 4, 1, 1, 2)

        self.log_text = QTextEdit(self.centralwidget)
        self.log_text.setObjectName(u"log_text")
        self.log_text.setMinimumSize(QSize(100, 500))
        self.log_text.setMaximumSize(QSize(65535, 65535))
        self.log_text.setReadOnly(True)

        self.gridLayout.addWidget(self.log_text, 0, 1, 4, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1397, 22))
        self.aboutMenu = QMenu(self.menubar)
        self.aboutMenu.setObjectName(u"aboutMenu")
        self.proxyMenu = QMenu(self.menubar)
        self.proxyMenu.setObjectName(u"proxyMenu")
        self.translationEngineMenu = QMenu(self.menubar)
        self.translationEngineMenu.setObjectName(u"translationEngineMenu")
        self.editorMenu = QMenu(self.menubar)
        self.editorMenu.setObjectName(u"editorMenu")
        self.menulanguage = QMenu(self.menubar)
        self.menulanguage.setObjectName(u"menulanguage")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.aboutMenu.menuAction())
        self.menubar.addAction(self.proxyMenu.menuAction())
        self.menubar.addAction(self.translationEngineMenu.menuAction())
        self.menubar.addAction(self.editorMenu.menuAction())
        self.menubar.addAction(self.menulanguage.menuAction())
        self.aboutMenu.addAction(self.actioncopyright)
        self.proxyMenu.addAction(self.proxySettings)
        self.translationEngineMenu.addAction(self.engineSettings)
        self.translationEngineMenu.addAction(self.customEngineSettings)
        self.editorMenu.addAction(self.actionedit)
        self.menulanguage.addAction(self.actionEnglish)
        self.menulanguage.addAction(self.actionChinese)
        self.menulanguage.addAction(self.actionJapanese)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ren'py Translator", None))
        self.actioncopyright.setText(QCoreApplication.translate("MainWindow", u"copyright", None))
        self.proxySettings.setText(QCoreApplication.translate("MainWindow", u"proxy settings", None))
        self.engineSettings.setText(QCoreApplication.translate("MainWindow", u"engine settings", None))
        self.customEngineSettings.setText(QCoreApplication.translate("MainWindow", u"custom engine", None))
        self.actionedit.setText(QCoreApplication.translate("MainWindow", u"edit from rpy", None))
        self.actionEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.actionChinese.setText(QCoreApplication.translate("MainWindow", u"Chinese", None))
        self.actionJapanese.setText(QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"Version 1.8.7", None))
        self.translateBtn.setText(QCoreApplication.translate("MainWindow", u"translate", None))
        self.selectFilesBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"directory", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"file(s)", None))
#if QT_CONFIG(tooltip)
        self.selectFilesText.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.selectFilesText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input or choose or drag the file(s) you want to translate here. Examaple : F:\\GameName\\game\\tl\\language\\script.rpy", None))
        self.selectDirBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.selectDirText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input or choose or drag the directory you want translate here.  Example:F:\\GameName\\game\\tl\\language", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"translation", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"target", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"source", None))
        self.multiTranslateCheckBox.setText(QCoreApplication.translate("MainWindow", u"Multi-Translate (If disabled translation will continue after the previous file has been translated)", None))
        self.backupCheckBox.setText(QCoreApplication.translate("MainWindow", u"Generate Backup Files (xxx.rpy.bak)", None))
        self.copyrightLabel.setText(QCoreApplication.translate("MainWindow", u"\u00a92024 Last moment,All rights reserved.", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"font", None))
        self.selectFontText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input or choose or drag the font which supports the language after translation. Example : DejaVuSans.ttf (ren'py 's default font)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"font", None))
        self.selectFontBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.replaceFontBtn.setText(QCoreApplication.translate("MainWindow", u"replace font", None))
        self.openFontStyleBtn.setText(QCoreApplication.translate("MainWindow", u"open font style file", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"directory", None))
        self.selectDirText_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input or choose or drag the directory you want to replace font here.  Example:F:\\GameName\\game\\tl\\language", None))
        self.selectDirBtn_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.selectFilesText_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.selectFilesText_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input or choose or drag the file(s) you want to extract here.    Examaple : F:\\GameName\\game\\script.rpy", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"file(s)", None))
        self.selectFilesBtn_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"extraction", None))
        self.selectDirBtn_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"tl directory", None))
        self.selectDirText_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input or choose or drag the directory you want to translate here.  Example:F:\\GameName\\game\\tl\\language", None))
        self.extractBtn.setText(QCoreApplication.translate("MainWindow", u"extract", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"tl name", None))
        self.tlNameText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"only force needs in file(s)/directory(s) mode , for tl directory , fill nothing is acceptable. input the directory name under game\\tl  Example: japanese or chinese", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"directory(s)", None))
#if QT_CONFIG(tooltip)
        self.selectDirsText.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.selectDirsText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input or choose or drag the directory(s) you want to extract here.    Examaple : F:\\GameName\\game\\character", None))
        self.selectDirsBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.filterCheckBox.setText(QCoreApplication.translate("MainWindow", u"Enable filter for extract", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"filter length less than", None))
        self.emptyCheckBox.setText(QCoreApplication.translate("MainWindow", u"Generate empty strings instead of original", None))
        self.clearLogBtn.setText(QCoreApplication.translate("MainWindow", u"clear log", None))
        self.aboutMenu.setTitle(QCoreApplication.translate("MainWindow", u"about", None))
        self.proxyMenu.setTitle(QCoreApplication.translate("MainWindow", u"proxy", None))
        self.translationEngineMenu.setTitle(QCoreApplication.translate("MainWindow", u"translation engine", None))
        self.editorMenu.setTitle(QCoreApplication.translate("MainWindow", u"editor", None))
        self.menulanguage.setTitle(QCoreApplication.translate("MainWindow", u"language", None))
    # retranslateUi

