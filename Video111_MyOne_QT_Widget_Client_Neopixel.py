import sys
import socket
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.87', 12345)

def offButtonPressed():
    print("Off Button Pressed")
    color = "off"
    request_message = color
    client_socket.sendto(request_message.encode(), server_address)
    data, addr = client_socket.recvfrom(1024)
    print("Received Data: ", data.decode())

def redButtonPressed():
    print("Red Button Pressed")
    color = "red"
    request_message = color
    client_socket.sendto(request_message.encode(), server_address)
    data, addr = client_socket.recvfrom(1024)
    print("Received Data: ", data.decode())
    
def greenButtonPressed():
    print("Green Button Pressed")
    color = "green"
    request_message = color
    client_socket.sendto(request_message.encode(), server_address)
    data, addr = client_socket.recvfrom(1024)
    print("Received Data: ", data.decode())
    
def cyanButtonPressed():
    print("Cyan Button Pressed")
    color = "cyan"
    request_message = color
    client_socket.sendto(request_message.encode(), server_address)
    data, addr = client_socket.recvfrom(1024)
    print("Received Data: ", data.decode())
    
def magentaButtonPressed():
    print("Magenta Button Pressed")
    color = "magenta"
    request_message = color
    client_socket.sendto(request_message.encode(), server_address)
    data, addr = client_socket.recvfrom(1024)
    print("Received Data: ", data.decode())

def blueButtonPressed():
    print("Blue Button Pressed")
    color = "blue"
    request_message = color
    client_socket.sendto(request_message.encode(), server_address)
    data, addr = client_socket.recvfrom(1024)
    print("Received Data: ", data.decode())
    
def yellowButtonPressed():
    print("Yellow Button Pressed")
    color = "yellow"
    request_message = color
    client_socket.sendto(request_message.encode(), server_address)
    data, addr = client_socket.recvfrom(1024)
    print("Received Data: ", data.decode())

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyQt5")
window.setGeometry(100,100,700,300)

widgetBox = QVBoxLayout(window)
buttonBox = QHBoxLayout()

offButton = QPushButton("OFF")
offButton.setStyleSheet("backGround-color:orange; color:black;")
offButton.clicked.connect(offButtonPressed)
buttonBox.addWidget(offButton)

redButton = QPushButton("RED")
redButton.setStyleSheet("backGround-color:red; color:white;")
redButton.clicked.connect(redButtonPressed)
buttonBox.addWidget(redButton)

cyanButton = QPushButton("CYAN")
cyanButton.setStyleSheet("backGround-color:cyan; color:black;")
cyanButton.clicked.connect(cyanButtonPressed)
buttonBox.addWidget(cyanButton)

greenButton = QPushButton("GREEN")
greenButton.setStyleSheet("backGround-color:green; color:white;")
greenButton.clicked.connect(greenButtonPressed)
buttonBox.addWidget(greenButton)

magentaButton = QPushButton("MAGENTA")
magentaButton.setStyleSheet("backGround-color:purple; color:white;")
magentaButton.clicked.connect(magentaButtonPressed)
buttonBox.addWidget(magentaButton)

blueButton = QPushButton("BLUE")
blueButton.setStyleSheet("backGround-color:blue; color:white;")
blueButton.clicked.connect(blueButtonPressed)
buttonBox.addWidget(blueButton)

yellowButton = QPushButton("YELLOW")
yellowButton.setStyleSheet("backGround-color:yellow; color:black;")
yellowButton.clicked.connect(yellowButtonPressed)
buttonBox.addWidget(yellowButton)

sliderLabel = QLabel("Hello, world!, Welcome to Tucson AZ")
sliderLabel.setAlignment(Qt.AlignCenter)
sliderLabel.setStyleSheet("font-size: 24px;padding 2px; ")

widgetBox.addWidget(sliderLabel)
widgetBox.addStretch()
widgetBox.addLayout(buttonBox)

window.setLayout(widgetBox)
window.show()
sys.exit(app.exec())
