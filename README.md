# IoT Data Concatenator

This platform gathers humidity / temperature data with Arduino Yun and traffic data from Seoul City Open API.
Then, combine this data into one CSV file.

To use this script, the Python script and Arduino sketch script should be uploaded on Arduino Yun and be executed.
Python script can be executed via SSH.

Also, HOST in python script for PC should be changed to proper IP address.

## Steps

1. Connect Arduino Yun and PC to same WIFI network. It is recommended to use PC as hotspot AP and connect Arduino to that.
1. Update required files on Arduino Yun. Sketch file can be uploaded via Sketch IDE and Python script can be uploaded via SCP.
1. Execute Sketch file and python file on Arduino. If you uploaded Sketch file properly, It will be executed automatically, and python file should be executed manually via SSH. (You can set it to be executed automatically when Linux is booted, if you want.)
1. Execute Python script for PC.

Then it will automatically connect to Arduino and get humidity, temperature, traffic data from Arduino and Open API, and generate CSV file containing them with timestamp.

## Notice

- 노드 링크에 `표준링크`와 `서울특별시 서비스링크`  두 가지가 있다. 이 프로그램에서는 `서울특별시 서비스링크`를 입력해야만 한다.
- `docs/references`에 변환할 수 있는 엑셀 표가 있다.