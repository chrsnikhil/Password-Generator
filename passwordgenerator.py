import random
import string
lst_num=[1,2,3,4,5,6,7,8,9,]
lst_lletters = list(string.ascii_lowercase) # lowercase letters
lst_uletters = list(string.ascii_uppercase) # uppercase letters
lst_splch = ['!', '@', '#', '$', '%', '^', '&', '*']#spccial characters

n=int(input("Enter the number of Numbers in your password"))
lst=[]
while len(lst)<=n-1:#To take random numbers
    element=random.choice(lst_num)
    lst.append(element)
tupl=tuple(lst)
tup = ''.join(map(str,tupl))
lst1=[]
n1=int(input("Enter the number of upper case letters in your password"))
while len(lst1)<=n1-1:#To take random uppercase letters
    ele=random.choice(lst_uletters)
    lst1.append(ele)
tup1=tuple(lst1)
tup1=''.join(map(str,tup1))
lst2=[]
n2=int(input("Enter the number of lowercase letters"))
while len(lst2)<=n2-1:#To take random lowercase letters
    ele=random.choice(lst_lletters)
    lst2.append(ele)
tup2=tuple(lst2)
tupletters=''.join(map(str,tup2))
lst3=[]
n3=int(input("Enter the number of special characters"))
while len(lst3)<=n3-1:#To take random special characters
    ele=random.choice(lst_splch)
    lst3.append(ele)
tup3=tuple(lst3)
tupletters3=''.join(map(str,tup3))
lst_finalpassword=[]
lst_finalpassword.append(tup)
lst_finalpassword.append(tup1)
lst_finalpassword.append(tupletters)
lst_finalpassword.append(tupletters3)
tuple_finalpassword=tuple(lst_finalpassword)
password=''.join(map(str,tuple_finalpassword))
print(password)


