# This Python file uses the following encoding: utf-8
import sys
import asyncio
from surrealdb import Surreal
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import Qt


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ui_dialog import Ui_Dialog


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the pushButton clicked signal to the slot
        self.ui.pushButton.clicked.connect(self.display_text)

    def display_text(self):
        # Get the text from plainTextEdit
        input_text = self.ui.plainTextEdit.toPlainText()

        # Set the text to textBrowser
        self.ui.textBrowser.setPlainText(input_text)


class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Connect the accepted signal of Dialog Button Box to the slot
        self.ui.buttonBox.accepted.connect(self.open_main_window)

    async def connect_to_surrealdb(self, url):
        """Example of how to use the SurrealDB client."""
        try:
            async with Surreal(f"ws://{url}/rpc") as db:
                await db.signin({"user": "root", "pass": "root"})
            return True
        except Exception as e:
            print(f"Failed to connect: {e}")
            return False

    def open_main_window(self):
        # Get the text from textEdit
        url = self.ui.textEdit.toPlainText()
        loop = asyncio.get_event_loop()
        asyncio.set_event_loop(loop)
        try:
            connection_successful = asyncio.run(self.connect_to_surrealdb(url))
            if connection_successful:
                self.main_window = MainWindow()
                self.main_window.show()
            else:
                self.ui.textBrowser.setPlainText("Failed to connect")
        except Exception as e:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Dialog()
    widget.show()
    sys.exit(app.exec())
