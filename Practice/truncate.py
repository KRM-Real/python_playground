def truncate_text(text):
    
    if len(text) <= 20:
        return text
    
    else:
        return text[:17] + "..."

word = "Exactly twenty chars"
print(truncate_text(word))