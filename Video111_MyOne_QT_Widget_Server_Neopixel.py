import network
import usocket as socket
import neopixel
import secrets
import time

pixPin = 0
pixSize = 8
pix = neopixel.NeoPixel(machine.Pin(0),8)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID,secrets.PASSWORD)

while not wlan.isconnected():
    time.sleep(1)
print("Connection Completed")
print('WiFi connected')
print(wlan.ifconfig())

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((wlan.ifconfig()[0], 12345))
print("Server is Up and Listening")
print(wlan.ifconfig()[0])

while True:
    print('Waiting for a request from the client...')
    color, client_address = server_socket.recvfrom(1024)
    color=color.decode()
    print("Client Request:",color)
    print("FROM CLIENT",client_address)
    
           
    if (color=="red"):
        for i in range(0,1,1):   
            red = (15,0,0)
            pix[i] = red
            pix.write()
    if (color=="cyan"):
        for i in range(1,2,1):
            cyan = (0,15,15)
            pix[i] = cyan
            pix.write()
    if (color=="green"):
        for i in range(2,3,1):
            green = (0,15,0)
            pix[i] = green
            pix.write()
    if (color=="magenta"):
        for i in range(3,4,1):
            magenta = (15,0,15)
            pix[i] = magenta
            pix.write()
    if (color=="blue"):
        for i in range(4,5,1):
            blue = (0,0,15)
            pix[i] = blue
            pix.write() 
    if (color=="yellow"):
        for i in range(5,6,1):
            yellow = (15,13,0)
            pix[i] = yellow
            pix.write()
    if (color=="off"):
        off = (0,0,0)
        pix.fill(off)
        pix.write()
    
    data="LED "+color+" executed"
    server_socket.sendto(data.encode(), client_address)
    print(f'Sent data to {client_address}')
    time.sleep(1)