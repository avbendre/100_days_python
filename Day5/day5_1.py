#love score game
n1=input("enter your name")
n2=input("enter their name")
cn=(n1+n2).lower()

t=cn.count("t")
r=cn.count('r')
u=cn.count('u')
e=cn.count('e')
l=cn.count('l')
o=cn.count('o')
v=cn.count('v')
e=cn.count('e')

true=t+r+u+e
love=l+o+v+e


ls=str(true)+str(love)
print(ls)