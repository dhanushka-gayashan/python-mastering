user_name = input('Enter your name: ')

my_file = open('data.txt', 'w')

my_file.write(user_name)

my_file.close()