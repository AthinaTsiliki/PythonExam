import urllib2
import json
import datetime

cur_date=datetime.datetime.now()

my_list=[]
maxlen = 10
while len(my_list) < maxlen:
    i = int(input("Enter a number to create your list: "))
    if i < 1 or i > 81:
        print("Your number is out of range!Please try again!")
        continue
    else:
        if i not in my_list:
            my_list.append(i)
    
print ("Finally your list is:")
print sorted(my_list)
def compare_lists(my_list,klhrwseis):
    count = 0 
    for i in my_list :
        if i in klhrwseis:
           count += 1
    return count


for i in range(31):
    cur_date= cur_date - datetime.timedelta(days=1)
    date_str= cur_date.strftime("%d-%m-%Y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']
    r=[]
    for k in klhrwseis:
        tmp=k["results"]
        r.append(compare_lists(my_list,tmp))
    print "Results for date ",date_str,"are: "
    print min(r),r.count(min(r))
    print max(r),r.count(max(r))
    print 12*"-"
times_won = 0
for nr in r:
    if nr >= 4:
        times_won += 1
print "you won", times_won, "times"
   
  
