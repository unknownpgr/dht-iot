import requests
import xml.etree.ElementTree as ET
import time

key = '5766457145756e6b3835484a417a52'
link_id = '1220003800'
url = f"http://openapi.seoul.go.kr:8088/{key}/xml/TrafficInfo/1/5/{link_id}"
while True:
    data = requests.get(url).text
    root = ET.fromstring(data)
    code = root[0][0].text
    if code != 'INFO-100':
        print(f'에러 발생 :', root[0][1].text)
    else:
        print(root[2][1].text)
    time.sleep(2)
