t=['0']*6
pref=['0']*6
try:
	file1=open('x.txt','r')
	file1.close()
	file1=open('x.txt','w')
	file1.write('Dont delete this\n')
	file=open('pref.txt','r')
	pref=[i[0:-1] for i in file.readlines()]
	file.close()
	t[int(input('Enter the number of the required config\n(1)Path to the folder of your excel files\n(2)Number of significant figures\n(3)Colour of data points\n(4)Colour of the line\n(5)Error type\n\n'))]='1'
except IOError:
	file1=open('x.txt','w')
	file1.write('Dont delete this\n')
	t=['1']*6
if t[1]=='1':
	pref[0]=(str(input('Enter the path to the folder of your excel files : ')))
if t[2]=='1':
	pref[1]=(str(input('Number of significant figures : ')).lower())
if t[3]=='1':
	pref[2]=(str(input('Colour of data points : ')).lower())
if t[4]=='1':
	pref[3]=(str(input('Colour of the line : ')).lower())
if t[5]=='1':
	pref[4]=(str(input('Standard Deviation or Standard Deviation Error(SD/SDE) : ')).lower())
if str(input('Save Changes?(Y/N):')).lower()=='y':
	file=open('pref.txt','w')
	file.writelines([i+'\n' for i in pref])
	file.close()
file1.close()
