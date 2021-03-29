import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

archivo=('thunderstruck.wav')
fsonido, sonido= sf.read(archivo)

y= (fsonido)

numf=len(y)
n=np.arange(0,numf)/sonido

c=fft(y)
M_gk=abs(c)
M_gk= M_gk[0:numf//2]/numf

Ph_gk= np.angle(c)
F= sonido*np.arange(0, numf//2)/numf
"""print(c)
print(M_gk)
print(F)
print(Ph_gk)"""

plt.plot(F, M_gk)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.show()



