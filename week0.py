string=input("Enter sentences:").lower().split('.')
new =''
for i in string:
    word=i.split()
    if word!=[]:
        sentences1=" ".join(word)
        new +=sentences1.capitalize() + '. '

print ("The formatting sentence is:"+new)