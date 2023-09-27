from neu_s_2.Method.cmd import runCMD

def trainNS2(dataset_folder_path):
    cmd = 'cd ../ns2/ && ./build/testbed' + \
        ' --scene ' + dataset_folder_path

    if not runCMD(cmd, True):
        print('[ERROR][train::trainNS2]')
        print('\t runCMD failed!')
        print('\t cmd:', cmd)
        return False

    return True
