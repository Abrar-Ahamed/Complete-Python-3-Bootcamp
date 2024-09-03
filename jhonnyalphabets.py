alphabet_ind = {}
capsalpha_ind = {}
asc = ord("a")
asc_alpha = ord("A")
for i in range(1,27):
    alphabet_ind[chr(asc)] = i
    capsalpha_ind[chr(asc_alpha)] = i*2
    asc_alpha += 1
    asc += 1

s = input("Enter string S: ")
#calculate index
c = 1
index = 0
#to find max index: sort alphabets in desscending order of ascii values
alpha = sorted(s,reverse = True)
word = ""
for i in alpha:
    word += i
print(word)

for i in word:
    if ord(i)>=65 and ord(i)<=90:
        index += capsalpha_ind[i]*c
    elif ord(i)>=97 and ord(i)<=122:
        index += alphabet_ind[i]*c
    c += 1
print(index)
