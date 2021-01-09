import librosa
import librosa.display
import matplotlib.pyplot as plt

#waveplot
audio = 'discomfort/discomfort_01.wav'
y, sr = librosa.load(audio)

librosa.display.waveplot(y, sr=sr)
plt.title('Waveplot')
plt.show()


#하나의 plot 생성_waveplot_discomfort
folder = ['discomfort', 'hungry', 'laugh', 'tired']
set_label=[]

for i in range(1,10):
    a = folder[0]+'/'+folder[0]+'_0'+str(i)+'.wav'
    y, sr = librosa.load(a)
    librosa.display.waveplot(y, sr=sr, alpha=0.5)
    set_label.append(i)
    
plt.legend(set_label)
plt.title(folder[0])
plt.xlabel("Time(ms)")
plt.ylabel("Sound(dB)")
plt.show()

#하나의 그래프에 여러 개의 소리 데이터 표현-discomfort-화면분할
for i in range(1,10):
    plt.subplot(3,3,i)
    a = folder[0]+'/'+folder[0]+'_0'+str(i)+'.wav'
    y, sr = librosa.load(a)
    librosa.display.waveplot(y, sr=sr)
    plt.title(folder[0]+str(i))
plt.tight_layout()
plt.show()

#여러개의 subplot 생성-4가지 상황
for i in range(0,4):
    plt.subplot(4,1,i+1)
    a = folder[i]+'/'+folder[i]+'_01.wav'
    y, sr = librosa.load(a)
    librosa.display.waveplot(y, sr=sr)
    plt.title(folder[i])
plt.tight_layout()
plt.show()

#여러개의 subplot 생성-4가지 상황, 동일 시간
for i in range(0,4):
    plt.subplot(4,1,i+1)
    a = folder[i]+'/'+folder[i]+'_01.wav'
    y, sr = librosa.load(a)
    librosa.display.waveplot(y[:100000], sr=sr)
    plt.title(folder[i])
plt.tight_layout()
plt.show()

#여러개의 subplot 생성-4가지 상황, 동일 시간, 다른 색
for i in range(0,4):
    plt.subplot(4,1,i+1)
    a = folder[i]+'/'+folder[i]+'_07.wav'
    y, sr = librosa.load(a)
    librosa.display.waveplot(y[:100000], sr=sr, color=plt.cm.Spectral(i*55))
    plt.title(folder[i])
plt.tight_layout()
plt.show()
