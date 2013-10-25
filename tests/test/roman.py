#!/usr/bin/env python
#coding:utf-8
import re
#define exceptions

class RomanError(Exception): pass

class OutOfRangeError(RomanError): pass

class NotIntegerError(RomanError): pass

class InvalidRomanNumeralError(RomanError): pass

#Define digit mapping
romanNumeralMap = (('M', 1000),
                ('CM', 900),
                ('D', 500),
                ('CD', 400),
                ('C', 100),
                ('XC', 90),
                ('L', 50),
                ('XL', 40),
                ('X', 10),
                ('IX', 9),
                ('V', 5),
                ('IV', 4),
                ('I', 1))

def toRoman(n):
    """Convert integer to roman numberal"""
    if not (0 < n < 4000):
        raise OutOfRangeError, 'number out of range(must between 1~3999)'
    if not int(n) == n:
        raise NotIntegerError, 'noo-integer can not bu converted'
 
    result = ''
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result

#Define pattern to detect valid Roman numerals
romanNumeralPattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'

def fromRoman(s):
    """Convert Roman numberal to integer"""
    if not re.search(romanNumeralPattern, s):
        raise InvalidRomanNumeralError, 'Invalid Roman numeral: %s' % s
    if not s:
        raise InvalidRomanNumeralError, 'Input can not be blank'

    result = 0
    index = 0
    for numeral, integer in romanNumeralMap:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result
