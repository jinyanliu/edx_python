# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

resultInt = int(input('Enter an interger: '))

if(resultInt == 0):
    for times in range(1,6):
        print('0**'+str(times) +'=0')
    exit
    
rootInt = 0
while rootInt <= abs(resultInt):
    for pwrInt in range(1,6):
        if rootInt**pwrInt == abs(resultInt):
      
            if (resultInt < 0) and (pwrInt%2 != 0) :
                print( str(-rootInt) +'**'+str(pwrInt) +'='+ str(resultInt))
                
            if(resultInt > 0) and (pwrInt%2 == 0):
                print( str(-rootInt) +'**'+str(pwrInt) +'='+ str(resultInt))
                print( str(rootInt) +'**'+str(pwrInt) +'='+ str(resultInt))
                
            if(resultInt > 0) and (pwrInt%2 != 0):
                print( str(rootInt) +'**'+str(pwrInt) +'='+ str(resultInt))
                
            break;
    rootInt = rootInt + 1