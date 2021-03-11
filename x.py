
ans=[]
v=set()
a,e,i,o,u=0,0,0,0,0
s=input("enter the sentence\n") # entering the user input 
s=s.lower()        #changing it to lower case
for j in s:                             #taking each alphabet of sentence
    if 'a' == j:                         # to check if it is a vowel or not
        a+=1                             # count the number of times a vowel appear
        v.add('a')                       #  add it to the set
    elif 'e' == j:
        e+=1
        v.add('e')
    elif 'i'== j:
        i+=1
        v.add('i')
    elif 'o'== j:
        o+=1
        v.add('o')    
    elif 'u'== j:
        u+=1
        v.add('u')
for j in v:                       # to check which vowels are present
    if j == 'a':
       ans.append(a)                # add their count value in list
    if j == 'e':
        ans.append(e)
    if j == 'i':
        ans.append(i)
    if j == 'o':
        ans.append(o) 
    if j == 'u':
        ans. append(u)     
print(v, '\n', ans)              