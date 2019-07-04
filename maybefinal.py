#--------------------------------------------------------------------------------------------------------------------------------------------
texttosearch1="[$host]"
print("enter new host name")
texttoreplace1=input('>')

texttosearch2="[$loc]"
print("enter new location")
texttoreplace2=input('>')

texttosearch3="[$ip1]"
print("enter ntp ip address 1")
texttoreplace3=input('>')

texttosearch4="[$ip2]"
print("enter ntp ip address 2")
texttoreplace4=input('>')

texttosearch5="[$host1]"
print("Enter side host-1 description")
texttoreplace5=input(">")

texttosearch6="[$host2]"
print("Enter side host-2 description")
texttoreplace6=input(">")


texttosearch7="[$ip3]"
print("Enter loopback-1 ip")
texttoreplace7=input(">")


texttosearch8="[$ip4]"
print("Enter system ip")
texttoreplace8=input(">")

texttosearch14="[$mpls1]"
print("Enter MPLS-1 path")
texttoreplace14=input(">")

texttosearch15="[$mpls2]"
print("Enter MPLS-2 path")
texttoreplace15=input(">")


texttosearch9="[$hhost]"
texttosearch10="[$hhost1]"
texttosearch11="[$hhost2]"
texttosearch12="[$ip31]"
texttosearch13="[$ip41]"

#--------------------------------------------------------------------------------------------------------------------------------------------

A=list(texttoreplace1)
B=list(texttoreplace5)
C=list(texttoreplace6)
for i in range(0,2):
    A.remove('_')
    B.remove('_')
    C.remove('_')
A="".join(A)
B="".join(B)
C="".join(C)


#--------------------------------------------------------------------------------------------------------------------------------------------
M=list(texttoreplace7)
for i in range(0,len(M)-1):
    if M[i]=='/':
        q=i
b=[]
for d in range(0,q):
    b=b+[M[d]]
MM="".join(b)
#--------------------------------------------------------------------------------------------------------------------------------------------
N=list(texttoreplace8)
for z in range(0,len(N)-1):
    if N[z]=='/':
        flag=z
V=[]
for d in range(0,flag):
    V=V+[N[d]]
NN="".join(V)

#--------------------------------------------------------------------------------------------------------------------------------------------


file=open("config1.txt","r+")
f1=open("yoyo.txt","w+")
for line in file.readlines():
    if ((texttosearch1 in line) or (texttosearch2 in line)or (texttosearch3 in line) or (texttosearch4 in line)or (texttosearch5 in line)or (texttosearch6 in line)or (texttosearch7 in line)or (texttosearch8 in line)or (texttosearch9 in line)or (texttosearch10 in line)or (texttosearch11 in line) or (texttosearch12 in line) or (texttosearch13 in line) or (texttosearch14 in line) or (texttosearch15 in line)):
        m=line.replace( texttosearch1, texttoreplace1 )
        m=m.replace( texttosearch5, texttoreplace5 )
        m=m.replace( texttosearch2, texttoreplace2 ) 
        m=m.replace( texttosearch3, texttoreplace3 ) 
        m=m.replace( texttosearch4, texttoreplace4 ) 
        m=m.replace( texttosearch6, texttoreplace6 ) 
        m=m.replace( texttosearch7, texttoreplace7 ) 
        m=m.replace( texttosearch8, texttoreplace8 ) 
        m=m.replace( texttosearch9, A ) 
        m=m.replace( texttosearch10, B ) 
        m=m.replace( texttosearch11, C )
        m=m.replace( texttosearch12, MM)
        m=m.replace( texttosearch13, NN)
        m=m.replace( texttosearch14, texttoreplace14)
        m=m.replace( texttosearch15, texttoreplace15)
        f1.write(m)
    else:
        f1.write(line)

#--------------------------------------------------------------------------------------------------------------------------------------------
input("press any key to exit")
file.close()
f1.close()
#--------------------------------------------------------------------------------------------------------------------------------------------
