#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 21, 2014

@author: anroco

In Python, how to use the operators + and * with bytes objects?

En Python, ¿Cómo usar los operadores + y * con los objetos bytes?
'''

#create a bytes object
b = b'byte 123'
print (b)

#The * operator allow repeat the characters of a bytes object
print(b * 3)

#create two bytes objects.
b1 = bytes([80, 121, 116, 104, 111, 110, 32])
b2 = b'easy'

#The + operator allow create a new bytes object joining two or more bytes.
b = b1 + b2
print(b)

#create a bytes object combining operators
b = b'by' + b'e' * 4 + b'!'
print(b)
