# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'one_key_translate.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_OneKeyTranslateDialog(object):
    def setupUi(self, OneKeyTranslateDialog):
        if not OneKeyTranslateDialog.objectName():
            OneKeyTranslateDialog.setObjectName(u"OneKeyTranslateDialog")
        OneKeyTranslateDialog.resize(1039, 582)
        self.selectFileBtn = QPushButton(OneKeyTranslateDialog)
        self.selectFileBtn.setObjectName(u"selectFileBtn")
        self.selectFileBtn.setGeometry(QRect(520, 45, 81, 91))
        self.selectFileText = QTextEdit(OneKeyTranslateDialog)
        self.selectFileText.setObjectName(u"selectFileText")
        self.selectFileText.setGeometry(QRect(110, 45, 411, 91))
        self.tlNameText = QTextEdit(OneKeyTranslateDialog)
        self.tlNameText.setObjectName(u"tlNameText")
        self.tlNameText.setGeometry(QRect(110, 160, 491, 81))
        self.label_8 = QLabel(OneKeyTranslateDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 170, 71, 31))
        self.label_8.setWordWrap(True)
        self.label = QLabel(OneKeyTranslateDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 71, 61))
        self.label.setWordWrap(True)
        self.label_9 = QLabel(OneKeyTranslateDialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 265, 41, 31))
        self.changeTranslationEngineButton = QPushButton(OneKeyTranslateDialog)
        self.changeTranslationEngineButton.setObjectName(u"changeTranslationEngineButton")
        self.changeTranslationEngineButton.setGeometry(QRect(30, 340, 571, 24))
        self.targetComboBox = QComboBox(OneKeyTranslateDialog)
        self.targetComboBox.setObjectName(u"targetComboBox")
        self.targetComboBox.setGeometry(QRect(110, 270, 491, 22))
        self.sourceComboBox = QComboBox(OneKeyTranslateDialog)
        self.sourceComboBox.setObjectName(u"sourceComboBox")
        self.sourceComboBox.setGeometry(QRect(110, 305, 491, 22))
        self.label_10 = QLabel(OneKeyTranslateDialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 300, 41, 31))
        self.localGlossaryCheckBox = QCheckBox(OneKeyTranslateDialog)
        self.localGlossaryCheckBox.setObjectName(u"localGlossaryCheckBox")
        self.localGlossaryCheckBox.setGeometry(QRect(30, 390, 571, 20))
        self.selectFontBtn = QPushButton(OneKeyTranslateDialog)
        self.selectFontBtn.setObjectName(u"selectFontBtn")
        self.selectFontBtn.setGeometry(QRect(520, 470, 81, 91))
        self.label_4 = QLabel(OneKeyTranslateDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 500, 71, 31))
        self.label_4.setWordWrap(True)
        self.selectFontText = QTextEdit(OneKeyTranslateDialog)
        self.selectFontText.setObjectName(u"selectFontText")
        self.selectFontText.setGeometry(QRect(110, 470, 411, 91))
        self.unpackCheckBox = QCheckBox(OneKeyTranslateDialog)
        self.unpackCheckBox.setObjectName(u"unpackCheckBox")
        self.unpackCheckBox.setGeometry(QRect(620, 50, 411, 20))
        self.unpackCheckBox.setChecked(True)
        self.runtimeExtractionCheckBox = QCheckBox(OneKeyTranslateDialog)
        self.runtimeExtractionCheckBox.setObjectName(u"runtimeExtractionCheckBox")
        self.runtimeExtractionCheckBox.setGeometry(QRect(620, 110, 411, 20))
        self.runtimeExtractionCheckBox.setChecked(True)
        self.extractionCheckBox = QCheckBox(OneKeyTranslateDialog)
        self.extractionCheckBox.setObjectName(u"extractionCheckBox")
        self.extractionCheckBox.setGeometry(QRect(620, 170, 411, 20))
        self.extractionCheckBox.setChecked(True)
        self.replaceFontCheckBox = QCheckBox(OneKeyTranslateDialog)
        self.replaceFontCheckBox.setObjectName(u"replaceFontCheckBox")
        self.replaceFontCheckBox.setGeometry(QRect(620, 230, 411, 20))
        self.replaceFontCheckBox.setChecked(True)
        self.addEntranceCheckBox = QCheckBox(OneKeyTranslateDialog)
        self.addEntranceCheckBox.setObjectName(u"addEntranceCheckBox")
        self.addEntranceCheckBox.setGeometry(QRect(620, 290, 411, 20))
        self.addEntranceCheckBox.setChecked(True)
        self.translateCheckBox = QCheckBox(OneKeyTranslateDialog)
        self.translateCheckBox.setObjectName(u"translateCheckBox")
        self.translateCheckBox.setGeometry(QRect(620, 350, 411, 20))
        self.translateCheckBox.setChecked(True)
        self.filterCheckBox = QCheckBox(OneKeyTranslateDialog)
        self.filterCheckBox.setObjectName(u"filterCheckBox")
        self.filterCheckBox.setGeometry(QRect(30, 430, 261, 20))
        self.filterCheckBox.setChecked(True)
        self.filterLengthLineEdit = QLineEdit(OneKeyTranslateDialog)
        self.filterLengthLineEdit.setObjectName(u"filterLengthLineEdit")
        self.filterLengthLineEdit.setGeometry(QRect(500, 430, 101, 20))
        self.filterLengthLineEdit.setText(u"8")
        self.label_14 = QLabel(OneKeyTranslateDialog)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(290, 432, 201, 16))
        self.label_14.setAlignment(Qt.AlignCenter)
        self.startButton = QPushButton(OneKeyTranslateDialog)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(620, 390, 401, 171))

        self.retranslateUi(OneKeyTranslateDialog)

        QMetaObject.connectSlotsByName(OneKeyTranslateDialog)
    # setupUi

    def retranslateUi(self, OneKeyTranslateDialog):
        OneKeyTranslateDialog.setWindowTitle(QCoreApplication.translate("OneKeyTranslateDialog", u"One Key Translate", None))
        self.selectFileBtn.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"...", None))
#if QT_CONFIG(tooltip)
        self.selectFileText.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.selectFileText.setPlaceholderText(QCoreApplication.translate("OneKeyTranslateDialog", u"input or choose or drag the game you want to extract it's dialogues.Example:F:/DemoGame.exe", None))
        self.tlNameText.setPlaceholderText(QCoreApplication.translate("OneKeyTranslateDialog", u"Input the directory name under game\\tl  Example: 'japanese' or 'chinese'.If the folder already exists, the content will be appended to the original file", None))
        self.label_8.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"tl name", None))
        self.label.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"file", None))
        self.label_9.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"target", None))
        self.changeTranslationEngineButton.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"Change Translation Engine", None))
        self.label_10.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"source", None))
        self.localGlossaryCheckBox.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"Local Glossary (replace certain words with preset content)", None))
        self.selectFontBtn.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"...", None))
        self.label_4.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"font", None))
        self.selectFontText.setPlaceholderText(QCoreApplication.translate("OneKeyTranslateDialog", u"input or choose or drag the font which supports the language after translation. Example : DejaVuSans.ttf (ren'py 's default font)", None))
        self.unpackCheckBox.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"Unpack Game Package", None))
        self.runtimeExtractionCheckBox.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"Runtime Extraction", None))
        self.extractionCheckBox.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"Extraction", None))
        self.replaceFontCheckBox.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"Replace Font", None))
        self.addEntranceCheckBox.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"Add Change Langauge Entrance", None))
        self.translateCheckBox.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"Translate", None))
        self.filterCheckBox.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"Enable filter for extract", None))
        self.label_14.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"filter length less than", None))
        self.startButton.setText(QCoreApplication.translate("OneKeyTranslateDialog", u"Start", None))
    # retranslateUi

