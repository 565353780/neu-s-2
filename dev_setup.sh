cd ..
git clone git@github.com:565353780/colmap-manage.git
git clone --recursive https://github.com/19reborn/NeuS2 ns2

sudo apt-get install build-essential git python3-dev python3-pip libopenexr-dev libxi-dev \
	libglfw3-dev libglew-dev libomp-dev libxinerama-dev libxcursor-dev

cd colmap-manage
./dev_setup.sh

cd ../ns2
rm -rf build

pip install -r requirements.txt

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install "git+https://github.com/facebookresearch/pytorch3d.git"

cmake . -B build
cmake --build build --config RelWithDebInfo -j
