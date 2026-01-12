cd ..
git clone git@github.com:565353780/colmap-manage.git
git clone https://github.com/facebookresearch/pytorch3d.git

conda install cmake -y

pip install ninja

conda install -c conda-forge pkg-config xorg-libxrandr \
  xorg-libxinerama xorg-libxcursor xorg-libxi glew mesalib -y
conda install -c anaconda mesa-libgl-cos6-x86_64 -y
conda install -c menpo glfw3 -y

#if [ !f "${CONDA_PREFIX}/lib/libGL.so" ]; then
#  ln -s ${CONDA_PREFIX}/lib/libGL.so.1 ${CONDA_PREFIX}/lib/libGL.so
#fi

pip install torch torchvision torchaudio \
  --index-url https://download.pytorch.org/whl/cu124

pip install commentjson imageio numpy pybind11 scipy \
  tqdm opencv-python trimesh tensorboard

cd pytorch3d
python setup.py install

cd ../colmap-manage
./dev_setup.sh

cd ../neu-s-2
rm -rf build

mkdir build
cd build

PKG_CONFIG_PATH="$CONDA_PREFIX/lib/pkgconfig:$PKG_CONFIG_PATH" \
  cmake ..

make -j
