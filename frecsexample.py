# Read in a WAV and find the freq's
import pyaudio
import wave
import numpy as np
import sys
import time
#import RPi.GPIO as GPIO

leds = range(2, 14)

chunk = 1024

# open up a wave
wf = wave.open('thunderstruck.wav', 'rb')
swidth = wf.getsampwidth()
RATE = wf.getframerate()
window = np.blackman(chunk)
MAX = 500
MIN = 0

# open stream
p = pyaudio.PyAudio()


def callback(in_data, frame_count, time_info, status):
    #GPIO.setmode(GPIO.BCM)
    # data = wf.readframes(frame_count)
    global MAX
    global MIN
    global swidth
    global window

    thefreq = 0
    leds = range(2, 14)

    # unpack the data and times by the hamming window
    unpacked = wave.struct.unpack("%dh"%(len(data)/swidth), data)
    if unpacked and len(unpacked) == len(window):
        indata = np.array(unpacked) * window
        # Take the fft and square each value
        fftData=abs(np.fft.rfft(indata))**2
        # find the maximum
        which = fftData[1:].argmax() + 1
        # use quadratic interpolation around the max
        if which != len(fftData)-1:
            y0,y1,y2 = np.log(fftData[which-1:which+2:])
            x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
            # find the frequency and output it
            thefreq = (which+x1)*RATE/chunk
            print ("The freq is %f Hz." % (thefreq))
        else:
            thefreq = which*RATE/chunk
            print ("The freq is %f Hz." % (thefreq))
        # read some more data
        data = wf.readframes(chunk)

        if thefreq > MAX:
            MAX = int(thefreq)
        elif thefreq < MIN:
            MIN = int(thefreq)

        index = ((thefreq - MIN) / ((MAX - MIN) / len(leds))) + 1
        print ("index: "+ index)
        for led in leds:
            #GPIO.setup(led, GPIO.OUT)
            if led <= index:
                print('led '+led+' activo')
            else:
                print('led '+led+' inactivo')

    return (data, pyaudio.paContinue)


stream = p.open(format=
                p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=RATE,
                output=True,
                stream_callback=callback)

stream.start_stream()

# play stream and find the frequency of each chunk
while stream.is_active():
    time.sleep(0.1)

#GPIO.cleanup()

stream.stop_stream()
stream.close()
wf.close()
p.terminate()