import sys
import pyttsx3
from gtts import gTTS
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QLabel, QFileDialog
from PyQt5.QtGui import QIcon
from mydesign import *

class TextToSpeechApp(QMainWindow):
    def __init__(self):
        super().__init__()




        self.setWindowIcon(QIcon('icon.png'))

        self.setWindowTitle("Text to Speech")
        self.setGeometry(100, 100, 500, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        self.speak_button = QPushButton("Озвучить")
        self.speak_button.clicked.connect(self.speak_text)
        self.layout.addWidget(self.speak_button)

        self.save_button = QPushButton("Сохранить в MP3")
        self.save_button.clicked.connect(self.save_mp3)
        self.layout.addWidget(self.save_button)

        self.save_button = QPushButton("Сохранить в .MP3 как")
        self.save_button.clicked.connect(self.save_to_mp3)
        self.layout.addWidget(self.save_button)


        self.created_by_label = QLabel("Created by quthery")
        self.statusbar = self.statusBar()
        self.statusbar.addPermanentWidget(self.created_by_label)

        self.central_widget.setLayout(self.layout)

        self.engine = pyttsx3.init()
        self.output_file = "autosave.mp3"

    def speak_text(self):
        self.statusbar.showMessage("Озвучено!")
        text = self.text_edit.toPlainText()
        self.engine.say(text)
        self.engine.runAndWait()
        

    def save_mp3(self):
            text = self.text_edit.toPlainText()
            tts = gTTS(text)
            tts.save(self.output_file)
            self.statusbar.showMessage("озвучка успешно сохранена!")

    def save_to_mp3(self):
        text = self.text_edit.toPlainText()
        tts = gTTS(text)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить в MP3", self.output_file, "MP3 Files (*.mp3);;All Files (*)", options=options)

        if file_name:
            tts.save(file_name)
            self.statusbar.showMessage("озвучка успешно сохранена как mp3!")

def main():
    app = QApplication(sys.argv)
    window = TextToSpeechApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
