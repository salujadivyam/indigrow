import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Create the application
app = QApplication(sys.argv)

# Create a window
window = QWidget()
window.setWindowTitle("Hacknight")
window.setGeometry(210, 100, 1500, 1000)  # (x, y, width, height)
window.show()

# Run the application
sys.exit(app.exec_())
