R=-3
P= 12**0
N=21
M=((N-1)//P)*(R+R)
print(f'M:{M} N:{N} P:{P} R:{R}')
O=M-(P+1)
R=M+O-R
P= (N % 3) + (O-R)
N=(N+1) + R +P+O
M=M+N+O+P+R
print(f'M:{M} N:{N} O:{O} P:{P} R:{R}')

