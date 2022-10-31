print("\t't ********application********")

a=('''To
The Principle 
school
address
date:<|date|>

subject:- Application for leave

respected sir/madam,

Respectfully, I am here to inform you that, 
I am suffering from fever since last night, 
The doctor had advised me to take rest for 
____ days.
\t Hence, kindely grant me leave for____days.
I shall be thankful to you


your's obediently

name:|name|
class:|class|
roll no:|roll no|
'''
)

b=input("name:")
c=input("class:")
d=input("roll no:")
e=input("date:")
f=input("time period:")
g=input("school:")
h=input("address:")

print('___________________________________________')
a=a.replace('school',g)
a=a.replace('address',h)
a=a.replace('<|date|>',e)
a=a.replace('|name|',b)
a=a.replace('|class|',c)
a=a.replace('|roll no|',d)
a=a.replace('___',f)
print(a)