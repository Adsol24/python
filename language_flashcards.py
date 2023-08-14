import random
print("type phrases, vocab, or description dictionary to see all words in each category")
print("type 1.phrases test, 2.vocab test, or 3.description test to quiz yourself")
u_input = input(print("what would you like to do:"))

phrases = {'parfois':'sometimes', 'Jaimerais':'I would like', 'vrai':'true', 'Sans':'without', 'autrement':'otherwise',
           'trop':'too much', 'souvent':'often', 'Pour':'for', 'je voulais juste': 'I just wanted',"pas de":'no (something',
           'comme':'how', 'Cest':'its', 'est':'is', 'en':'in', 'ton/ta':'your', 'nous':'we', 'je taime':'I love you',
           'ou est':'where is', 'cest pour quel genre':'what kind of', 'je viens(), nous sommes()':'I am from, we are from',
           'je suis':'I am'}
vocab = {'gare':'train station','voiture':'car','boef':'beef'}
description = {'amusant':'funny', 'fantastique':'fantastic'}

if u_input == 'phrases dictionary':
    for key,value in phrases.items():
        print(key,value)
if u_input == 'vocab dictionary':
    for key,value in vocab.items():
        print(key,value)
if u_input == 'description dictionary':
    for key,value in description.items():
        print(key,value)
if u_input == '1':
    francais = random.choice(list(phrases.keys()))
    u_guess = input("enter the english translation of {}: ".format(francais))
    correct_phrases = phrases[francais]

    if u_guess == correct_phrases:
        print("Correct!")
    else:
        print("incorrect, the translation of {} is {}".format(francais, correct_phrases))

if u_input == '2':
    francais1 = random.choice(list(vocab.keys()))
    u_guess1 = input("enter the english translation of {}: ".format(francais1))
    correct_vocab = vocab[francais1]

    if u_guess1 == correct_vocab:
        print("Correct!")
    else:
        print("incorrect, the translation of {} is {}".format(francais1, correct_vocab))
if u_input == '3':
    francais2 = random.choice(list(description.keys()))
    u_guess2 = input("enter the english translation of {}: ".format(francais2))
    correct_description = description[francais2]

    if u_guess2 == correct_description:
        print("Correct!")
    else:
        print("incorrect, the translation of {} is {}".format(francais2, correct_description))


