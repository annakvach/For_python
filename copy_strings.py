import sys
import os

len_sys_argv = len(sys.argv[1:])

path_to_file_1 = sys.argv[1]
path_to_file_2 = sys.argv[2]

if len_sys_argv == 4:

    int_1 = int(sys.argv[3])
    int_2 = int(sys.argv[4])

    list_of_strings = list(range(int_1 - 1, int_2))

    with open(path_to_file_1, "r") as file_1, open(path_to_file_2, "a") as file_2:
        strings = file_1.readlines()
        file_2.write("\n") # чтобы не было нахлеста на последнюю строку
        for i in list_of_strings:
            file_2.write(strings[i])

elif len_sys_argv == 2:

    with open(path_to_file_1, "r") as file_1, open(path_to_file_2, "a") as file_2:
        strings = file_1.readlines()
        file_2.write("\n") # чтобы не было нахлеста на последнюю строку
        for j in range(len(strings)):
            file_2.write(strings[j])



