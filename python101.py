#Python101
var1 = 42
var2 = "dog"
print("\n") #"\n" is used to add a new line
print("Variable#1 says %d, and Variable#2 says %s" % (var1, var2))
print("%d, %s, %d" %(var1, var2, var1))
y = ""
for x in (2,3,4,5):
        print("We're on time %d" % (x))
for x in ("dog", "cat", "hippo", "moose"):
        print("We're on time %s" %(x))
        y=y+x+ " "
        print(y)
y = 0
for x in (1,2,3):
        y=y+x
print(y)
