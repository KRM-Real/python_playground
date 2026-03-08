# 171. Excel Sheet Column Number
# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# For example:
# A -> 1, B -> 2, C -> 3, Z -> 26, AA -> 27, AB -> 28 


def titleToNumber(columnTitle):
    
    val = [i for i in range(1, 27)]
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    mapping = dict(zip(letters, val))
    
    i = len(columnTitle)-1
    
    result = 0
    count = 0

    
    # print(columnTitle)
    while i >= 0:
        result = mapping[columnTitle[i]] * (26**count) + result
        i-=1
        count+=1
        
    return result

column = "ZY"
print(titleToNumber(column))