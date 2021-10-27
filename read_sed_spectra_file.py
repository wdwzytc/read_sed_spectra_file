# the aim of this code is to find all .sed files in a target directory, extract the spectra data, and output to a csv file.
import os
import numpy as np
import csv


# read sed files and put them into a list
def read_sed_spectra_file(filepath= r'D:\3 杨天成 读博\1 博士学习_按时间顺序\2021-10-16 反演播种密度试验 测试\光谱\1268029_00148.sed'):
    import numpy as np
    with open(filepath) as f:
        content_text = f.read()

    this_text = putting_a_text_into_a_list(content_text)
    # print(this_text)

    # now the variable this_text contains all the information splitted.
    # this_text[24] is the first line of numeric data, this_text[1047] is the last.
    # transfer spectra information to numeric
    data_array = np.zeros((1024,4))
    for i in range(24, 1048):
        for j in range(0,4):
            data_array[i-24,j] = float(this_text[i][j])

    reflectance = data_array[:,3].transpose().tolist()
    return reflectance
    # return reflectance(%)


# split the text containing '\t' and '\n'.
# When meet a '\t', set a new element in the list. When meet a '\n', set a new list.
def putting_a_text_into_a_list(text):
    start_flag = 0
    end_flag = 0
    this_text = []
    this_line = []
    this_word = []
    for i in range(0, len(text)):
        if text[i] == '\t':
            end_flag = i
            this_word = text[start_flag: end_flag]  # not contain text[end_flag]
            this_line.append(this_word)
            start_flag = i + 1

        if text[i] == '\n':
            end_flag = i
            this_word = text[start_flag: end_flag]  # not contain text[end_flag]
            this_line.append(this_word)
            this_text.append(this_line)
            this_line = []
            start_flag = i + 1

        end_flag = end_flag + 1

    return this_text

target_directory = r'C:\Users\ytc\Desktop\test folder'
for dirpath_dirnames_filenames in os.walk(target_directory):
    # 遍历文件夹
    exist_sed_file = False
    data_for_this_folder = []
    for file_name in dirpath_dirnames_filenames[2]:
        # 遍历文件夹中的所有文件，寻找.sed文件
        if os.path.splitext(file_name)[1] == '.sed':
            exist_sed_file = True
            # 用之前的函数读取数据read_sed_spectra_file()，然后把数据合并
            data_for_one_file = read_sed_spectra_file(filepath=os.path.join(dirpath_dirnames_filenames[0],file_name))
            data_for_this_folder.append([file_name] + data_for_one_file)
    # 如果文件夹里没有“Collection_of_sed_spectra_data_in_this_folder.csv”，就创建一个
    if (exist_sed_file == True) and (not "Collection_of_sed_spectra_data_in_this_folder.csv" in dirpath_dirnames_filenames[2]):
        csv_filename = os.path.join(dirpath_dirnames_filenames[0], "Collection_of_sed_spectra_data_in_this_folder.csv")
        with open(csv_filename, 'w', newline='') as csvfile:
            csv.writer(csvfile, delimiter=',').writerows(data_for_this_folder)


