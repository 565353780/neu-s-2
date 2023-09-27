import os
import shutil

from neu_s_2.Method.cmd import runCMD


def trainNS2(dataset_folder_path):
    dataset_name = dataset_folder_path.split('/ns2/')[0].split('/')[-1]

    if os.path.exists(dataset_folder_path + 'output/'):
        shutil.rmtree(dataset_folder_path + 'output/')
    if os.path.exists('../neu-s-2/output/' + dataset_name + '/'):
        shutil.rmtree('../neu-s-2/output/' + dataset_name + '/')

    cmd = 'cd ../ns2 && ./build/testbed' + \
        ' --scene ' + dataset_folder_path + \
        ' --config ' + '../ns2/configs/nerf/base.json'

    if not runCMD(cmd, True):
        print('[ERROR][train::trainNS2]')
        print('\t runCMD failed!')
        print('\t cmd:', cmd)
        shutil.move(dataset_folder_path + 'output/',
                    '../neu-s-2/output/' + dataset_name)
        return False

    shutil.move(dataset_folder_path + 'output/',
                '../neu-s-2/output/' + dataset_name)

    return True
