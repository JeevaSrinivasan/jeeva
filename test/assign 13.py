var = "123 hi 123 hi 123 hi 123 hi 123 hi"
substring="hi"
counter=var.count(string)
offste=0
while counter>0:
    index = var.find(substring)
    var[:index+len(substring)]
    var=var[index+len(substring):]
    offset=index+len(substring)
    counter-=1
for i in range(0,len(var)):

     part1=var[:index+len("one")]
     part2=var[index+len("one"):]
     print(part2.find("one"))
