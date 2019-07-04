bangou = [1,5,6,7,8,9,15,16,19]
word = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
j = word.replace(".", " ")
j = word.replace(".", " ")
j = word.replace(".", " ")
k = j.replace("  ", " ")
z = k.split(" ")
for a, b in enumerate(z):
    a = a + 1
    print(a,end=",")
    if a in bangou:
        print(b[0])
    else:
        print(b[:2])


