#Puzzle #7
#Open a file.
f=open('fortunes.txt', 'r') #'fortunes.txt' = the file path 'r' = read only parameter
while (True):
        #Read a line.
        if line =="":
                print ("******DONE******")
                break
        if line =="\n"
                print ("***EMPTY LINE***")
        #Print other lines.
        stripped = line.strip()
        print ("******LINE******")
        print (stripped)
