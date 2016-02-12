'''
Created by:		Magi Joy S. Larin
				2013-56443
Subject:		CMSC 128 AB-3L
Date Created:	February 13, 2016
Description:	Performs the following: 
					numToWords === Accepts a whole number from 0 to 1000000 and prints it in word form
					wordsToNum === Accepts a number in word form (from 0 to 1000000) and returns it in numerical form (Input must be in lowercase)
					wordsToCurrency === Accepts a number in word form (from 0 to 1000000) and any of the following: JPY, PHP, USD. The function returns the number to its numerical form with a prefix of the currency
					numberDelimited === Accepts a number from 0 to 1000000, a delimiter to be used (single character only), and the number of jumps when the delimiter will appear (from right most going to left most digit)
'''

def numToWords():
	num = int(input("Number to Words: "))
	if(num>1000000) or (num<0): 	#num is greater than one million or less than 0
		words = "ERROR!!"
	elif num==0:					#num is zero
		words = "zero"
	elif(num<20):					#num is less than twenty
		if(num<10):
			words = getword(num)
		else:
			words = gettens(num)
	else:
		words = ""
		ones = 0
		for i in range(0,len(str(num))): #[0,7)   limit is million
			x = int(num % 10)
			num = num/10
			if (i==0) or (i==3):
				ones=x
			if(num>0) or (x>0):
				word = str(getword(x))
				if(i==2) or (i==5):		#digit is in hundred
					if(x!=0):
						words = word + ' hundred ' + words
				elif i==3:				#digit is in thousand
					if(int(num%10) == 1) or (int(num%10) != 0) or (int((num/10)%10) != 0):
						words = 'thousand ' + words
					elif(x!=0):
						words = word + ' ' + "thousand" + ' ' + words
				elif i==6:				#digit is in million
					if(x!=0):
						words = word + ' ' + "million" + ' ' + words
				elif(i==1) or (i==4):	#digit is in tens or ones
					if(x==1) and (i==1):
						words = str(gettens(10+ones))
					elif(x==1) and (i==4):
						words = str(gettens(10+ones)) + ' ' + words
					elif(x!=0):
						words = str(gettwenty(x)) + ' ' + words
				else:	
					if(x!=0):
						words = word + ' ' + words
	print(words)
			
def getword(num):	#ones in words
	if num == 1:
		return("one")
	elif num == 2:
		return("two")
	elif num == 3:
		return("three")
	elif num == 4:
		return("four")
	elif num == 5:
		return("five")
	elif num == 6:
		return("six")
	elif num == 7:
		return("seven")
	elif num==8:
		return("eight")
	elif num==9:
		return("nine")
	else:
		return
		
def gettwenty(num):		#tens-ty in words
	if num == 2:
		return("twenty")
	elif num==3:
		return("thirty")
	elif num==4:
		return("forty")
	elif num==5:
		return("fifty")
	elif num==6:
		return("sixty")
	elif num==7:
		return("seventy")
	elif num==8:
		return("eighty")
	elif num==9:
		return("ninety")
	else:
		return
		
def gettens(num):		#teens in words
	if num==10:
		return("ten")
	elif num==11:
		return("eleven")
	elif num==12:
		return("twelve")
	elif num==13:
		return("thirteen")
	elif num==14:
		return("fourteen")
	elif num==15:
		return("fifteen")
	elif num==16:
		return("sixteen")
	elif num==17:
		return("seventeen")
	elif num==18:
		return("eighteen")
	elif num==19:
		return("nineteen")
	else:
		return
		
def wordsToNum(words):
	num = 0
	temp = 0
	for word in words.split(' ', words.count(' ')): #seperate by space
		i = getNum(word)
		if(i==0):
			num = 0
		if(word == "million"):
			num = temp*1000000
			temp = 0
		elif(word == "thousand"):
			num = num + (temp*1000)
			temp = 0
		else:
			if(word == "hundred"):
				temp = temp*100
			else:
				temp += i
	num += temp
	return(str(num))
			
def getNum(word):
	if word=="zero":
		return 0
	elif word=="one":
		return 1
	elif word=="two":
		return 2
	elif word=="three":
		return 3
	elif word=="four":
		return 4
	elif word=="five":
		return 5
	elif word=="six":
		return 6
	elif word=="seven":
		return 7
	elif word=="eight":
		return 8
	elif word=="nine":
		return 9
	elif word=="ten":
		return 10
	elif word=="eleven":
		return 11
	elif word=="twelve":
		return 12
	elif word=="thirteen":
		return 13
	elif word=="fourteen":
		return 14
	elif word=="fifteen":
		return 15
	elif word=="sixteen":
		return 16
	elif word=="seventeen":
		return 17
	elif word=="eighteen":
		return 18
	elif word=="nineteen":
		return 19
	elif word=="twenty":
		return 20
	elif word=="thirty":
		return 30
	elif word=="forty":
		return 40
	elif word=="fifty":
		return 50
	elif word=="sixty":
		return 60
	elif word=="seventy":
		return 70
	elif word=="eighty":
		return 80
	elif word=="ninety":
		return 90

def wordsToCurrency():
	words = input("Words to Currency: ")	
	conv = ''
	i=0
	for word in words.split(',', 1): 	#seperate by comma
		temp = word[1:len(word)-1]		#get word without "'"
		if(i==0):
			conv = wordsToNum(str(temp))
		else:
			conv = temp + conv
		i+=1
	print(conv)

def numberDelimited():
	words = input("Number Delimiter: ")
	i = 0		#counter
	num=''		#number
	temp = 0	#set to 1 if delimiter is a comma
	delimiter=''
	end = ''	#number of jumps from the right	to left
	for word in  words.split(',', words.count(',')):	#seperate by commas
		if(i==0):
			num = word
		elif(temp == 1):	#set delimiter to comma
			delimiter = ','
			temp = 0
		elif(word=="'"):	#delimiter is comma
			temp = 1
		elif(i==1):			#store delimiter
			delimiter = word[1]
		else:				#number of jumps
			end = word
		i+=1
	jump = len(num) - int(end)	#jump position
	print(num[0:jump] + delimiter + num[jump:len(num)])

numToWords()
print(wordsToNum(input("Enter words to number: ")))
wordsToCurrency()
numberDelimited()