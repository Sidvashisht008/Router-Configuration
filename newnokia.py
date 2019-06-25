from string import Template
f=open("foo.txt","r+")
f1=open("yo.txt","w+")
                                                                 
print("Enter new host name")                                                #New host name
texttoreplace=input('>')

print("Enter new location")                                                 #New location name
texttoreplace1=input('>')


print("Enter new ip address 1")                                             #new ip address
texttoreplace2=input('>')


print("Enter new ip address2")                                              #new ip address 2
texttoreplace3=input('>')

                                                        
print("Enter 1st port description")                                         #1st port description
texttoreplace4=input('>')

                                                        
print("Enter 2nd port description")                                         #2nd port description
texttoreplace5=input('>')

                                                     
print("Enter loopback-1 ip address")                                        #loopback ip address
texttoreplace6=input('>')

                                                        
print("Enter interface-1 name")                                             #1st interface name 
texttoreplace7=input('>')

                                                                            
print("Enter interface-1 ip address")                                       #1st interface ip
texttoreplace8=input('>')

                                                        
print("Enter interface-2 name")                                             #2nd interface name
texttoreplace9=input('>')

                                                                
print("Enter interface-2 ip address")                                       #2nd interface ip
texttoreplace10=input('>')

                                                    
print("Enter system ip address")                                            #system ip address
texttoreplace11=input('>')

                                                       
print("Enter MPLS path 1")                                                  #MPLS path 1 description
texttoreplace12=input('>')

                                                       
print("Enter MPLS path 2")                                                  #MPLS path 2 description
texttoreplace13=input('>')


print("config file")                                                        #old configuration file name 
filetoSearch=input(">")

for line in f.readlines():
    c=Template(line)
    e = {}
    d=c.substitute(**e)
    f1.write(d)
f1.close()
f.close()
