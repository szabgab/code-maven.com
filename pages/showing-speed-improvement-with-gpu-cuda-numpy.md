---
title: "Showing speed improvement using a GPU with CUDA and Python with numpy on Nvidia Quadro 2000D"
timestamp: 2017-12-10T10:30:01
tags:
  - numpy
  - numba
  - GPU
  - cuda
  - conda
  - Nvidia
published: true
author: szabgab
archive: true
---


I just installed Linux on an old computer that used to be powerful that has a <b>Nvidia Quadro 2000D</b> GPU. I wanted to see how to use the GPU to speed up computation done in a simple Python program. It took me some time and some hand holding to get there. Let me share the journey and the results.

In a nutshell: Using the GPU has overhead costs. If the computation is not heavy enough, then the cost (in time) of using a GPU might be larger than the gain. On the other hand if the computation is heavy, you can see a huge improvement in speed.


## Installation

Once I had Ubuntu 17.10 installed (desktop edition) I went to install all the Python stuff. Ubuntu already comes with Python 3. I installed `virtualenv` using `apt` and then using `pip` I've installed all the Python modules I needed in the virtualenv. That did not work out well. When I ran the code that was supposed to use the GPU (see the code below) I got an error:

```
numba.cuda.cudadrv.error.NvvmSupportError: libNVVM cannot be found. Do `conda install cudatoolkit`:
library nvvm not found
```

OK. I deactivated the virtualenv and installed [Miniconda](https://conda.io/miniconda.html).

Some stuff I needed for the rest of the installation:

```
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
sudo aptitude install nvidia-cuda-dev
sudo aptitude install python3-dev
```

Install Miniconda:

```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
```

Install the tools I needed:

```
conda install cudatoolkit
conda install numpy
conda install numba
```

Once I've managed to install everything I wrote a short Python script based on [this article](https://devblogs.nvidia.com/parallelforall/numba-python-cuda-acceleration/). 

{% include file="examples/python/vector_addition_with_gpu.py" %}

That was an utter disappointment. The GPU actually slowed down the operations though if we look closely we can see that the slow down ratio is much worse for the smaller vectors. I tried creating bigger matrices and multiply them, but there is a limit to the size of the matrices this GPU can handle. Whenever I supplied a number that created a matrix which was too big I got an exception:

```
numba.cuda.cudadrv.driver.CudaAPIError: [1] Call to cuLaunchKernel results in CUDA_ERROR_INVALID_VALUE
```

Even when I got close to the limit the CPU was still a lot faster than the GPU.

```
$ python speed.py cpu 100000
Time: 0.0001056949986377731
$ python speed.py cuda 100000
Time: 0.11871792199963238

$ python speed.py cpu 11500000
Time: 0.013704434997634962
$ python speed.py cuda 11500000
Time: 0.47120747699955245
```

In the meantime I was monitoring the GPU using `nvidia-smi`.  Occasionally it showed that the Python process is running, but otherwise it was not useful to me.

```
watch -n 0.5 nvidia-smi
```

I asked on [Stack Overflow](https://stackoverflow.com/questions/47710707/cuda-gpu-is-slower-than-cpu-in-simple-numpy-operation). I got some good suggestions, especially from [Ignacio Vergara Kausel](https://stackoverflow.com/users/2244081/ignacio-vergara-kausel). He pointed me to [a notebook](https://github.com/ContinuumIO/gtc2017-numba/blob/master/2%20-%20CUDA%20Basics.ipynb) (that apparently was also linked from a comment in the original article I skimmed) that showed a much better example. It even showed the problem I was facing. That is the GPU slowing down the operations.

Based on that article I've created a new script that would be able to demonstrate the speed improvement.

{% include file="examples/python/math_with_gpu.py" %}

```
$ python math_with_gpu.py
1
Time: 0.011146817007102072
Time: 0.13940549999824725
10
Time: 0.12172191697754897
Time: 0.023090153001248837
100
Time: 1.2920606719853822
Time: 0.03889427299145609
1000
Time: 12.961911355989287
Time: 0.1976439240097534
```


That is, if we calculate sinus once, the CPU is still faster.
If we calculate it 10 times, the GPU is already faster.
(I think I found them roughly the same speed at 6 iterations.)

The actual ratios of the 4 measurement points are here:

```
 0.08
 5.27
33.22
65.58
```

It surprised me that the speed improvement only doubled when we went from 100 iteration to 1000 iteration.
I though it would have a much bigger impact. I'll need to create more complex examples to understand that part.

In an case, we can see that for tasks with relatively low computational complexity we might actually lose time using the GPU, but as our computations becomes more and more intensive, we do see a gain even from a relatively old and weak GPU.

