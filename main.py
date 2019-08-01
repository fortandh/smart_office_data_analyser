#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re

folder_path = r"E:\work\1238257272382\results6"
aim_file_name = "xx.csv"
group_size = 10

if __name__ == '__main__':
    # result6
    if os.path.isdir(folder_path):
        # p_0, p_1, np_0
        for config_name in os.listdir(folder_path):
            config_path = r"{}\{}".format(folder_path, config_name)
            if os.path.isdir(config_path):
                aim_file_path = r"{}\{}".format(config_path, aim_file_name)
                with open(aim_file_path, "w") as aim_file:
                    result_average_list = [0.0]*100
                    for data_file_name in os.listdir(config_path):
                        if data_file_name != aim_file_name:
                            data_file_path = r"{}\{}".format(config_path, data_file_name)
                            with open(data_file_path, "r") as data_file:
                                j = 0
                                for line in data_file:
                                    pattern = re.compile(r'(\d+),(\d+\.?\d*)')
                                    result = pattern.findall(line)
                                    if result:
                                        result = result[0]
                                        # result_average_list[int(result[0])] += float(result[1])
                                        result_average_list[j] += float(result[1])
                                        j += 1
                    for i in list(range(100)):
                        result_average_list[i] /= group_size
                    for i in list(range(100)):
                        aim_file.write("{},{}\n".format(i, result_average_list[i]))
    else:
        print("文件夹不存在！\n")

    print("All task finished.")
