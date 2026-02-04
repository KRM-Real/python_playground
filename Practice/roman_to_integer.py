class Solution(object):
    def romanToInt(self, s):
       
        result = 0
        roman_values ={
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        for x, y in zip(s, s[1:]):
            if roman_values[x] < roman_values[y]: 
            # When the condition is True, then value of result will be subtracted by X
                result -= roman_values[x]
            else:
                result += roman_values[x]
        
        return result + roman_values[s[-1]]

        