# NeuS2

## Source

```bash
https://github.com/19reborn/NeuS2
```

## Requirements

```bash
gcc-11 & g++-11
cuda-12.2
optix-7.5.0
```

and set

```bash
~/.zshrc
->
export OptiX_INSTALL_DIR=$HOME/NVIDIA-OptiX-SDK-8.0.0-linux64-x86_64/
```

## Install

```bash
conda create -n ns2 python=3.9
conda activate ns2
./setup.sh
```

## Run

```bash
python convert.py
python demo.py
```

## Enjoy it~
