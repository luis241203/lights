from wavefile import WaveReader
import numpy as np
from playsound import playsound
import threading

def volumenes ():
    with WaveReader("secrets.wav") as r:
        for datos in r.read_iter(size=512):
            canal= datos[0]
            volume=np.linalg.norm(canal)
            vomune2=int(volume*10)
            #print ('|'*vomune2)

            if vomune2>=0 and vomune2<2:
                print ('volumen 0-2')
                
            elif vomune2>2 and vomune2<4:
                print ('volumen 2-4')
                
            elif vomune2>4 and vomune2<6:
                print ('volumen 4-8')
                
            elif vomune2>6 and vomune2<8:
                print ('volumen entre 6-8')

            else:
                print ('volumen de más de 10 ')
    
            

def play ():
    with WaveReader("secrets.wav") as r:
        for datos in r.read_iter(size=512):
            canal= datos[0]
            volume=np.linalg.norm(canal)
            vomune2=int(volume*10)
            if vomune2>=7 and vomune2=<8:
                playsound("secrets.wav")
                break

com1=threading.Thread(target=volumenes)
com2=threading.Thread(target=play)

com1.start()
com2.start()



