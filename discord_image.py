import requests
import time
import os

payload= {
    'content' : '!clear 99', 
}

files = {
    "file" : ("./cropped.jpeg", open("./cropped.jpeg", 'rb')) # The picture that we want to send in binary
}

header= {
    'authorization': os.environ['Auth_KEY']
}

r1 = requests.post(os.environ['CHANNEL_KEY'],
                    data=payload,headers=header)

time.sleep(60)

r2 = requests.post( os.environ['CHANNEL_KEY'],
                    headers=header,files=files)
