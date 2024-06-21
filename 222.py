import os
from PIL.ImageFilter import *
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image
from PyQt5.QtWidgets import *




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

app = QApplication([])
window = QWidget()
window.resize(800, 600)
app.setStyleSheet("""


        QWidget
        {
        background-color: #FFC55A;




        }
        QPushButton
        {
            background-color: #FC4100;
            border-color: brown;
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
                background-color: #3edb00 ;
                border-color: green;
                color: black;
            }
        QListWidget
        {
            font-size: 20px;
            font-style: oblique;
            color: white;
            font-family: "Times New Roman", Times, serif;
            background-color: #577B8D;
            border-style: groove;
            border-width: 5px;
            border-color: blue;
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
C_B_btn = QPushButton("Ч/Б")
list_png = QListWidget()
pic = QLabel('Picture')

main_line = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()

main_line.addLayout(v1)
v1.addWidget(data_btn)
v1.addWidget(list_png)
v1.addLayout(h1)
main_line.addLayout(v2)
v2.addWidget(pic)
v2.addLayout(h2)
h2.addWidget(left_btn)
h2.addWidget(right_btn)
h2.addWidget(dzerela_btn)
h2.addWidget(Rizkist_btn)
h2.addWidget(C_B_btn)



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

image_processor = ImageProcessor()


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


list_png.currentRowChanged.connect(show_chosen_image)





data_btn.clicked.connect(open_directory)



window.setLayout(main_line)
window.show()
app.exec()