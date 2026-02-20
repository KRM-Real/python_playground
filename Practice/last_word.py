def lengthOfLastWord(s):                
    end = len(s) - 1

    while s[end] == " ":
        end -= 1
        
    start = end
    while start >= 0 and s[start] != " ":
        start -= 1
        
    return end - start

inputs = "luffy is still joyboy"
print(lengthOfLastWord(inputs))