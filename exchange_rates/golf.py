I,M=input,max
while a:=int(I()):
 C,U=1e5,0
 while a:(U:=M(C/(r:=eval(I()))*97//100,U),C:=M(U*r*97//100,C));a-=1
 print(f'{C/100:.2f}')
