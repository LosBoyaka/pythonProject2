import sys
import os
from PIL.ImageFilter import *
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image
from PyQt5.QtWidgets import *
from PIL import ImageFilter
from PIL import ImageEnhance

def main_project():

    def pil2pixmap(im):
        if im.mode == "RGB":
            r, g, b = im.split()
            im = Image.merge("RGB", (b, g, r))
        elif  im.mode == "RGBA":
            r, g, b, a = im.split()
            im = Image.merge("RGBA", (b, g, r, a))
        elif im.mode == "L":
            im = im.convert("RGBA")
        im2 = im.convert("RGBA")
        data = im2.tobytes("raw", "RGBA")
        qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
        pixmap = QPixmap.fromImage(qim)
        return pixmap

    window = QDialog()
    window.resize(1280, 720)
    window.setStyleSheet("""
    
    
            QDialog
            {
            background-color: #969696;
    
    
    
    
            }
            QPushButton
            {
                background-color: #ffffff;
                border-color: grey;
                color: black;
                border-style: groove;
                border-width: 5px;
                border-radius: 7px;
                font-family: "Times New Roman", Times, serif;
                min-width: 6em;
                padding: 6px;
                font-size: 15px;
            }            
                QPushButton:hover {
                    background-color: #3edb00 ;
                    border-color: green;
                    color: black;
                }
            QListWidget
            {
                font-size: 20px;
                font-style: oblique;
                color: black;
                font-family: "Times New Roman", Times, serif;
                background-color: #ffffff;
                border-style: groove;
                border-width: 5px;
                border-color: grey;
                border-radius: 7px;
            }
            QLabel
            {
                background-color: #ffffff;
                font-size: 15px;
                font-style: oblique;
                font-family: "Times New Roman", Times, serif;
    
            }
        """)

    data_btn = QPushButton("Папка")
    left_btn = QPushButton("Вліво")
    right_btn = QPushButton("Вправо")
    dzerela_btn = QPushButton("Джерела")
    Rizkist_btn = QPushButton("Різкість")
    mirror_btn = QPushButton("Віддзеркалення")
    saturation_btn = QPushButton("Насиченність")
    Smooth_btn = QPushButton("Згладити")
    Brightness_btn = QPushButton("Яскравість")
    Blur_btn = QPushButton("Блюр")
    Counture_btn = QPushButton("Контури")
    Theme_btn1 = QPushButton("Світла тема")
    Theme_btn2 = QPushButton("Темна тема")
    C_B_btn = QPushButton("Ч/Б")
    list_png = QListWidget()
    pic = QLabel('Picture')
    main_line = QHBoxLayout()
    v1 = QVBoxLayout()
    v2 = QVBoxLayout()
    h1 = QHBoxLayout()
    h2 = QHBoxLayout()
    h3 = QHBoxLayout()

    main_line.addLayout(v1)
    v1.addWidget(data_btn)
    v1.addWidget(list_png)
    v1.addWidget(Theme_btn1)
    v1.addWidget(Theme_btn2)
    v1.addLayout(h1)
    main_line.addLayout(v2)
    v2.addWidget(pic)
    v2.addLayout(h2)
    h2.addWidget(left_btn)
    h2.addWidget(right_btn)
    h2.addWidget(mirror_btn)
    h2.addWidget(Brightness_btn)
    h2.addWidget(dzerela_btn)
    v2.addLayout(h3)
    h3.addWidget(Rizkist_btn)
    h3.addWidget(Smooth_btn)
    h3.addWidget(Counture_btn)
    h3.addWidget(Blur_btn)
    h3.addWidget(saturation_btn)
    h3.addWidget(C_B_btn)



    class ImageProcessor:
        def __init__(self):
            self.folder = None
            self.image = None
            self.filename = None

        def picture_load(self):
            image_path = os.path.join(self.folder, self.filename)
            self.image = Image.open(image_path)

        def image_show(self):
            pixel = pil2pixmap(self.image)
            pic.setPixmap(pixel)


        def mirror_image(self):
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.image_show()

        def saturation_image(self):
            num2, ok = QInputDialog.getText(window, "Значення", "Надайте значення")
            self.image = ImageEnhance.Color(self.image).enhance(float(num2))
            self.image_show()

        def smooth_image(self):
            self.image = self.image.filter(ImageFilter.SMOOTH)
            self.image_show()

        def Black_and_white_image(self):
            self.image = self.image.convert("L")
            self.image_show()

        def Rizkisty_image(self):
            self.image = self.image.filter(ImageFilter.SHARPEN)
            self.image_show()

        def Brightness_image(self):
            num1, ok = QInputDialog.getText(window, "Значення", "Надайте значення")
            self.image = ImageEnhance.Brightness(self.image).enhance(float(num1))
            self.image_show()

        def BLUR_image(self):
            self.image = self.image.filter(ImageFilter.BLUR)
            self.image_show()
        def Counture_image(self):
            self.image = self.image.filter(ImageFilter.CONTOUR)
            self.image_show()

        def right_locate_fun(self):
            self.image = self.image.transpose(Image.ROTATE_90)
            self.image_show()
        def left_locate_fun(self):
            self.image = self.image.transpose(Image.ROTATE_270)
            self.image_show()
    image_processor = ImageProcessor()


    def Switch_Theme_1():
        window.setStyleSheet("""
    
    
                QDialog
                {
                background-color: #969696;
    
    
    
    
                }
                QPushButton
                {
                    background-color: #ffffff;
                    border-color: grey;
                    color: black;
                    border-style: groove;
                    border-width: 5px;
                    border-radius: 7px;
                    font-family: "Times New Roman", Times, serif;
                    min-width: 6em;
                    padding: 6px;
                    font-size: 15px;
                }            
                    QPushButton:hover {
                        background-color: #3edb00 ;
                        border-color: green;
                        color: black;
                    }
                QListWidget
                {
                    font-size: 20px;
                    font-style: oblique;
                    color: black;
                    font-family: "Times New Roman", Times, serif;
                    background-color: #ffffff;
                    border-style: groove;
                    border-width: 5px;
                    border-color: grey;
                    border-radius: 7px;
                }
                QLabel
                {
                    background-color: #ffffff;
                    font-size: 15px;
                    font-style: oblique;
                    font-family: "Times New Roman", Times, serif;
    
                }
            """)


    def Switch_Theme_2():
        window.setStyleSheet("""
    
    
                QDialog
                {
                background-color: #232324;
    
    
    
    
                }
                QPushButton
                {
                    background-color: #242426;
                    border-color: black;
                    color: white;
                    border-style: groove;
                    border-width: 5px;
                    border-radius: 7px;
                    font-family: "Times New Roman", Times, serif;
                    min-width: 6em;
                    padding: 6px;
                    font-size: 15px;
                }            
                    QPushButton:hover {
                        background-color: #bfbfbf ;
                        border-color: gray;
                        color: black;
                    }
                QListWidget
                {
                    font-size: 20px;
                    font-style: oblique;
                    color: white;
                    font-family: "Times New Roman", Times, serif;
                    background-color: #212121;
                    border-style: groove;
                    border-width: 5px;
                    border-color: black;
                    border-radius: 7px;
                }
                QLabel
                {
                    background-color: #ffffff;
                    font-size: 15px;
                    font-style: oblique;
                    font-family: "Times New Roman", Times, serif;
    
                }
            """)

    def open_directory():
        folder = QFileDialog.getExistingDirectory()
        image_processor.folder = folder
        files = os.listdir(folder)
        for file in files:
            image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.jfif')
            if file.endswith(".png"):
                list_png.addItem(file)
            if file.endswith(".jpeg"):
                list_png.addItem(file)
            if file.endswith(".jpg"):
                list_png.addItem(file)
            if file.endswith(".gif"):
                list_png.addItem(file)
            if file.endswith(".bmp"):
                list_png.addItem(file)
            if file.endswith('.tiff'):
                list_png.addItem(file)
            if file.endswith('.jfif'):
                list_png.addItem(file)

    def show_chosen_image():
        image_processor.filename = list_png.currentItem().text()
        image_processor.picture_load()
        image_processor.image_show()
    def new_image():
        image_processor.filename = list_png.currentItem().text()
        image_processor.picture_load()
        image_processor.image_show()

    list_png.currentRowChanged.connect(show_chosen_image)





    data_btn.clicked.connect(open_directory)


    right_btn.clicked.connect(image_processor.right_locate_fun)
    left_btn.clicked.connect(image_processor.left_locate_fun)
    Theme_btn1.clicked.connect(Switch_Theme_1)
    Theme_btn2.clicked.connect(Switch_Theme_2)
    Counture_btn.clicked.connect(image_processor.Counture_image)
    Blur_btn.clicked.connect(image_processor.BLUR_image)
    Brightness_btn.clicked.connect(image_processor.Brightness_image)
    Rizkist_btn.clicked.connect(image_processor.Rizkisty_image)
    C_B_btn.clicked.connect(image_processor.Black_and_white_image)
    mirror_btn.clicked.connect(image_processor.mirror_image)
    saturation_btn.clicked.connect(image_processor.saturation_image)
    Smooth_btn.clicked.connect(image_processor.smooth_image)



    window.setLayout(main_line)
    window.show()
    window.exec()