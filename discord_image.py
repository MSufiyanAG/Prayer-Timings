import requests
import os

payload= {
    'content' : 'image_bytes', 
}


files = {
    "file" : ("./cropped.jpeg", open("./cropped.jpeg", 'rb')) # The picture that we want to send in binary
}

header= {
    'authorization': os.environ['Auth_KEY']
}

r = requests.post( os.environ['CHANNEL_KEY'],
                    headers=header,files=files)
