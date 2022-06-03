from genericpath import exists
import os
import sys
import subprocess

# fileDir = os.path.dirname(os.path.realpath('author.py'))
# print(fileDir)
# file = open(fileDir + '/tekst.txt')
# def try_utf8(data):
#     "Returns a Unicode object on success, or None on failure"
#     try:
#        return data.decode('utf-8')
#     except UnicodeDecodeError:
#        return None

# file = open('precode.py', "r", encoding="utf-8")
# data = file.read()
# print(type(data))
# if "def print_contact():" in data:
#     print("удалите")

# for codec in codecs:
#     with open("author.py", "r", encoding="utf-8") as file:
#         text = file.read()
#     print(codec.rjust(12), "|", text)

# def test_mike_out(capfd):
#     os.system('author.py')
#     out, err = capfd.readouterr()
#     out2 = out.split('\n')
#     print(out2)

os.system('author.py')
# print(type(new))
output = subprocess.check_output(['python.exe', 'author.py'], encoding='utf-8')
print(output)

