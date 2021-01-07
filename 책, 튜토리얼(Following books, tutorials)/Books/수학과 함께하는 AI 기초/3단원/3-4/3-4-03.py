# 여러 폴더에 저정된 소리 파일 가져오기
folder = ['discomfort', 'hungry', 'laugh', 'tired']

# 4개 폴더의 첫 번째 소리 데이터 제목 출력
for i in range(0,4):
    a = folder[i]+'/'+folder[i]+'_1.wav'
    print(a)

'''
discomfort/discomfort_1.wav
hungry/hungry_1.wav
laugh/laugh_1.wav
tired/tired_1.wav
'''