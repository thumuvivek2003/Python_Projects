#Developed By Vivek
name = "Vivek"
Name = name
Sym = "**"
Sym2 = "__"
ll = 5


from time import sleep
sleepvalue = 0.05
Name = Name.upper()
Name2 = ""
Letter = []
def check(i):
	if(i=='1'):
		return 'a'
	elif(i=='2'):
		return 'b'
	elif(i=='3'):
		return 'c'
	elif(i=='4'):
		return 'd'
	elif(i=='5'):
		return 'e'
	elif(i=='6'):
		return 'f'
	elif(i=='7'):
		return 'g'
	elif(i=='8'):
		return 'h'
	elif(i=='9'):
		return 'k'
	elif(i=='0'):
		return 'O'
	elif(i==' '):
		return 's'
	else:
		return i

start = 0
for i in Name:
	i = check(i)
	if(start%ll==0):
		l = 1
	start = start+1
	Name2 += i+"({},{},i,j) or ".format(l,l+4)
	l += 6
def p():
	print(Sym,end="")
def s(l,u,i,j):
	if(j>=l and j<=u):
		return False
def a(l,u,i,j):
	if((j>=l and j<=u) and (j==l+2 or i== 8 or (i<=2 and i+j==l+2))):
		return True
def b(l,u,i,j):
	if((j>=l and j<=u) and (i==0 or i==4 or i==8 or (i<=4 and j==u) or (i>4 and j==l) or (i<=2 and j==l) or (i>=7 and j==u))):
		return True
def c(l,u,i,j):
	if((j>=l and j<=u) and (j==u or i==0 or i==4 or i==8)):
		return True
def d(l,u,i,j):
	if((j>=l and j<=u) and (j==u or i==4 or (i<=4 and j==l))):
		return True
def e(l, u, i, j):
	if(j>=l and j<=u) and (i== 0 or i==3 or i==8 or (i<=3 and j==l) or ( i>=4 and j==u)):
		return True
def f(l,u,i,j):
	if((j>=l and j<=u) and (i==0 or i==4 or i==8 or j==l or (i>=4 and j==u))):
		return True
def g(l,u,i,j):
	if(j>=l and j<=u) and (i==0 or j==u):
		return True
def h(l,u,i,j):
	if(j>=l and j<=u) and (i==0 or i==4 or i==8 or j==l or j==u):
		return True
def k(l,u,i,j):
	if(j>=l and j<=u) and (i==0 or i==4 or i==8 or j==u or (i<4 and j==l)):
		return True
def A(l, u,i, j):
	if(j>=l and j<=u) and (j==l or j==u or i==4 or i==0):
		return True
def B(l,u,i,j):
	if(j>=l and j<=u) and (j==l or (j<=l+3 and (i==0 or i==8)) or (j<=l+2 and i==4) or j-i==l+3 or i+j==l+11 or (j==l+3 and (i==3 or i==5)) or (j==u and (i==2 or i==6))):
		return True
def C(l,u,i,j):
	if(j>=l and j<=u) and (j==l or i==0 or i==8 or (j==u and (i==1 or i==7))):
		return True
def D(l,u,i,j):
	if(j>=l and j<=u) and (j==l or (j<=l+2 and (i==0 or i==8)) or (i<=6 and i>=2 and j==u) or (j==u-1 and (i==1 or i==7))):
		return True
def E(l, u, i, j):
	if((j>=l and j<=u) and (i==0 or i==4 or i==8 or j== l)) :
		return True
def F(l,u,i,j):
	if((j>=l and j<=u) and (i==0 or i==4  or j== l)) :
		return True
def G(l, u, i, j):
	if((j>=l and j<=u) and (j==l or i==0 or i==8 or (i>=4 and j==u) or (i<=1 and j==u) or (j>=l+2 and i==4))) :
		return True
def H(l,u,i,j):
	if((j>=l and j<=u) and (j==l or j==u or i== 4)):
		return True
def I(l, u, i, j):
	if((j>=l and j<=u) and (i==0 or i==8 or j==l+2)) :
		return True
def J(l,u,i,j):
	if((j>=l and j<=u) and (i==0 or j==l+2 or (j<=l+2 and i==8) or (i==1 and (j==l or j==l+4)) or (j==l and i==7))) :
		return True
def K(l,u,i,j):
	if((j>=l and j<=u) and (j==l or (j<=u and (i+j==l+5 or j-i==l-3)) or (j==u and (i==0 or i==8)))) :
		return True
def L(l,u,i,j):
	if((j>=l and j<=u) and (i==8 or j==l or (j==u and i==7))) :
		return True
def M(l,u,i,j):
	if((j>=l and j<=u) and (i==0 or j==l or j==u or (i<=3 and j==l+2))) :
		return True
def N(l, u, i, j) :
	if((j>=l and j<=u) and (j==l or j==u or i==0)):
		return True
def O(l,u,i,j):
	if((j>=l and j<=u) and (i==0 or i==8 or j== l or j==u)):
		return True
def P(l, u, i, j):
	if((j>=l and j<=u)and (i==0 or i==4 or j==l or (i<=4 and j==u))) :
		return True
def R(l, u, i, j) :
	if((j>=l and j<=u) and (j==l or i==0 or i==4 or (i<=4 and j==u) or (i>4 and j-i==l-4))) :
		return True
def Q(l,u,i,j):
	if(j>=l and j<=u) and (i==0 or i==6 or (i<=6 and (j==l or j==u))or j-i==l-4):
		return True
def S(l, u, i, j):
	if(j>=l and j<=u) and (i== 0 or i==4 or i==8 or (i<=3 and j==l) or ( i>=4 and j==u) or (i==1 and j==u) or (i==7 and j==l)):
		return True
def T(l,u, i, j):
	if((j>=l and j<=u) and (i==0 or j==l+2 or (i<=1 and (j==l or j==u)))) :
		return True
def U(l, u, i, j):
		if((j>=l and j<=u) and (j==l or j==u or i==8)):
			return True
def V(l, u, i, j):
	if((j>=l and j<=u) and (i<=5 and (j==l or j== u)) or (i<=8 and i>=6 and (j-i==-6+l or i+j == 10+l))) :
		return True
def W(l,u,i,j):
	if((j>=l and j<=u) and (i==8 or j==l or j==u or (i>=3 and j==l+2))) :
		return True
def X(l, u, i, j):
	if(j<=u and j>=l) and (i<=2 and (j==l or j==u) or (i>=6 and (j==l or j==u)) or j-i==l-2 or i+j==u+2):
		return True
def Y(l, u, i, j):
	if((j>=l and j<=u) and (i==3 or i==8 or j==u or (i<=3 and j==l) or (i>=6 and j==l))):
		return True
def Z(l,u,i,j):
    if((j>=l and j<=u) and (i==0 or i==8 or (i>6 and j==l) or (i<2 and j==l+4) or ((i>=2 and i<=6) and i+j==l+6))):
        return True
        
        
        
        
Name2 = Name2[:-3]
fpos = []
lpos = []
def split():
    for i in range(1,len(Name2)):
        if(Name2[i]=="("):
            fpos.append(i-1)
        elif(Name2[i]==")"):
            lpos.append(i+1)
split()


def print_letters():
    l = len(lpos)
    begin = 0
    end = 0
    flag  = True
    count = 0
    while(flag):
        if(l>begin+ll) : end = ll-1
        else:
            end = l-begin-1
            flag = False
        txt = Name2[fpos[begin]:lpos[begin+end]]
        print(Sym2*((6*ll+3) ))
        print(Sym2*(6*ll+3) )
        print(Sym2*(6*ll+3) )
        for i in range(9):
            for j in range((6*ll+3) ):
                if(eval(txt)):
                    count+=1
                    print(Sym,end="",flush=True)
                else:
                    print(Sym2,end="",flush=True)
            print()
        begin += ll
        print(Sym2*(6*ll+3) )
        print(Sym2*(6*ll+3) )
        print(Sym2*(6*ll+3) )

print_letters()
