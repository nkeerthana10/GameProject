import requests
import json

url = "https://wizklub.com/api/secured/wiziot-poll-request/"

headers = {"Api-Access-Key": "ZWlYUHdqUDVjMG9VZTRWX0FscVU=", "Api-Secret-Key": "amM0SF9nb2RHUlFIaTJfRFVLSlRaeG55VG5PR08zQkhJQQ==", "Content-Type": "application/json"}

payload_reset = json.dumps({"mode": "WRITE", "device_id": "keerthana_IoT_device", "source": "API", "api": "oled", "type": "reset", "msg_to_write": "", "x_axis": "0", "y_axis": "0"})

payload_text = json.dumps({"mode": "WRITE", "device_id": "keerthana_IoT_device", "source": "API", "api": "oled", "type": "text", "msg_to_write": "Welcome All", "x_axis": "2", "y_axis": "5"})

requests.request("POST",url, headers = headers, data = payload_reset) #reset oled

response = requests.request("POST", url, headers = headers, data = payload_text) #display text

print(response.json())

