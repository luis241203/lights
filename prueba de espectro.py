from wavefile import WaveReader
import numpy as np
from playsound import playsound
import threading

def volumenes ():
    with WaveReader("thunderstruck.wav") as r:
        for datos in r.read_iter(size=512):
            canal= datos[0]
            volume=np.linalg.norm(canal)
            vomune2=int(volume*10)
            if vomune2>13:
                vomune2=int(volume)
            else:
                vomune2=int(volume*10)
            
            #print ('|'*vomune2)
            if vomune2==0:
                print('si led 14')
                continue
            print ('no led 14')

            if vomune2>0 and vomune2<=2:
                print ('si led 7')
                continue
            print ('no led 7')
                
            if vomune2>2 and vomune2<=4:
                print ('si led 11')
                continue
            print ('no led 11')
                
            if vomune2>4 and vomune2<=6:
                print ('si led 12')
                continue
            print ('no led 12')
                
            if vomune2>6 and vomune2<=8:
                print ('si led 13')
                continue
            print ('no led 13')

            if vomune2>8:
                print ('VOLUMEN EN '+str(vomune2))
                continue
            print ('volumen debajo de parametros')


    
            

def play ():
    playsound("thunderstruck.wav")

com1=threading.Thread(target=volumenes)
com2=threading.Thread(target=play)

com1.start()
com2.start()



