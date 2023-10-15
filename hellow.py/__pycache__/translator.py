def translate(phrasse):
    translation = ""
    for letter in phrasse :
        if letter in "AEIOUaeiou" :
            translation = translation +"r"
        else :
            translation = translation + letter
    
    return translation

print(translate(input(" Enter the Phrase : ")))