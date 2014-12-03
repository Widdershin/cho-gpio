import requests
import json
import time
from RPi.GPIO import setmode, IN, OUT, BCM, setup, add_event_detect, RISING

setmode(BCM)

PLAYER1_CHANNEL = 18
PLAYER2_CHANNEL = 4

setup(PLAYER1_CHANNEL, IN)
setup(PLAYER2_CHANNEL, IN)


def player_scored(player_number):
    print("Player {} scored!".format(player_number))
    requests.post(
        'http://localhost:3000/scores',
        data=json.dumps({'player': player_number}),
        headers={'content-type': 'application/json'}
    )
        


add_event_detect(PLAYER1_CHANNEL, RISING, callback=lambda _: player_scored(1), bouncetime=200)
add_event_detect(PLAYER2_CHANNEL, RISING, callback=lambda _: player_scored(2), bouncetime=200)


print("Listening for button presses...")

while raw_input('Type exit to exit') != 'exit':
  pass

exit()
