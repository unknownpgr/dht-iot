# IoT Data Concatenator

This platform gethers humidity / temperature data with Arduino Yun and traffic data from Seoul City OpenAPI.
Then, combine this data into one CSV file.

To use this script, the Python script and Arduino sketch script should be uploaded on Arduino Yun and be executed.
Python script can be executed via ssh.

Also, HOST in python script for PC should be changed to proper IP address.

## Steps to Execute

1. Connect Arduino Yun and PC to same WiFi network. It is recommneded to use PC as hotspot AP and connect Arduino to that.
1. Update required files on Arduino Yun. Sketch file can be uploaded via Sketch IDE and Python script can be uploaded via SCP.
1. Execute Sketch file and python file on Arduino. If you uploaded Sketch file properly, It whill be executed automatically, and python file shoudl be executed manually via ssh. (You can set it to be executed automatically when linux is booted, if you want.)
1. Execute Python script for PC.

Then it will automatically connect to Arduino and get humidity, temperature, traffic data from Arduino and OpenAPI, and generate CSV file containing them with timestamp.
