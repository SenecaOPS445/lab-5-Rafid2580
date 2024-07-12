#!/usr/bin/env python3
# Author ID: 186140216

def append_file_string(file_name, string_of_lines):
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()

def write_file_list(file_name, list_of_lines):
    f = open(file_name, 'w')
    for line in list_of_lines:
        f.write(line + '\n')
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    fr = open(file_name_read, 'r')
    lines = fr.readlines()
    fr.close()
    fw = open(file_name_write, 'w')
    for i, line in enumerate(lines, 1):
        fw.write(f"{i}: {line}")
    fw.close()

def read_file_string(file_name):
    f = open(file_name, 'r')
    content = f.read()
    f.close()
    return content

def read_file_list(file_name):
    f = open(file_name, 'r')
    content = f.readlines()
    f.close()
    # Strip the newline character from each line
    return [line.strip() for line in content]

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
