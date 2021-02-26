import requests
import xml.etree.ElementTree as ET
import time
import socket
import csv
import datetime

# Constants
HOST = '192.168.137.47'
PORT = 8080
API_KEY = '5766457145756e6b3835484a417a52'
LINK_ID = '1220003800'

# OpenAPI url for traffic data
url = f"http://openapi.seoul.go.kr:8088/{API_KEY}/xml/TrafficInfo/1/5/{LINK_ID}"

print('URL :', url)

with open('output.csv', 'w', newline='') as f:
    # CSV file for data logging
    csv_writer = csv.writer(f)
    csv_writer.writerow(['Timestamp', 'Humidity', 'Temperature', 'Traffic'])

    # Start main process
    while True:
        print('-----------------------')

        # Get the data from the Arduino Yun
        try:
            # Try connecting to Arduino and get data
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                data_arduino = str(s.recv(1024), encoding='utf-8')
                # Split the data into humidity and temperature
                data_humidity, data_temperature = data_arduino.split('/')
                print('Arduino Data :', data_arduino)
        except (ConnectionRefusedError, ConnectionResetError):
            # If connection is not established, print error message and try again after 2 seconds.
            print('Could not connect to Arduino. Try again after 2 seconds.')
            time.sleep(2)
            continue

        # Get the traffic data from OpenAPI
        data = requests.get(url).text

        # Parse xml-type data with ElementTree library
        root = ET.fromstring(data)

        # Get response code
        code = root[1][0].text

        # If response contains errors, print it and retry.
        if code != 'INFO-000':
            print(f'Could not get data with OpenAPI. :', root[1][1].text)
            print("Try again after 2 seconds.")
            time.sleep(2)
            continue

        # Else, just parse data and get required value(traffic)
        data_traffic = root[2][1].text
        print('OpenAPI Data :', data_traffic)

        # Concatenate data and write it to csv file
        csv_writer.writerow(
            [datetime.datetime.now(), data_humidity, data_temperature, data_traffic])

        # Flush data
        f.flush()

        # Wait for 2 seconds
        time.sleep(2)
