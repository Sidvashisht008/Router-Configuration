#------------------------------------------------------------------------------------------------------------
texttosearch="AAAA"                                                                 
print("Enter new host name")                                                #New host name
texttoreplace=input('>')

texttosearch1="BBBB"
print("Enter new location")                                                 #New location name
texttoreplace1=input('>')

texttosearch2="0.0.0.0"
print("Enter new ip address 1")                                             #new ip address
texttoreplace2=input('>')

texttosearch3="1.1.1.1"
print("Enter new ip address2")                                              #new ip address 2
texttoreplace3=input('>')

texttosearch4="CCCC"                                                        #1st port description
print("Enter 1st port description")
texttoreplace4=input('>')

texttosearch5="DDDD"                                                        #2nd port description
print("Enter 2nd port description")
texttoreplace5=input('>')

texttosearch6="3.3.3.3"                                                     #loopback ip address
print("Enter loopback-1 ip address")
texttoreplace6=input('>')

texttosearch7="EEEE"                                                        #1st interface name 
print("Enter interface-1 name")
texttoreplace7=input('>')

texttosearch8="4.4.4.4"                                                     #1st interface ip
print("Enter interface-1 ip address")
texttoreplace8=input('>')

texttosearch9="FFFF"                                                        #2nd interface name
print("Enter interface-2 name")
texttoreplace9=input('>')

texttosearch10="5.5.5.5"                                                    #2nd interface ip
print("Enter interface-2 ip address")
texttoreplace10=input('>')

texttosearch11="6.6.6.6"                                                    #system ip address
print("Enter system ip address")
texttoreplace11=input('>')

texttosearch12="ZZZZ"                                                       #MPLS path 1 description
print("Enter MPLS path 1")
texttoreplace12=input('>')

texttosearch13="YYYY"                                                       #MPLS path 2 description
print("Enter MPLS path 2")
texttoreplace13=input('>')


print("config file")                                                        #old configuration file name 
filetoSearch=input(">")

#------------------------------------------------------------------------------------------------------------
file=open(filetoSearch,'r+')
f1=open("yoyo.txt","w+")
for line in file.readlines():
    if texttosearch in line:
        f1.write( line.replace( texttosearch, texttoreplace ) )
    elif texttosearch1 in line:  
        f1.write( line.replace( texttosearch1, texttoreplace1 ) )
    elif texttosearch2 in line:     
        f1.write( line.replace( texttosearch2, texttoreplace2 ) )
    elif texttosearch3 in line:
        f1.write( line.replace( texttosearch3, texttoreplace3 ) )
    elif texttosearch4 in line:
        f1.write( line.replace( texttosearch4, texttoreplace4 ) )
    elif texttosearch5 in line:
        f1.write( line.replace( texttosearch5, texttoreplace5 ) )
    elif texttosearch6 in line:
        f1.write( line.replace( texttosearch6, texttoreplace6 ) )
    elif texttosearch7 in line:
        f1.write( line.replace( texttosearch7, texttoreplace7 ) )
    elif texttosearch8 in line:
        f1.write( line.replace( texttosearch8, texttoreplace8 ) )
    elif texttosearch9 in line:
        f1.write( line.replace( texttosearch9, texttoreplace9 ) )
    elif texttosearch10 in line:
        f1.write( line.replace( texttosearch10, texttoreplace10 ) )
    elif texttosearch11 in line:
        f1.write( line.replace( texttosearch11, texttoreplace11 ) )
    elif texttosearch12 in line:
        f1.write( line.replace( texttosearch12, texttoreplace12 ) )
    elif texttosearch13 in line:
        f1.write( line.replace( texttosearch13, texttoreplace13 ) )
    else:
        f1.write(line)
#------------------------------------------------------------------------------------------------------------
input("press any key to exit")
file.close()
f1.close()