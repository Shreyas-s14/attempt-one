import os
import requests


def send_text(url_link, text_path):
    info = open(text_path, "rb").read()
    payload = {"text": info,"id":123}

    response = requests.post(url_link, files=payload).json()

    return response


resp = send_text("http://localhost:4001/process", "./content/text1.txt")
print(resp)