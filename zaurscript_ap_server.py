# MicroPython HTTP AP server for ESP8266 to serve ZaurScript files from flash
# Save as zaurscript_ap_server.py and run on ESP8266 (MicroPython)

import network
import socket
import os
import time

AP_SSID = 'ZaurScript_AP'
AP_PASSWORD = ''  # Open network, or set a password if you want

# Start Access Point
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=AP_SSID, password=AP_PASSWORD)
print('AP started:', AP_SSID)
print('AP IP:', ap.ifconfig()[0])

# Ensure at least one .zs file exists in flash
if 'main.zs' not in os.listdir():
    with open('main.zs', 'w') as f:
        f.write('echo "Default main.zs from ESP8266 AP"\n')

# Simple HTTP server to serve .zs files
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('Listening on', addr)

while True:
    cl, addr = s.accept()
    print('Client connected from', addr)
    request = cl.recv(1024)
    request_str = request.decode('utf-8')
    print('Request:', request_str)

    # Parse HTTP GET for .zs file
    if request_str.startswith('GET'):
        path = '/'
        try:
            path = request_str.split(' ')[1]
        except:
            pass
        if path.startswith('/'):
            path = path[1:]
        if path == '':
            path = 'main.zs'
        if path.endswith('.zs') and path in os.listdir():
            with open(path, 'r') as f:
                content = f.read()
            cl.send('HTTP/1.0 200 OK\r\nContent-Type: text/plain\r\n\r\n')
            cl.send(content)
        else:
            cl.send('HTTP/1.0 404 Not Found\r\n\r\nFile not found')
    else:
        cl.send('HTTP/1.0 400 Bad Request\r\n\r\n')
    cl.close()
