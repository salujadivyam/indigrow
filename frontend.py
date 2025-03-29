import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap
from PyQt5.QtCore import Qt

class FirstPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Indigrow")
        self.setGeometry(210, 100, 1500, 1000)

        # Custom fonts
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

        # Image beside "Indigrow"
        self.image_label = QLabel(self)
        pixmap = QPixmap("C:/Users/athar/Downloads/hackknights/sources/Vector.svg")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.image_label.resize(150, 150)

        # Tagline below "Indigrow"
        self.label2 = QLabel("solving farmer’s problems", self)
        self.label2.setFont(QFont(font_family2, 30))
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet("color: black;")
        self.label2.adjustSize()

        # Button to open SecondPage in a new window
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
        self.next_button.move(self.width() - self.next_button.width() - button_margin, self.height() - self.next_button.height() - button_margin)

    def open_second_page(self):
        """Opens SecondPage in a separate window without closing FirstPage"""
        self.second_page = SecondPage()
        self.second_page.show()

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

        # Page title label
        self.label1 = QLabel("indigrow", self)
        self.label1.setFont(QFont(font_family1, 25))
        self.label1.move(30, 20)
        self.label1.setStyleSheet("color: black;")
        self.label1.adjustSize()

        # Image beside title
        self.image_label = QLabel(self)
        pixmap = QPixmap("C:/Users/athar/Downloads/hackknights/sources/Vector.svg")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.image_label.resize(50, 50)
        self.image_label.move(320, 20)

        # **Input Fields**
        self.text_location = QLineEdit(self)
        self.text_location.setPlaceholderText("Enter Location")
        self.text_location.setFont(QFont(font_family2, 12))
        self.text_location.setStyleSheet("padding: 10px; border: 1px solid grey; border-radius: 15px;")
        self.text_location.adjustSize()
        self.text_location.setGeometry(30, 100, 400, 50)

        self.text_soil = QLineEdit(self)
        self.text_soil.setPlaceholderText("Enter Soil Type")
        self.text_soil.setFont(QFont(font_family2, 12))
        self.text_soil.adjustSize()
        self.text_soil.setStyleSheet("padding: 10px; border: 1px solid grey; border-radius: 15px;")
        self.text_soil.setGeometry(450, 100, 400, 50)

        self.text_crop = QLineEdit(self)
        self.text_crop.setPlaceholderText("Enter Crop Type")
        self.text_crop.adjustSize()
        self.text_crop.setFont(QFont(font_family2, 12))
        self.text_crop.setStyleSheet("padding: 10px; border: 1px solid grey; border-radius: 15px;")
        self.text_crop.setGeometry(870, 100, 400, 50)

        # **Buttons**
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setFont(QFont(font_family2, 12, QFont.Bold))
        self.submit_button.setStyleSheet("background-color: black; color: white; padding: 10px; border-radius: 10px;")
        self.submit_button.setGeometry(30, 170, 150, 50)
        self.submit_button.clicked.connect(self.process_input)

        self.close_button = QPushButton("Close", self)
        self.close_button.setFont(QFont(font_family2, 12, QFont.Bold))
        self.close_button.setStyleSheet("background-color: black; color: white; padding: 10px; border-radius: 10px;")
        self.close_button.setGeometry(220, 170, 150, 50)
        self.close_button.clicked.connect(self.close)

    def process_input(self):
        location = self.text_location.text()
        soil = self.text_soil.text()
        crop = self.text_crop.text()
    
        user_data = [location, soil, crop]
        print(f"User Data: {user_data}")  # Modify this to store or process the data further

        # Show notification
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Data Submitted Successfully!")
        msg.setWindowTitle("Success")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_() # Modify this to store or process the data further

app = QApplication(sys.argv)
window = FirstPage()
window.show()
sys.exit(app.exec_())
