
def encode(ip):
    string = ""
    for s in ip:
        string += str(len(s)) + "#" + s
    return string

def decode(ip):
    list = []
    i = 0
    while i<len(ip):
       j = i
       while ip[j] != "#":
           j += 1
       length = int(ip[i:j])
       list.append(ip[j+1 : j+1+length])
       i = j + 1 + length
    return list
           
       

ip = ["neet","code"]
st = encode(ip)
lt = decode(st)
print(st)
print(lt)