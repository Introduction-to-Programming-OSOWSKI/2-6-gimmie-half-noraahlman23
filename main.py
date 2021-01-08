def gimmieHalf(x,y):
    if y % x == 0 and y / x == 2:
        return True
    else: 
        return False

print (gimmieHalf(5,10))