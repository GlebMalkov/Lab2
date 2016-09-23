ivan={
   "name":"ivan",
   "age":34,
   "children":[{
       "name":"vasja",
       "age":12,
   },{
       "name":"petja",
       "age":10,
   }],
}
darja={
   "name":"darja",
   "age":41,
   "children":[{
       "name":"kirill",
       "age":21,
   },{
       "name":"pavel",
       "age":15,
   }],
}
emps=[ivan,darja]


def filt(emps, age_limit):
   filtered=[]
   for work in emps:
   	  for child in work['children']:
   	  	if child['age'] > age_limit:
   	  		filtered.append(work['name'])
   	  		break
   print(filtered)
   
  
filt(emps, 18)
