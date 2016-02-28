#Julius Cesar code to encrypt messages
#by Radek

Phraze = input('Type message to encrypt: ')
shiftValue = input('Enter shift value: ')

listPhraze = list(Phraze)
listLenght = len(listPhraze)
print (listLenght)

ascii = []
for ch in listPhraze:
	ascii.append(ord(ch))
print (ascii)


#ascii_list = list()
#counter = listLenght
#if counter != 0:
#	for i in range (listLenght):
#		ascii_code = ord(listPhraze(i))
#		ascii_list.append(ascii_code)
#		counter = counter - 1
#elif counter == 0:
#	print (ascii_list)

#ascii_code = ord(listPhraze)


#print(ascii_code)
