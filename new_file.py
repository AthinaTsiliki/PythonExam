import random
file=open("F:\\1stSemester\\PythonEx\\trueDetective.txt")
read_file=file.read()
txt=[]
list_of_lists=[]
b=read_file.split(" ")
empty_list=[]
for item in b:
    empty_list=empty_list+[item.lower().replace('.','').replace(',','').strip()] 
    #Only lowercase letters without characters dot and comma are in empty_list.
q=0
w=3
for i in range(len(empty_list)-3):
    q += 1
    w += 1
    list_of_lists.insert(0,empty_list[q:w])
    
start =(random.choice(list_of_lists))
for word in start:
    txt.append(word)

count = 0
while len(txt) <= 205:
    count += 1
    for three_words in list_of_lists:
        if txt[-2] == three_words[0] and txt[-1] == three_words[1]:
            if len(txt) <= 200:
                for word in three_words:
                    txt.append(word)
    if count > 1000:
        break

result = " ".join(txt)
print "I found", len(txt), "words chained together"
print ""
print result
file.close()
