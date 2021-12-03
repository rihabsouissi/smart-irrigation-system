import matplotlib
import matplotlib.pyplot as plt
import numpy as nb
import random
i=1
l=[]
l2=[]
while i<32:
    l.append(i)
    sensor_analog=random.randint(0,1023)
    humidité_percentage=100-((sensor_analog/1023.00)*100)
    l2.append(humidité_percentage)
    print('humidité_percentage=',humidité_percentage)
    if humidité_percentage < 50:
        print ("sol sec")
        print("demarer le moteur")
        plt.plot(i,humidité_percentage,'b.')
    else :
        print ("sol humide")
        print("Arrêter le moteur ")
        plt.plot(i,humidité_percentage,'r.')
    x=nb.array(l)
    y=nb.array(l2)
    i=i+1
plt.plot(x,y)
plt.title("humidité_percentage par jour")
plt.xlabel("jour")
plt.ylabel("humidité_percentage")
plt.show()