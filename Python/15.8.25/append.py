p=open("E:/xiics1st2024-25/College 25-26/Python/15.8.25/pratima.txt","a")
p.write("\n Ami sir next cls e valo na korle barite case deben.")
p.close()
p=open("E:/xiics1st2024-25/College 25-26/Python/15.8.25/pratima.txt","r")
for i in p.readlines():
    print(i,end='')
#print(p.read())
p.close()