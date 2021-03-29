from wavefile import WaveReader
import numpy as np
#from playsound import playsound
import simpleaudio as sa
import threading,time
#tiempos.duration('thunderstruck.wav')
vol= []
song=sa.WaveObject.from_wave_file("thunderstruck.wav")
with WaveReader("thunderstruck.wav") as r:
        for datos in r.read_iter(size=512):
            canal= datos[0]
            #print('canal:{} '.format(canal) )
            volume=np.linalg.norm(canal)
            volumen= int(volume*10)
            vol.append(volumen)
def volumenes ():
    ti=time.time()
    #print('volumenes '+str(ti))
    #time.sleep(0.01142195732344882)
    for x in vol:
        time.sleep(0.0112)
        #print('volume {}'.format(volume))
        print('|'* x)
    t0=time.time()
    print('tiempo de proceso: '+str(t0-ti))        

#simpleaudio


    
def play ():
    ti=time.time()
    #print('play '+str(ti))
    song.play()
    #playsound("thunderstruck.wav", block=False)
    t0=time.time()
    print('simpleaudio '+str(t0-ti))  
com1=threading.Thread(target=volumenes)
com2=threading.Thread(target=play)

com1.start()
com2.start()
           





