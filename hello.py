if __name__ == '__main__':
	user_info={'first_name':'','last_name':''}
	user_info['first_name']=input('Your name? ')
	user_info['last_name']=input('Your last name? ')
	print (user_info.get('first_name'))
	print (user_info.get('last_name'))
	print (user_info)
