import sys
sys.path.append('../colmap-manage/')

import os

from colmap_manage.Module.dataset_manager import DatasetManager

home = os.environ['HOME']
# 小妖怪头
shape_id = '003fe719725150960b14cdd6644afe5533743ef63d3767c495ab76a6384a9b2f'
# 女人上半身
shape_id = '017c6e8b81a17c298baf2aba24fd62fa5a992ba8346bc86b2b5008caf1478873'
# 长发男人头
shape_id = '0228c5cdba8393cd4d947ac2e915f769f684c73b87e6939c129611ba665cafcb'

data_folder_path = home + '/chLi/Dataset/pixel_align/' + shape_id + '/colmap/'

dataset_folder_path = home + '/chLi/Dataset/pixel_align/' + shape_id + '/'
method_dict = {
    'aabb_scale': 1,
}
is_copy = True
print_progress = True

DatasetManager().generateDataset(
    'ns2',
    data_folder_path,
    dataset_folder_path,
    method_dict,
    is_copy,
    print_progress,
)
