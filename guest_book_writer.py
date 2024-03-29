from pathlib import Path

path : str = Path('guest.txt')
user_name : str = ''
contents : str = ''

while(user_name != 'quit'):
    user_name = input("Please enter your name: ")
    if user_name != 'quit':
        contents += user_name + '\n'

path.write_text(contents)