def main():
	for first_number in range(1,99999):

		number_convert = bin(first_number)[2:]
		count_1 = 0
		for i in number_convert:
			if i == "1":
				count_1 +=1

		if count_1 % 2 != 0:
			number_convert += "10"
		else:
			number_convert += "00"

		if int(number_convert,2)>150:
			print("1 Задача",int(number_convert,2))
			break


	mas = []
	for number in range(1,100):
		last_number = int(f"{number % 4}{number % 3}{number % 2}")

		if last_number == 101:
			mas.append(number)
	mas.sort()
	print("2 Задача",mas[-1])

	for first_number in range(1,99999):

		number_convert = bin(first_number)[2:]
		count_1 = 0
		for i in number_convert:
			if i == "1":
				count_1 +=1

		number_convert+=number_convert[-1]

		if count_1 % 2 != 0:
			number_convert += "1"
			count_1+=1
		else:
			number_convert += "0"

		if number_convert[-2] != "0":
			count_1+=1

		if count_1 % 2 != 0:
			number_convert += "1"
		else:
			number_convert += "0"

		if int(number_convert,2)>130:
			print("3 Задача",int(number_convert,2))
			break

	for number in range (1, 255):
		last_number = number ^ 255
		if last_number - number == 99:
			print("4 Задача",number)


	mas = []
	for first_number in range(4,100):

		number_convert = str(bin(first_number)[2:])
		if first_number % 5 == 0:
			number_convert+=number_convert[-3]+number_convert[-2]+number_convert[-1]
		else:
			number_convert+=str(bin((first_number % 5)*5)[2:])
		if int(number_convert,2)<100:
			mas.append(first_number)
	mas.sort()
	print("5 Задача",mas[-1])

	def convert_integer_3(num):
		new = ''
		while num > 0:
		    num, remainder = divmod(num, 3)
		    new = str(remainder) + new
		return new
	mas = []
	for first_number in range(1,99999):

		number_convert = convert_integer_3(first_number)

		if first_number % 3 == 0:
			number_convert+=number_convert[-2]+number_convert[-1]
		else:
			number_convert+=convert_integer_3((first_number % 3)*5)

		if int(number_convert,3)>133:
			mas.append(int(number_convert,3))
	mas.sort()
	print("6 Задача",mas[0])

if __name__ == "__main__":
	main()

#	for number in range (1, 255):
#		next_number = str(bin(number)[2:])
#		if len(next_number) < 8:
#			next_number = "0"*(8-len(next_number))+next_number
#		last_number = ""
#		for i in next_number:
#			if i == "1":
#				last_number+="0"
#			else:
#				last_number+="1"
#		if int(last_number, 2) - number == 99:
#			print("4 Задача",number)
