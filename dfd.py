def date(n):
	str=n
	lst=str.split()
	year=lst[2]
	print (year)
	year1=int(year)
	if year1<1999:
		considerd=year1-1900
	else:
		considerd=year1-2000+100
	print (considerd)
	quotient= considerd//4
	print (quotient)
	month=lst[1]

	def code(mon):
		if mon=='jan':
			return 2
		elif mon=='feb':
			return 5

		elif mon=='mar':
			return 5

		elif mon=='apr':
			return 1

		elif mon=='may':
			return 3

		elif mon=='jun':
			return 6

		elif mon=='jul':
			return 1

		elif mon=='aug':
			return 4

		elif mon=='sep':
			return 7

		elif mon=='otb':
			return 2

		elif mon=='nov':
			return 5

		elif mon=='dec':
			return 7

	moncode=code(lst[1])
	print (moncode)
	dat1=lst[0]
	dat=int(dat1)
	print (dat)
	total=considerd+quotient+moncode+dat
	print (total)

	def leapyr(n):
	    if n%4==0:
		    if (n%400==0 or n%100!=0):
			    print (n, " is a leap year.")
			    newtotal=total-1
			    print (newtotal)
			    return newtotal
		    else:
			    print (n, " is not a leap year")
			    newtotal=total
			    print(newtotal)
			    return newtotal
	    else:
		    print (n, " is not a leap year")
		    newtotal=total
		    print(newtotal)
		    return newtotal
	total_ret=leapyr(year1)
	weekcode=total_ret%7
	print (weekcode)
	if weekcode==0:
		print("its friday")
	elif weekcode==1:
		print("its saturday")
	elif weekcode==2:
		print("its sunday")
	elif weekcode==3:
		print("its monday")
	elif weekcode==4:
		print("its tuesday")
	elif weekcode==5:
		print("its wednesday")
	elif weekcode==6:
		print("its thursday")
