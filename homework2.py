from pywebio.input import input as pw_input
from pywebio.output import toast

user_food = pw_input('Say your favorite food')

smile = '\U0001F601'

toast(f'Oh, I love too {user_food}, {smile}.')
