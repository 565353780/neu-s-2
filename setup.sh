cd ..
git clone https://github.com/565353780/colmap-manage.git
git clone https://github.com/facebookresearch/pytorch3d.git

conda install cmake -y

conda install -c conda-forge xorg-libxrandr xorg-libxinerama \
  xorg-libxcursor xorg-libxi glew mesalib -y
conda install -c anaconda mesa-libgl-cos6-x86_64 -y
conda install -c menpo glfw3 -y

#if [ !f "${CONDA_PREFIX}/lib/libGL.so" ]; then
#  ln -s ${CONDA_PREFIX}/lib/libGL.so.1 ${CONDA_PREFIX}/lib/libGL.so
#fi

pip install torch torchvision torchaudio \
  --index-url https://download.pytorch.org/whl/cu124

cd pytorch3d
python setup.py install

cd ../colmap-manage
./dev_setup.sh

cd ../neu-s-2
rm -rf build

pip install commentjson imageio numpy pybind11 scipy \
  tqdm opencv-python trimesh tensorboard

cmake . -B build
cmake --build build --config RelWithDebInfo -j
