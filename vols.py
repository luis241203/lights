from wavefile import WaveReader
import numpy as np
from playsound import playsound
import threading,time
#tiempos.duration('thunderstruck.wav')
vol= []

def volumenes ():
    ti=time.time()
    with WaveReader("thunderstruck.wav") as r:
        for datos in r.read_iter(size=512):
            canal= datos[0]
            #print('canal:{} '.format(canal) )
            volume=np.linalg.norm(canal)
            print('volume {}'.format(volume))
    t0=time.time()
    print(to-ti)        
            """x=int(volume*10)
            time.sleep(0.11)
            if x==0:
                print('si led 14')
                continue
            print ('no led 14')

            if x>0 and x<=7:
                print ('si led 7')
                continue
            print ('no led 7')
                
            if x>7 and x<=14:
                print ('si led 11')
                continue
            print ('no led 11')
                
            if x>14 and x<=21:
                print ('si led 12')
                continue
            print ('no led 12')
                
            if x>28 and x<=35:
                print ('si led 13')
                continue
            print ('no led 13')

            if x>35:
                print ('VOLUMEN EN '+str(x))
                break
            


    
            

def play ():
    playsound("thunderstruck.wav")"""

com1=threading.Thread(target=volumenes)
#com2=threading.Thread(target=play)

com1.start()
#com2.start()



