"""#Pgm to print a patter
1
22
333
4444
55555
and
*
**
***
****
*****"""


def pat(num):
	x=0
	for i in range(0,num):   # outer loop to handel the number of rows
		x+=1
		for j in range(0,i+1): # inner loop to handel the number of columns
			print(x,end="")
		print("\r")		# ending line after each row	



pat(5)



def pat(num):
	x=0
	for i in range(0,num):   # outer loop to handel the number of rows
		x+=1
		for j in range(0,i+1): # inner loop to handel the number of columns
			print("*",end="")
		print("\r")		# ending line after each row	



pat(5)
