'''
Функция принимает на вход:
(1) путь до файла в который будут записаны поверх цифры
(2) с какой цифры
(3) по какую цифру будет записано
(4) путь до файла в поторый будет записан алфавит
! если этих файлов нет, то они будут созданы в соответствии с указанными путями
 '''
# example: python gener_test.py ~/BIOINF_2020/python_2/test_2.txt 1 30 ~/BIOINF_2020/python_2/test_1.txt

import sys
import string

path_to_file_1 = str(sys.argv[1])
x = int(sys.argv[2])
y = int(sys.argv[3]) + 1

path_to_file_2 = str(sys.argv[4])

with open(path_to_file_1, "w") as file_1, open(path_to_file_2, "w") as file_2:

    list_of_num = [str(i) for i in range(x,y)]
    file_1.write('\n'.join(list_of_num))

    file_2.write('\n'.join(string.ascii_letters))
