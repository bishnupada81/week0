string=input("Enter sentences:").lower()
sentence=string.split('.')
new =''
for i in sentence:
    word=i.split()
    if word!=[]:
        sentences1=" ".join(word)
        new +=sentences1.capitalize() + '. '

print ("The formatting sentence is:"+new)