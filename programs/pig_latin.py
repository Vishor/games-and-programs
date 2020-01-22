# Pig Latin is a silly made-up language that alters English words.
# If a word begins with a vowel, the word yay is added to the end of it.
# If a word begins with a consonant or consonant cluster (like ch or gr), that consonant or cluster
# is moved to the end of the word followed by ay.

message = "My name is AL SWEIGART and I am 4,000 years old."
message = message.split(" ")
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
p_list = [".", ","]

# if the first letter is in uppercase, the word in latin has to have first letter in uppercase too
# if the word has >1 letters in uppercase, then the whole word is in uppercase
def is_upper(i, lw):
    if i.isupper() and len(i)>1:
        return lw.upper()
    elif i[0].isupper():
        lw = lw[0].upper() + lw[1:]
    return lw

# if the last item in i(word) is in p_list(punctuations list) it returns this item
# else return empty string
def is_punctuation(i, p_list, p=""):
    if i[-1] in p_list:
        p = i[-1]
    return p

def pig_word(vowels, i):
    p = is_punctuation(i, p_list)
    # dividing the word and the punctuation if there is any
    if p:
        i = i[:-1]
    # check if a is word
    if i.isalpha() != True:
        return i + " "
    #checking if word begins with vowel (it only recognizes lower cases)
    elif i[0].lower() in vowels:
        lw = i+"yay"
    else:
        if len(i) < 2:
            lw = i + "ay"
        # the word's lenght has to be >1, else the letter doesn't change position
        elif len(i) > 1:
            # if it's a cluster consonant, move it to the end
            if i[1] not in vowels:
                lw = i[2:]+i[:2]+"ay"
            # else move only the first letter
            else:
                lw = i[1:]+i[:1]+"ay"
    if len(lw) > 1:
        lw = is_upper(i, lw.lower())
    return lw + p + " "

def latin_message(message):
    l_message = ""
    for i in message:
        l_message += pig_word(vowels, i)
    return l_message

print(latin_message(message))
