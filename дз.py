def main():
	print("задача 1")
	with open("17-370.txt", "r") as F:
		mas = F.readlines()

	minmas = []
	pr = 0
	for Snumber in mas:
		number = int(Snumber)
		if ((number > 99 and number < 1000) or (number > -1000 and number < -99)) and (number % 10 == 3):
			minmas.append(number)
	nmin = min(minmas)
	minmas = []
	for i in range(1,len(mas)):
		FN = int(mas[i-1])
		SN = int(mas[i])
		if (FN > 999 and FN < 10000) or (FN > -10000 and FN < -999):
			CF = True
		else:
			CF = False
		if (SN > 999 and SN < 10000) or (SN > -10000 and SN < -999):
			SF = True
		else:
			SF = False
		if CF != SF:
			if ((FN**2) + (SN**2)) % nmin == 0:
				pr+=1
				minmas.append((FN**2) + (SN**2))
	pmin = min(minmas)
	print(pr,pmin)

	print("задача 2")

	def convert_integer(num):
		new = ''
		while num > 0:
		    num, remainder = divmod(num, 3)
		    new = str(remainder) + new
		return new
	with open("17-370.txt", "r") as F:
		mas = F.readlines()

	nmas = []
	pr = 0
	for Snumber in mas:
		number = int(Snumber)
		if (number > 99 and number < 1000):
			number3 = convert_integer(number)
			rnumber3 = number3[::-1]
			if number3 == rnumber3:
				nmas.append(number)
	nmax = max(nmas)
	nmas = []
	for i in range(1,len(mas)):
		FN = int(mas[i-1])
		SN = int(mas[i])
		if (FN > 999 and FN < 10000) or (FN > -10000 and FN < -999):
			CF = True
		else:
			CF = False
		if (SN > 999 and SN < 10000) or (SN > -10000 and SN < -999):
			SF = True
		else:
			SF = False
		if CF != SF:
			if ((FN**2) + (SN**2)) % nmax == 0:
				pr+=1
				nmas.append((FN**2) + (SN**2))
	pmin = min(nmas)
	print(pr,pmin)

if __name__ == "__main__":
	main()

