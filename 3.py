s = input()
l_s=len(s)
r_s=""

for i in range(l_s-1,-1,-1):
    r_s+=s[i]

print("Reuslt is: ",r_s)
if(r_s==s):
    print("PALINDROME")
else:
    print("NOT PALINDROME")