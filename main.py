from mq2 import MQ2
from utime import sleep_ms 
from machine import Pin , PWM, ADC
import network, time, urequests

def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 4):
                  return False
      return True
    
sensorg = MQ2 (Pin(34))

sensorg.calibrate()
print("Calibración completa")


if conectaWifi("Redmi Frank", "12345678#"):

    print("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())

    url_1 = "https://maker.ifttt.com/trigger/sensorGas/with/key/gWUKJPf3bornWX7tQ6re08yG6Exr6YZiv5WRkI-pifI?"


    while True: 
                
        time.sleep (2)
        lectura=float(sensorg.readMethane())
        print("Nivel de metano: {:.1f}".format(lectura) )
        sleep_ms(1)


        if lectura > 4.0:
                      
            envio_ifttt = urequests.get(url_1+"&value1="+str(lectura))      
            print( envio_ifttt.text, envio_ifttt.status_code)
            envio_ifttt.close ()
            
            buzzer = PWM(Pin(32), freq = 5000)
            for i in range(0, 1023):
                buzzer.duty(i)
                sleep_ms(1)


else:
       print ("Imposible conectar")
       miRed.active (False)