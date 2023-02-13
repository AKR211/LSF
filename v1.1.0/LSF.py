import matplotlib.pyplot as plt
from pandas import read_excel,isnull
from math import log10, floor

import os
path = os.path.normpath(os.getcwd())
w=path.split(os.sep)
w.pop()
w.append("preferences")
w.append("pref.txt")

file=open('\\'.join(w),'r')
a=file.readlines()
pref=[i[0:-1] for i in a]
file.close()

def round_(x):
	if x==0:
		return float(0)
	return round(x, -int(floor(log10(abs(x)))) + (int( pref[1])-1))

m=str(input('No. of readings or excel file: ')).split(',')
if m==['']:
	file1=open('geret.txt','r')
	mem=file1.readlines()
	xandy=[i[0:-1] for i in mem]
	file1.close()
	X=xandy[0].split(',')
	Y=xandy[1].split(',')
	print('X = '+'['+','.join(X)+']')
	print('Y = '+'['+','.join(Y)+']')
	X=[float(i) for i in X]
	Y=[float(i) for i in Y]
	n=len(X)
	xlb=''
	ylb=''
else:
	m.append('0')
	n,n1=m[0],int(m[1]) or 1
	print('Enter the values')
	try:
		n=int(n)
		X=eval(input('X = '))
		Y=eval(input('Y = '))
		xlb=''
		ylb=''
	except ValueError:
		xlb=str(input('X = '))
		X=[float(i) for i in read_excel(r''+ pref[0]+'\\'+n,sheet_name=n1-1)[xlb].tolist() if not isnull(i)]
		ylb=str(input('Y = '))
		Y=[float(j) for j in read_excel(r''+ pref[0]+'\\'+n,sheet_name=n1-1)[ylb].tolist() if not isnull(j)]
		n=len(X)

file1=open('geret.txt','w')
file1.writelines([','.join(str(v) for v in X)+'\n',','.join(str(u) for u in Y)+'\n'])
file1.close()
x=sum(X)
y=sum(Y)

X2=[x1**2 for x1 in X]
x2=sum(X2)

XY=[X[i]*Y[i] for i in range(0,len(X))]
xy=sum(XY)

dlt=((n*x2)-(x**2))
a=((n*xy)-(x*y))/dlt
b=((y*x2)-(xy*x))/dlt

D=[Y[j]-(a*X[j]+b) for j in range(0,len(X))]
D2=[d1**2 for d1 in D]

d=sum(D)
d2=sum(D2)

if  pref[4]=='sde':
	Erry=(d2/(n**2-2*n))**0.5
if  pref[4]=='sd':
	Erry=(d2/(n-2))**0.5
Errb=Erry*((x2/dlt)**0.5)
Erra=Erry*((n/dlt)**0.5)
print()
print('a = '+str(a)+' + '+str(Erra))
print('b = '+str(b)+' + '+str(Errb))

a=round_(a)
b=round_(b)
Erra=round_(Erra)
Errb=round_(Errb)
plt.title(input('Title : '))
plt.xlabel(input('x-axis : ') or xlb)
plt.ylabel(input('y-axis : ') or ylb)


s=(max(X)-min(X))/10
t=(max(Y)-min(Y))/10
plt.plot(X,Y,'.',c= pref[2])
plt.plot([min(X)-s,max(X)+s],[a*(min(X)-s)+b,a*(max(X)+s)+b],c= pref[3])
ymax=max(Y)+t
ymin=min(Y)-t
plt.axis(ymin=min(Y)-t, ymax=max(Y)+2*t+(ymax-ymin)/4, xmin=min(X)-s, xmax=max(X)+s)
plt.text(min(X)-3*s/5, ymax, '$\chi^2%.2f$'+'/ndf  =  '+str(round_(d2))+' / '+str(n-2)+'\na  =  '+str(a)+' '+'$\pm$'+' '+str(Erra)+'\nb  =  '+str(b)+' '+'$\pm$'+' '+str(Errb), fontsize = 15, bbox=dict(facecolor = 'white', alpha = 1))

plt.show()
input()