
def word_counter(content:str)->int:
    return len(content.split())
def paragraph_counter(content:str)->int:
    counter = 0
    listed_content = list(content)
    for indice,char in enumerate(listed_content):
        if char == "\n" and indice < (len(listed_content)-1):
            if listed_content[indice+1] != "\n":
                counter+=1
        elif indice == len(listed_content)-1:
            counter+=1
    return counter

def sentence_counter(content:str)->int:
    separadores = ['.', '!', '?']
    num_oraciones = 0
    for caracter in content:
        if caracter in separadores:
                num_oraciones += 1
    return num_oraciones

def word_frequence(content:str)->str:
    words = content.split()
    words_dictionary = {word:0 for word in words}
    text = "\n"
    for word in words_dictionary:
        for w in words:
            if word == w:
                words_dictionary[word]+=1
    for word in words_dictionary:
        text += f"{word} | {words_dictionary[word]} | {round(words_dictionary[word]/len(words)*100,2)}%\n"
    return text

def vowel_and_consonant_counter(content:str)->tuple[int, int]:
    vocales = 'aeiou'
    consonantes = 'bcdfghjklmnñpqrstvwxyz'
    vowel_counter = 0
    consonant_counter = 0
    for char in content:
        if char.lower() in vocales:
            vowel_counter+=1
        elif char.lower() in consonantes:
            consonant_counter+=1
    return (vowel_counter,consonant_counter)

def lowercase_and_upercase_counter(content:str)->tuple[int, int]:
    abecedario_minuscula = 'abcdefghijklmnopqrstuvwxyz'
    abecedario_mayuscula = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_counter = 0
    upercase_counter = 0
    for char in content:
        if char in abecedario_minuscula:
            lowercase_counter+=1
        elif char in abecedario_mayuscula:
            upercase_counter+=1
    return (lowercase_counter,upercase_counter)

