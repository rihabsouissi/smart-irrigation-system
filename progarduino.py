from pyfirmata import Arduino, util
import time
carte = Arduino('COM8')
acquisition = util.Iterator(carte)
acquisition.start()
sensor_pin=carte.get_pin('a:1:i')
mot_pin=carte.get_pin('d:8:o')
mot_pin.write(0)
sensor_analog=sensor_pin.read()
moisture_percentage=(100-(sensor_analog/1023.00)*100)
if moisture_percentage<50:
    mot_pin.write(1)
    print ("sol sec")
    print("demarer le moteur")

else:
    mot_pin.write(0)
    print ("sol humide")
    print("Arrêter le moteur ")
carte.exit()
