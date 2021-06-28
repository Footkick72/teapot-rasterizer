data = ""
nverticies = 0
nfaces = 0
linenumber = 7000
charsinline = 0
maxchars = 100

with open("//Users/daniellong/Downloads/teapot.off.txt","r") as f:
    for line in f.readlines()[1:]:
        if charsinline == 0:
            data += str(linenumber) + " data "
        if line[:2] == "3 ":
            p = line.split()
            p = [p[1],p[2],p[3]]
            r = ",".join(p)
            data += r
            charsinline += len(r)
            nfaces += 1
        elif line[:2] == "4 ":
            p = line.split()
            p = [p[1],p[2],p[3],p[1],p[3],p[4]]
            r = ",".join(p)
            data += r
            charsinline += len(r)
            nfaces += 2
        else:
            x = list(map(lambda x: str(round(float(x),3)), line.split()))
            r = ",".join(x)
            data += r
            charsinline += len(r)
            nverticies += 1
        
        if charsinline > maxchars:
            charsinline = 0
            data += "\n"
            linenumber += 1
        else:
            data += ","
            

print(data)
print(nverticies)
print(nfaces)
