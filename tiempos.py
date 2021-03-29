from wavefile import WaveReader
import numpy as np
import time
import wave, contextlib
vol= []
with WaveReader("thunderstruck.wav") as r:
        for datos in r.read_iter(size=512):
            canal= datos[0]
            volume=np.linalg.norm(canal)
            volumen2=int(volume*10)
            vol.append(volumen2)
print(len(vol))
with contextlib.closing(wave.open('thunderstruck.wav','r')) as s:
        frames= s.getnframes()
        rate=s.getframerate()
        duracion= frames / (float(rate))
        print('el clip dura  '+ str(duracion))
        r1=(duracion*44100.0)
        r2=(r1/512.0)           
        print (r2)

def volumenes ():
    ti=time.time()
    #print('volumenes '+str(ti))
    #time.sleep(0.01142195732344882)
    for x in vol:
        #time.sleep(0.0112)
        #print('volume {}'.format(volume))
        print('|'* x)
    t0=time.time()
    tiempos=(t0-ti)
    print('tiempo de proceso: '+str(tiempos))
    tiempo1= (tiempos)

    tr1=duracion-tiempo1
    tr= tr1 / (len(vol))

    print (tr1)
    print (tr)   
"""def duration(archivo):
    with contextlib.closing(wave.open(archivo,'r')) as s:
        frames= s.getnframes()
        rate=s.getframerate()
        duracion= frames / (float(rate))
        print('el clip dura  '+ str(duracion))
#tiempo 011412091718182676


    ti=time.time()
    for x in vol:
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
            continue
        print ('volumen debajo de parametros')"""




    

volumenes()

