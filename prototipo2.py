from machine import Pin, PWM
import utime 
import network, time
from utelegram import Bot

sensorg = Pin(27, Pin.IN, Pin.PULL_DOWN)
TOKEN = "5611853245:AAHOGw4RoYmEe8v4Wjh23lnPQQV3TjXM18I"
bot = Bot(TOKEN)

def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True

if conectaWifi ("Redmi Frank", "12345678#"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())

    @bot.add_message_handler('Hola')
    def help(update):
        
        update.reply('Hola Franky Tenemos una fuga de gas en casa, Por favor tomar acciones')
    bot.start_loop() 

        while True:
            estado = sensorg.value()
        
            if estado ==1:
                print("Fuga de gas")
                utime.sleep(2)
         
            else:
                 print("Ambiente libre de gas")
                 utime.sleep(2)

        
            
else:
       print ("Imposible conectar")
       miRed.active (False)
