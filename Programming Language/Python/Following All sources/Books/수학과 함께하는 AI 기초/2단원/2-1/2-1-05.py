# 데이터를 직접 설정해 보기

a1 = []
a1.append({'num':0, 'wnum':0, 'ynum':0})     
a1.append({'num':0, 'wnum':0, 'ynum':0})      
a1.append({'num':0, 'wnum':0, 'ynum':0})     
a1.append({'num':0, 'wnum':0, 'ynum':0})     
a1.append({'num':0, 'wnum':0, 'ynum':0})     
a1.append({'num':7, 'wnum':5, 'ynum':6})     
a1.append({'num':4, 'wnum':1, 'ynum':3})     
a1.append({'num':20, 'wnum':1, 'ynum':16})   
a1.append({'num':22, 'wnum':0, 'ynum':16})   
a1.append({'num':17, 'wnum':4, 'ynum':16})   
a1.append({'num':5, 'wnum':1, 'ynum':5})     
a1.append({'num':13, 'wnum':5, 'ynum':13})   
a1.append({'num':19, 'wnum':11, 'ynum':18})  
a1.append({'num':9, 'wnum':5, 'ynum':1})     
a1.append({'num':14, 'wnum':10, 'ynum':4})   
a1.append({'num':18, 'wnum':16, 'ynum':4})   
a1.append({'num':15, 'wnum':13, 'ynum':2})   
a1.append({'num':13, 'wnum':5, 'ynum':10})   
a1.append({'num':18, 'wnum':13, 'ynum':14})  
a1.append({'num':16, 'wnum':16, 'ynum':13})   
a1.append({'num':8, 'wnum':5, 'ynum':7})      
a1.append({'num':10, 'wnum':8, 'ynum':7})     
a1.append({'num':10, 'wnum':8, 'ynum':10})    
a1.append({'num':4, 'wnum':0, 'ynum':3})      

a2 = []
a2.append({'num':0, 'wnum':0, 'ynum':0})

a = [a1, a2]

for i in range (0, len(a[0])) :
    print("Mon[", i, "] = ", a[0][i])

'''
Mon[ 0 ] =  {'num': 0, 'wnum': 0, 'ynum': 0}
Mon[ 1 ] =  {'num': 0, 'wnum': 0, 'ynum': 0}
Mon[ 2 ] =  {'num': 0, 'wnum': 0, 'ynum': 0}
Mon[ 3 ] =  {'num': 0, 'wnum': 0, 'ynum': 0}
Mon[ 4 ] =  {'num': 0, 'wnum': 0, 'ynum': 0}
Mon[ 5 ] =  {'num': 7, 'wnum': 5, 'ynum': 6}
Mon[ 6 ] =  {'num': 4, 'wnum': 1, 'ynum': 3}
Mon[ 7 ] =  {'num': 20, 'wnum': 1, 'ynum': 16}
Mon[ 8 ] =  {'num': 22, 'wnum': 0, 'ynum': 16}
Mon[ 9 ] =  {'num': 17, 'wnum': 4, 'ynum': 16}
Mon[ 10 ] =  {'num': 5, 'wnum': 1, 'ynum': 5}
Mon[ 11 ] =  {'num': 13, 'wnum': 5, 'ynum': 13}
Mon[ 12 ] =  {'num': 19, 'wnum': 11, 'ynum': 18}
Mon[ 13 ] =  {'num': 9, 'wnum': 5, 'ynum': 1}
Mon[ 14 ] =  {'num': 14, 'wnum': 10, 'ynum': 4}
Mon[ 15 ] =  {'num': 18, 'wnum': 16, 'ynum': 4}
Mon[ 16 ] =  {'num': 15, 'wnum': 13, 'ynum': 2}
Mon[ 17 ] =  {'num': 13, 'wnum': 5, 'ynum': 10}
Mon[ 18 ] =  {'num': 18, 'wnum': 13, 'ynum': 14}
Mon[ 19 ] =  {'num': 16, 'wnum': 16, 'ynum': 13}
Mon[ 20 ] =  {'num': 8, 'wnum': 5, 'ynum': 7}
Mon[ 21 ] =  {'num': 10, 'wnum': 8, 'ynum': 7}
Mon[ 22 ] =  {'num': 10, 'wnum': 8, 'ynum': 10}
Mon[ 23 ] =  {'num': 4, 'wnum': 0, 'ynum': 3}
'''