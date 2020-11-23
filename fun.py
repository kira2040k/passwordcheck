import re

def len10(password,points):
     
    if(len(password)>=10):
        points=points+3 
        return points
    else:
        return points
def len8(password,points):
    if(len(password)>=8):
        points=points+2 
        return points
    else:
        return points
def capital(password,points):
    p=re.findall('[A-Z]',password)
    p=len(p)
    p=p/2
    return points+p
def symbols(password,points):
    p=re.findall('[^a-z][^A-Z][^0-9]',password)
    p=len(p)
    return points+p

