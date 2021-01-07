# 첫번째 폴더 내의 소리 데이터 제목 출력  
folder = ['discomfort', 'hungry', 'laugh', 'tired']

for i in range(0,10):
   a = folder[0]+'/'+folder[0]+'_'+str(i+1)+'.wav'
   print(a)

'''
discomfort/discomfort_1.wav
discomfort/discomfort_2.wav
discomfort/discomfort_3.wav
discomfort/discomfort_4.wav
discomfort/discomfort_5.wav
discomfort/discomfort_6.wav
discomfort/discomfort_7.wav
discomfort/discomfort_8.wav
discomfort/discomfort_9.wav
discomfort/discomfort_10.wav
'''