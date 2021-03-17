vaars=[1,2,3,4,5,6,7,8,9]
varia=str(vaars)
for x in vaars:
    if x>1 and x<4:
        print ('ses')
        continue
    print (x)

    if x<8 and x>4:
        print ('ses2')
        continue
    print (x)