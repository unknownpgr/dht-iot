import requests
import xml.etree.ElementTree as ET
import time
import socket
import csv
import datetime

HOST = '192.168.137.47'
PORT = 8080
key = '5766457145756e6b3835484a417a52'
link_id = '1220003800'
url = f"http://openapi.seoul.go.kr:8088/{key}/xml/TrafficInfo/1/5/{link_id}"

with open('output.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['Timestamp', 'Humidity', 'Temperature', 'Traffic'])
    while True:
        print('-----------------------')
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                data_arduino = str(s.recv(1024), encoding='utf-8')
                print(data_arduino)
                data_humidity, data_temperature = data_arduino.split('/')
                print('Arduino Data :', data_arduino)
        except (ConnectionRefusedError, ConnectionResetError):
            print('Could not connect to Arduino. Try again after 2 seconds.')
            time.sleep(2)
            continue

        data = requests.get(url).text
        root = ET.fromstring(data)
        code = root[1][0].text
        if code != 'INFO-000':
            print(f'Could not get data with OpenAPI. :', root[1][1].text)
            print("Try again after 2 seconds.")
        else:
            data_traffic = root[2][1].text
            print('OpenAPI Data :', data_traffic)
        csv_writer.writerow(
            [datetime.datetime.now(), data_humidity, data_temperature, data_traffic])
        f.flush()
        time.sleep(2)
