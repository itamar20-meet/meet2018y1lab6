count= input ('type a number') 
    
if count % 3 == 0 and count % 5 == 0 :
         count='fizzbuzz'
elif count % 5 == 0:
        print("buzz")
elif count % 3 == 0 :
        print ('fizz')
else:
    print('sorry! wrong answer')        
