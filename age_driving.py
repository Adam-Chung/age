# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 16:21:08 2021

@author: fong_
"""
driving = input('你開過車嗎?')
if driving != 'yes' and driving !='no':
    print('please input yes/no')
    raise SystemExit
    
age = int(input('你貴庚'))

if driving == 'yes':
    if age >=18:
        print('good job')
    else:
        print('suck')
elif driving =='no':
    if age >=18:
        print('you can drive')
    else:
        print('你在',18-age,'年就可去考囉')
