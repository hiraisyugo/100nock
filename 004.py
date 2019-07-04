word = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
word1 = word.replace(',', ' ')
print(word1)
word2 = word1.replace('.', ' ')
print(word2)
word3 = word2.split(" ")

print(word3)
list = []
for i in word3:
    i = len(i)
    print(i)
