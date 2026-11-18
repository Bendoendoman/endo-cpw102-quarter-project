import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
import PySide6.QtCore

tempApp = QApplication(sys.argv)
# Prints PySide6 version

print(PySide6.__version__)
tempWindow = QWidget()
tempWindow.show()

tempButton = QPushButton("HEY")

tempButton.show()

# Prints the Qt version used to compile PySide`6
if tempButton.pressed:
    print("Hey")
tempApp.exec()
