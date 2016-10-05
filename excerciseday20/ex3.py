import random

verbs = ['sang', 'ran', 'jumped', 'danced']
nouns = ['cat', 'dog', 'woman', 'man', 'boy']
artcles = ['the', 'a']
adverbs = ['loudly', 'quietly', 'well', 'badly']

# n = 0
# line = ''
# while n < 5:
#     number = random.randint(0,1)
#     if number:
#         print(random.choice(nouns)+random.choice(adverbs)+random.choice(verbs))
#     else:
#         print(random.choice(artcles)+random.choice(nouns)+random.choice(verbs))
#     n = n + 1

#
# n = 0
# default = input('how much lines do you want: ')


import sys
lines = 5
if len(sys.argv) > 1:
    try:
        temp = int(sys.argv[1])
        if not 1<= temp <= 10:
            print('lines must be 1-10')
        else:
            lines = temp
    except ValueError as err:
        print('Error' + err)

n = 0

while n < lines:
    artcle = random.choice(artcles)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    number = random.randint(0, 1)
    if number:
        print(artcle, noun, verb)
    else:
        adverb = random.choice(adverbs)
        print(artcle, noun, verb, adverb)
    n = n + 1