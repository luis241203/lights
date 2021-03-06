import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np

archivo=('secrets.wav')
fsonido, sonido= sf.read(archivo)

y= (fsonido)
Pxx, freqs, bins, im =plt.specgram(y, NFFT=512, Fs=sonido, cmap="inferno")

plt.gcf().set_size_inches(10,6)
plt.xlim(0, len(y)/sonido)
plt.ylim(0, sonido/2)
plt.colorbar(im).set_label('Intensidad (db)')
plt.xlabel('tiempo (s)')
plt.ylabel('frecuencia (Hz)')
plt.show()

print (0, sonido/2)
print(0, len(y)/sonido)
print(Pxx,freqs, bins)
plt.plot(fsonido)
plt.show()
for x in freqs:
    while x > 1000 and x < 1000:
        print ('mas de 100 y menos de 1000')
        break

