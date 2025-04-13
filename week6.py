import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, 
                             QLabel, QSlider, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class LabelCustomizerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        

        self.student_name = "Andika Dhanan Jaya"  
        self.student_nim = "F1D022111"   
        
        self.setWindowTitle("Week 6 Assignment - Label Customizer")
        self.setGeometry(100, 100, 500, 400)
        

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        

        info_label = QLabel(f"{self.student_name} - NIM: {self.student_nim}")
        info_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(info_label)
        

        self.display_label = QLabel(self.student_nim)
        self.display_label.setAlignment(Qt.AlignCenter)
        self.display_label.setStyleSheet("border: 1px solid black;")
        layout.addWidget(self.display_label, 1)
        

        font_size_layout = QHBoxLayout()
        font_size_label = QLabel("Font Size")
        self.font_size_slider = QSlider(Qt.Horizontal)
        self.font_size_slider.setRange(20, 60)
        self.font_size_slider.setValue(30)
        self.font_size_slider.valueChanged.connect(self.update_label)
        
        font_size_layout.addWidget(font_size_label)
        font_size_layout.addWidget(self.font_size_slider)
        layout.addLayout(font_size_layout)
 
        font_color_layout = QHBoxLayout()
        font_color_label = QLabel("Font Color")
        self.font_color_slider = QSlider(Qt.Horizontal)
        self.font_color_slider.setRange(0, 255)
        self.font_color_slider.setValue(0)
        self.font_color_slider.valueChanged.connect(self.update_label)
        
        font_color_layout.addWidget(font_color_label)
        font_color_layout.addWidget(self.font_color_slider)
        layout.addLayout(font_color_layout)
        

        bg_color_layout = QHBoxLayout()
        bg_color_label = QLabel("Background Color")
        self.bg_color_slider = QSlider(Qt.Horizontal)
        self.bg_color_slider.setRange(0, 255)
        self.bg_color_slider.setValue(255)
        self.bg_color_slider.valueChanged.connect(self.update_label)
        
        bg_color_layout.addWidget(bg_color_label)
        bg_color_layout.addWidget(self.bg_color_slider)
        layout.addLayout(bg_color_layout)
        

        self.update_label()
    
    def update_label(self):
 

        font_size = self.font_size_slider.value()
        font_color = self.font_color_slider.value()
        bg_color = self.bg_color_slider.value()
        

        self.display_label.setStyleSheet(f"""
            font-size: {font_size}pt;
            color: rgb({font_color}, {font_color}, {font_color});
            background-color: rgb({bg_color}, {bg_color}, {bg_color});
            border: 1px solid black;
        """)
        

        if abs(font_color - bg_color) < 50:
  
            contrast_color = 0 if bg_color > 127 else 255
            self.display_label.setStyleSheet(f"""
                font-size: {font_size}pt;
                color: rgb({contrast_color}, {contrast_color}, {contrast_color});
                background-color: rgb({bg_color}, {bg_color}, {bg_color});
                border: 1px solid black;
            """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LabelCustomizerApp()
    window.show()
    sys.exit(app.exec_())