import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

'''
print('Meu diretório do projeto é:' , BASE_DIR)
print('Meu diretório dos dados é:' , DATA_DIR)
'''

files_names = os.lisdir(DATA_DIR)
print(files_names)


