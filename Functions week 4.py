
def newlist():
    
    a= [1,2,3]
    b= [1,2,3,3,6,7]
    c = list(set(a+b))
    return c

task= newlist()
print(task)



def duplicate_chars(tup, str):
    result = ""
    for count, char in zip(tup, str):
        result += char * count
    return result

print(duplicate_chars((1,4,3,2),"Jeff"))


