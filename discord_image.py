import requests

payload= {
    'content' : 'image_bytes', 
}


files = {
    "file" : ("./cropped.jpeg", open("./cropped.jpeg", 'rb')) # The picture that we want to send in binary
}

header= {
    'authorization': Auth_KEY
}

r2 = requests.post(CHANNEL_KEY,
                    headers=header,files=files)