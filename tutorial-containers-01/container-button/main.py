import qwiic_button
import requests
import time

my_button = qwiic_button.QwiicButton()
while True:
    requests.post(f'button/{my_button.is_button_pressed()}')
    time.sleep(1)
