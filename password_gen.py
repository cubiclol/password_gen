import random 

save_path = 'D:/'
symbols = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = int( input( 'Сколько паролей хочешь?: ' ))
lenght = int( input( 'Какая длина пароля требуется?: ' ))

for x in range( number ):
	password = ''

	for i in range( lenght ):
		password += random.choice( symbols )

	print( password )
	file = open( save_path + 'password.txt', 'a' )
	file.write( '\n' + password )
	file.close()


	
import os
os.system( 'pause' )