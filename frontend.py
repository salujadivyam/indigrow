import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap
from PyQt5.QtCore import Qt

class FirstPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Indigrow")
        self.setGeometry(210, 100, 1500, 1000)

        # custom fonts
        font_path1 = "C:/Users/athar/Downloads/hackknights/sources/KronaOne-Regular.ttf"
        font_id1 = QFontDatabase.addApplicationFont(font_path1)
        font_family1 = QFontDatabase.applicationFontFamilies(font_id1)[0] if font_id1 != -1 else "Arial"

        font_path2 = "C:/Users/athar/Downloads/hackknights/sources/MartianMono-VariableFont_wdth,wght.ttf"
        font_id2 = QFontDatabase.addApplicationFont(font_path2)
        font_family2 = QFontDatabase.applicationFontFamilies(font_id2)[0] if font_id2 != -1 else "Arial"

        # "Indigrow" Label
        self.label1 = QLabel("indigrow", self)
        self.label1.setFont(QFont(font_family1, 80))
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setStyleSheet("color: black;")
        self.label1.adjustSize()

        # Image beside "indigrow"
        self.image_label = QLabel(self)
        pixmap = QPixmap("C:/Users/athar/Downloads/hackknights/sources/Vector.svg")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.image_label.resize(150, 150)

        # Tagline below "indigrow"
        self.label2 = QLabel("solving farmer’s problems", self)
        self.label2.setFont(QFont(font_family2, 30))
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet("color: black;")
        self.label2.adjustSize()

        # Button to go to the next page
        self.next_button = QPushButton("Dashboard", self)
        self.next_button.setStyleSheet("background-color: black; color: white; padding: 20px; border-radius: 20px;")
        self.next_button.setFont(QFont(font_family2, 15, QFont.Bold))
        self.next_button.clicked.connect(self.open_second_page)
        self.next_button.adjustSize()

        self.resizeEvent(None)  

    def resizeEvent(self, event):
        label1_x = (self.width() - self.label1.width()) // 2 - 80
        label1_y = (self.height() - self.label1.height()) // 2
        self.label1.move(label1_x, label1_y)

        spacing = 20
        image_label_x = label1_x + self.label1.width() + spacing
        image_label_y = label1_y + (self.label1.height() - self.image_label.height()) // 2
        self.image_label.move(image_label_x, image_label_y)

        label2_x = (self.width() - self.label2.width()) // 2
        label2_y = label1_y + self.label1.height() + spacing
        self.label2.move(label2_x, label2_y)
        button_margin = 30
        self.next_button.move(self.width() - self.next_button.width() - button_margin,self.height() - self.next_button.height() - button_margin)

    def open_second_page(self):
        self.second_page = SecondPage()
        self.second_page.show()
        self.close()

class SecondPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second Page")
        self.setGeometry(210, 100, 1500, 1000)
        self.setStyleSheet("background-color: white;")

        font_path1 = "C:/Users/athar/Downloads/hackknights/sources/KronaOne-Regular.ttf"
        font_id1 = QFontDatabase.addApplicationFont(font_path1)
        font_family1 = QFontDatabase.applicationFontFamilies(font_id1)[0] if font_id1 != -1 else "Arial"
        font_path2 = "C:/Users/athar/Downloads/hackknights/sources/MartianMono-VariableFont_wdth,wght.ttf"
        font_id2 = QFontDatabase.addApplicationFont(font_path2)
        font_family2 = QFontDatabase.applicationFontFamilies(font_id2)[0] if font_id2 != -1 else "Arial"

        label1 = QLabel("indigrow", self)
        label1.setFont(QFont(font_family1, 25))
        label1.move(30,20)
        label1.setStyleSheet("color: black;")
        label1.adjustSize()

        image_label = QLabel(self)
        pixmap = QPixmap("C:/Users/athar/Downloads/hackknights/sources/Vector.svg")
        image_label.setPixmap(pixmap)
        image_label.setScaledContents(True)
        image_label.resize(50, 50)
        image_label.move(320, 20)
        
        self.back_button = QPushButton("Back", self)
        self.back_button.setStyleSheet("background-color: black; color: white; padding: 20px; border-radius: 20px;")
        self.back_button.setFont(QFont(font_family2, 15, QFont.Bold))
        self.back_button.clicked.connect(self.go_back)
        self.back_button.adjustSize()

        self.resizeEvent(None)

    def resizeEvent(self, event):
        button_margin = 30
        self.back_button.move(self.width() - self.back_button.width() - button_margin,self.height() - self.back_button.height() - button_margin)

    def go_back(self):
        self.first_page = FirstPage()
        self.first_page.show()
        self.close()

app = QApplication(sys.argv)
window = FirstPage()
window.show()
sys.exit(app.exec_())
