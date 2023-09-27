from neu_s_2.Method.train import trainNS2

def demo():
    dataset_folder_path = '../colmap-manage/output/3vjia_simple/ingp/'

    trainNS2(dataset_folder_path)
    return True
