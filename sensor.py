from antares_http import antares
from time import sleep

ANTARES_KEY = 'e75aca9711895ddc:9d6d5c89265bee66' #Key in your Profile

while 1:

    dataKapasitif = {
    'ORGANIC' : 32,
    'NON_ORGANIC' : 50
    }
    dataUltrasonic = {
    'VOLUME' : '20%',
    }
    #antares.setAccessKey(ANTARES_KEY)
    #antares.send(dataKapasitif, 'TRASHSCAN', 'SensorProximityKapasitif')
    print("==== SEND DATA ====")
    print(" Sensor ProximityKapasitif", dataKapasitif)
    print(" Sensor Ultrasonic", dataUltrasonic)
    print("===================")
    sleep(10)
    

