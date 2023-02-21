# WSL关闭
https://zhuanlan.zhihu.com/p/468333378

在 Windows 桌面左下角搜索框输入 cmd
右键点击用管理员账号执行 cmd
依次执行如下两条命令：
net stop LxssManager
bcdedit /set hypervisorlaunchtype off

# nvcc & nvidia-smi
nvcc & nvidia-smi
nvcc 属于CUDA的编译器，将程序编译成可执行的二进制文件，nvidia-smi 全称是 NVIDIA System Management Interface ，是一种命令行实用工具，旨在帮助管理和监控NVIDIA GPU设备。

CUDA有 runtime api 和 driver api，两者都有对应的CUDA版本， nvcc --version 显示的就是前者对应的CUDA版本，而 nvidia-smi显示的是后者对应的CUDA版本。

用于支持driver api的必要文件由 GPU driver installer 安装，nvidia-smi就属于这一类API；而用于支持runtime api的必要文件是由 CUDA Toolkit installer 安装的。nvcc是与CUDA Toolkit一起安装的CUDA compiler-driver tool，它只知道它自身构建时的CUDA runtime版本，并不知道安装了什么版本的GPU driver，甚至不知道是否安装了GPU driver。

CUDA Toolkit Installer通常会集成了GPU driver Installer，如果你的CUDA均通过CUDA Tooklkit Installer来安装，那么runtime api 和 driver api的版本应该是一致的，也就是说， nvcc --version 和 nvidia-smi 显示的版本应该一样。否则，你可能使用了单独的GPU driver installer来安装GPU dirver，这样就会导致 nvidia-smi 和 nvcc --version 显示的版本不一致了。

通常，driver api的版本能向下兼容runtime api的版本，即 nvidia-smi 显示的版本大于nvcc --version 的版本通常不会出现大问题。


# check dependencies
sudo apt-get update

# install gcc
nvcc是NVIDIA提供的用于编译CUDA程序的编译器，它是基于GCC的，所以需要先安装GCC
sudo apt install gcc

# check nvidia-smi and nvcc -V
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
sudo sh cuda_11.8.0_520.61.05_linux.run

Please make sure that
 -   PATH includes /usr/local/cuda-11.8/bin
 -   LD_LIBRARY_PATH includes /usr/local/cuda-11.8/lib64, or, add /usr/local/cuda-11.8/lib64 to /etc/ld.so.conf and run ldconfig as root

 export PATH="/usr/local/cuda-11.8/bin:$PATH"
 export LD_LIBRARY_PATH="/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH"

# anaconda3 install
wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
bash Anaconda3-2022.10-Linux-x86_64.sh

export PATH="~/anaconda3/bin":$PATH
source ~/anaconda3/bin/activate

# pip
pip config set global.index-url https://pypi.douban.com/simple

# vritualenv
pip install virtualenv
pip install virtualenvwrapper

(optional?) sudo apt-get install python-dev

export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
- sudo find / -name virtualenvwrapper.sh

# jupyterlab
pip install jupyterlab
conda install nb_conda
nohup jupyter lab --ip=0.0.0.0 --port=3378 --allow-root --no-browser > ~/jupyter.log 2>&1 &

# megatron_util
pip install megatron_util -f https://modelscope.oss-cn-beijing.aliyuncs.com/releases/repo.html