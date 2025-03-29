import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

# Create the window
window = QWidget()
window.setWindowTitle("Hacknight")
window.setGeometry(210, 100, 1500, 1000)
window.setStyleSheet("QWidget {background-image: url('C:/Users/athar/Downloads/hackknights/sources/Aerial View of Agricultural Farmland.jpeg'); background-position: center; background-repeat: no-repeat; background-size: cover;}")

# Load custom fonts
font_path1 = "C:/Users/athar/Downloads/hackknights/sources/KronaOne-Regular.ttf"
font_id1 = QFontDatabase.addApplicationFont(font_path1)
if font_id1 == -1:
    print("Failed to load font")
font_family1 = QFontDatabase.applicationFontFamilies(font_id1)[0]

font_path2 = "C:/Users/athar/Downloads/hackknights/sources/MartianMono-VariableFont_wdth,wght.ttf"
font_id2 = QFontDatabase.addApplicationFont(font_path2)
if font_id2 == -1:
    print("Failed to load font")
font_family2 = QFontDatabase.applicationFontFamilies(font_id2)[0]

# "Indigrow" Label
label1 = QLabel("indigrow", window)
label1.setFont(QFont(font_family1, 80))  
label1.setAlignment(Qt.AlignCenter)
label1.setAttribute(Qt.WA_TranslucentBackground)
label1.setStyleSheet("color: white;")  
label1.adjustSize()
# Position "indigrow" label
label1_x = (window.width() - label1.width()) // 2 - 80
label1_y = (window.height() - label1.height()) // 2
label1.move(label1_x, label1_y)

# Image beside "indigrow"
image_label = QLabel(window)
pixmap = QPixmap("C://Users//athar//Downloads//hackknights//sources//Vector.svg")
image_label.setAttribute(Qt.WA_TranslucentBackground)
image_label.setPixmap(pixmap)
image_label.setScaledContents(True)
image_label.resize(150, 150)  
spacing = 20  
image_label_x = label1_x + label1.width() + spacing
image_label_y = label1_y + (label1.height() - image_label.height()) // 2  
image_label.move(image_label_x, image_label_y)

# Tagline below "indigrow"
label2 = QLabel("solving farmer’s problems", window)
label2.setFont(QFont(font_family2, 30))  
label2.setAlignment(Qt.AlignCenter)
label2.setAttribute(Qt.WA_TranslucentBackground) 
label2.setStyleSheet("color: white;")  
label2.adjustSize()
# Position of tagline below "indigrow"
spacing = 20
label2_x = (window.width() - label2.width()) // 2
label2_y = label1_y + label1.height() + spacing
label2.move(label2_x, label2_y)

# Show the window
window.show()
sys.exit(app.exec_())