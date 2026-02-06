def mirror_string(strings):
    
    mirrored = strings + strings[::-1]
    
    return mirrored
    
    

word = "RaceCar"
print(mirror_string(word))