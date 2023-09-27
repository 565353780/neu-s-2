# NeuS2

## Source

```bash
https://github.com/19reborn/NeuS2
```

## Requirements

```bash
gcc-11 & g++-11
cuda-11.8
optix-7.6.0
```

and set

```bash
~/.zshrc
->
export OptiX_INSTALL_DIR=$HOME/NVIDIA-OptiX-SDK-7.6.0-linux64-x86_64/
```

## Install

```bash
conda create -n ns2 python=3.10
conda activate ns2
./setup.sh
```

## Run

```bash
python convert.py
python demo.py
```

## Enjoy it~
