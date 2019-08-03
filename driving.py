country = input('請問你是哪國人:')
age = input('您的年齡是:')
age = int(age)

if country == '台灣':

	if age >= 18:
		print('妳可以考駕照')

	else:
		print('你還不能考駕照')

elif country == 'USA':

	if age >= 16:
		print('妳可以考駕照')
	else:
		print('你還不能考駕照')

else:
	print('您只能輸入台灣和美國')