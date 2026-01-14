import os
import shutil

from neu_s_2.Method.cmd import runCMD


def trainNS2(dataset_folder_path):
    if os.path.exists(dataset_folder_path + 'output/'):
        shutil.rmtree(dataset_folder_path + 'output/')

    cmd = 'cd ../neu-s-2 && ./build/testbed' + \
        ' --scene ' + dataset_folder_path + \
        ' --config ' + '../neu-s-2/configs/nerf/base.json'

    if not runCMD(cmd, True):
        print('[ERROR][train::trainNS2]')
        print('\t runCMD failed!')
        print('\t cmd:', cmd)
        return False

    return True
