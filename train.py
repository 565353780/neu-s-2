import os

from neu_s_2.Method.train import trainNS2

dataset_folder_path = os.environ['HOME'] + '/chLi/Dataset/GS/haizei_1/'

trainNS2(dataset_folder_path + 'ns2/')
