word = input()

vowel = ['a','e','i','o','u']

lenght = len(word)
a = 0
e = 0
i = 0
u = 0

for j in range(lenght):
    for letter in vowel:
        if word.find(letter,j,j+1) != -1:
            if letter == 'a':
                a+=1
            elif letter == 'e':
                e+=1
            elif letter == 'i':   
                i+=1
            elif letter == 'u':  
                u+=1
  
if a == 0 or e == 0 or i == 0 or u == 0:
    print("False")
else:
    print(" Слово содержит букву a",a,"раз, e",e,"раз, i",i,"раз, u",u,"раз.")
    print("Слово содержит ",(a+e+i+u)," гласных и ", lenght - (a+e+i+u), "согласных букв")
