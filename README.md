# H.E.L.E.N.
H.E.L.E.N. (Haplotype Embedded Long-read Error-corrector for Nanopore)


[![Build Status](https://travis-ci.com/kishwarshafin/helen.svg?branch=master)](https://travis-ci.com/kishwarshafin/helen)

`HELEN` is a polisher intended to use for polishing assemblies generated by the [Shasta](https://github.com/chanzuckerberg/shasta) assembler. `HELEN` operates on the pileup summary generated by [MarginPolish](https://github.com/UCSC-nanopore-cgl/marginPolish). `MarginPolish` uses a probabilistic graphical-model to encode read alignments through a draft assembly to find the maximum-likelihood consensus sequence. The graphical-model operates in run-length space, which helps to reduce errors in homopolymeric regions. `MarginPolish` can produce tensor-like summaries encapsulating the internal likelihood weights. The weights are assigned to each genomic position over multiple likely outcomes that is suitable for inference by a Deep Neural Network model. `HELEN` uses a Recurrent-Neural-Network (RNN) based Multi-Task Learning (MTL) model that can predict a base and a run-length for each genomic position using the weights generated by `MarginPolish`. The combination of `Shasta-MarginPolish-HELEN` produces state-of-the-art human genome assemblies constructed using Oxford Nanopore Sequencing Technology.

© 2019 Kishwar Shafin, Trevor Pesout. <br/>
Computational Genomics Lab (CGL), University of California, Santa Cruz.

## Why MarginPolish-HELEN ?
* `MarginPolish-HELEN` outperforms other graph-based and Neural-Network based polishing pipelines (Racon-Medaka).
* Highly optimized pipeline that is faster than any other available tool.
* We have sequenced-assembled-polished 12 samples to ensure robustness, runtime-consistency and cost-efficiency.
* Using `HELEN` with GPU is simple. We tested GPU usage on `Amazon Web Services (AWS)` and `Google Cloud Platform (GCP)` to ensure robustness and scalability.
* Open source (MIT License)

## Table of contents
* [Workflow](#workflow)
* [Results](#Results)
* [Runtime](#Runtime)
   * [Google Cloud Platform runtime](#Google-Cloud-Platform-runtime)

## Workflow

The workflow is as follows:
* Generate an assembly with [Shasta](https://github.com/chanzuckerberg/shasta).
* Create a mapping between reads and the assembly using [Minimap2](https://github.com/lh3/minimap2).
* Use [MarginPolish](https://github.com/UCSC-nanopore-cgl/marginPolish) to generate the images.
* Use HELEN to generate a polished consensus sequence.

<p align="center">
<img src="img/pipeline.svg" alt="pipeline.svg" height="640p">
</p>



## Results
Put some dope results here

## Runtime
To ensure robustness of `HELEN` we have tested it on two cloud computing platforms `Amazon Web Services (AWS)` and `Google Cloud Platform (GCP)`. We report runtime on multiple samples and the instance-types we have used while running the pipeline. The three computation that we do with `HELEN` are:
* Download all images generated by `MarginPolish`
* Run `call_consensus.py` (requires GPU).
* Run `stitch.py` (Multi-threaded on CPU, no GPU required).

#### Google Cloud Platform runtime
GCP allows to customize an instance between different runs. Users can stop an instance, scale it and start the next step. We ran `HELEN` on four samples in such way that is most cost-effective. We estimated the costs from the [Google Cloud Platform Pricing Calculator](https://cloud.google.com/products/calculator/).

<center>
<font size="-2">
<table>
<colgroup>
<col style="width: 73px">
<col style="width: 99px">
<col style="width: 46px">
<col style="width: 44px">
<col style="width: 106px">
<col style="width: 154px">
<col style="width: 42px">
<col style="width: 54px">
<col style="width: 106px">
<col style="width: 44px">
<col style="width: 48px">
<col style="width: 57px">
</colgroup>
  <tr>
    <th class="tg-1wig" rowspan="2">Sample</th>
    <th class="tg-amwm" colspan="3">Download</th>
    <th class="tg-amwm" colspan="4">call_consensus.py</th>
    <th class="tg-amwm" colspan="3">stitch.py</th>
    <th class="tg-1wig" rowspan="2">TOTAL COST</th>
  </tr>
  <tr>
    <td class="tg-amwm">Instance type</td>
    <td class="tg-amwm">Time <br>Mins</td>
    <td class="tg-amwm">Cost</td>
    <td class="tg-amwm">Instance type</td>
    <td class="tg-amwm">GPU</td>
    <td class="tg-amwm">Time<br>Mins</td>
    <td class="tg-amwm">Cost</td>
    <td class="tg-amwm">Instance type</td>
    <td class="tg-amwm">Time<br>Mins</td>
    <td class="tg-amwm">Cost</td>
  </tr>
  <tr>
    <td class="tg-baqh">HG01109</td>
    <td class="tg-baqh">n1-standard-1</td>
    <td class="tg-baqh">67</td>
    <td class="tg-baqh">1$</td>
    <td class="tg-baqh">n1-standard-32</td>
    <td class="tg-baqh">2 x NVIDIA Tesla P100</td>
    <td class="tg-baqh"></td>
    <td class="tg-baqh"></td>
    <td class="tg-baqh"></td>
    <td class="tg-baqh"></td>
    <td class="tg-baqh"></td>
    <td class="tg-baqh"></td>
  </tr>
  <tr>
    <td class="tg-baqh">HG02080</td>
    <td class="tg-baqh">n1-standard-1</td>
    <td class="tg-baqh">66</td>
    <td class="tg-baqh">1$</td>
    <td class="tg-baqh">n1-standard-32</td>
    <td class="tg-baqh">2 x NVIDIA Tesla P100</td>
    <td class="tg-baqh">535</td>
    <td class="tg-baqh">39.96$</td>
    <td class="tg-baqh">n1-standard-96</td>
    <td class="tg-baqh">22</td>
    <td class="tg-baqh">2$</td>
    <td class="tg-baqh">43$</td>
  </tr>
  <tr>
    <td class="tg-baqh">HG01243</td>
    <td class="tg-baqh">n1-standard-1</td>
    <td class="tg-baqh">70</td>
    <td class="tg-baqh">1$</td>
    <td class="tg-baqh">n1-standard-32</td>
    <td class="tg-baqh">2 x NVIDIA Tesla P100</td>
    <td class="tg-baqh">541</td>
    <td class="tg-baqh">44.4$</td>
    <td class="tg-baqh">n1-standard-96</td>
    <td class="tg-baqh">21</td>
    <td class="tg-baqh">2$</td>
    <td class="tg-baqh">48$</td>
  </tr>
  <tr>
    <td class="tg-baqh">GM24143</td>
    <td class="tg-baqh">n1-standard-1</td>
    <td class="tg-baqh">68</td>
    <td class="tg-baqh">1$</td>
    <td class="tg-baqh">n1-standard-32</td>
    <td class="tg-baqh">2 x NVIDIA Tesla P100</td>
    <td class="tg-baqh"></td>
    <td class="tg-baqh"></td>
    <td class="tg-baqh"></td>
    <td class="tg-baqh"></td>
    <td class="tg-baqh"></td>
    <td class="tg-baqh"></td>
  </tr>
</table>
</font>
</center>

If you want to do all three steps without rescaling the instance after each step, we suggest you use this configuration:
* Instance type: n1-standard-32 (32 vCPUs, 120GB RAM)
* GPUs: 2 x NVIDIA Tesla P100
* Disk: 2TB SSD
* TIP: Use `Deep Learning Image: PyTorch 1.1.0 and fastai m25 CUDA 10.0` as boot disk which has pre-installed `CUDA 10.0` and `PyTorch`.

The estimated runtime with this instance type is 13 hours (including setup and download). The [estimated cost](https://cloud.google.com/products/calculator/#id=6aeafb9f-e28d-4f9e-9406-cf8282a12ecc) with this instance is <b>60.39$</b>.

## Installation
Although `HELEN` can be used in a `CPU` only machine, we highly recommend using a machine with `GPU`. This requires installing `CUDA` and the right `PyTorch` version compiled against the installed version of `CUDA`.

##### Install CUDA
We optimized `HELEN` to run on GPUs and we highly recommend using GPU machines to run `call_consensus.py`. The supported `CUDA` version for `HELEN` is `10.0`. To download `CUDA` for `Ubuntu 18.04` follow these insructions:

```bash
# download CUDA for ubuntu 18.04 x86_64 by running:
wget https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda_10.0.130_410.48_linux
# if you are using other systems please download the correct version from here: https://developer.nvidia.com/cuda-10.0-download-archive

# install CUDA by running:
sudo sh cuda_10.0.130_410.48_linux.run
# 1) Read or scroll through the EULA (you can press 'z' to scroll down).
# 2) Accept the EULA, put yes for OpenGL library, CUDA toolkit and all other softwares. Installing CUDA-samples is optional

# once installed, verify the right version by running:
cat /usr/local/cuda/version.txt
# Expected output: CUDA Version 10.0.130

# Verify that you can see your GPU status by running:
nvidia-smi
```

##### Install PyTorch
Please follow the instructions from this [pytorch-installation-guide](https://pytorch.org/get-started/locally/) to install the right `PyTorch` version.

```bash
# if you are using Ubuntu 18.04, python3 version 3.6.7 and CUDA 10.0 then follow these commands:
python3 -m pip install https://download.pytorch.org/whl/cu100/torch-1.1.0-cp36-cp36m-linux_x86_64.whl
python3 -m pip install torchvision

# otherwise install the right version by following the instructions from: https://pytorch.org/get-started/locally/
```

`HELEN` uses `PyTorch` as the deep-neural-network library. We suggest a careful installation of `PyTorch` with the right `CUDA` version. We highly recommend using `HELEN` on a GPU machine, and we have made it easy to use on multiple GPUs. Install the right `PyTorch` package compiled against the right `CUDA` version and using `HELEN` is as simple as setting a flag `--gpu_mode 1`. We have tested these PyTorch versions against `HELEN` to ensure GPU accelerated inference:
* PyTorch 1.0 with CUDA 10.0
* PyTorch 1.1 with CUDA 10.0

To ensure `PyTorch` is using `CUDA`, you follow these instructions:
```bash
$ python3
>>> import torch
>>> torch.cuda.is_available()
TRUE
# the expected output is TRUE
```

#### Install HELEN
`HELEN` requires `cmake` and `python3` to be installed in the system.
```bash
sudo apt-get -y install cmake
sudo apt-get -y install python3
sudo apt-get -y install python3-dev
```
To install `HELEN`:

```bash
git clone https://github.com/kishwarshafin/helen.git
cd helen
./build.sh
```

These steps will install `HELEN` in your local system. `HELEN` also requires installing some python3 packages.
```bash
python3 -m pip install h5py tqdm numpy torchnet
```

## Model
#### Released models
Change in the basecaller algorithm can directly affect the outcome of HELEN. We will release trained models with new basecallers as they come out.
<center>

|     Model Name     | Release Date | Intended base-caller |                                                                 Link                                                                |
|:------------------:|:------------:|:--------------------:|:-----------------------------------------------------------------------------------------------------------------------------------:|
| v0_lc_r941_flip235 |  16/05/2019  |      Guppy 2.3.5     | [Model_link](https://storage.googleapis.com/kishwar-helen/helen_trained_models/v0_london_calling_2019/HELEN_v0_lc_r941_flip235.pkl) |
</center>
#### Model Schema

HELEN implements a Recurrent-Neural-Network (RNN) based Multi-task learning model with hard parameter sharing. It implements a sliding window method where it slides through the input sequence in chunks. As each input sequence is evaluated independently, it allows HELEN to use mini-batch during training and testing.

<p align="center">
<img src="img/model_schema.svg" alt="pipeline.svg" height="640p">
</p>


## Usage
Full user documentation [Working on it]

## Help
Email address of someone helpful.

## Acknowledgement
We are thankful to the developers of these packages: </br>
* [pytorch](https://pytorch.org/)
* [ssw library](https://github.com/mengyao/Complete-Striped-Smith-Waterman-Library)
* [hdf5 python (h5py)](https://www.h5py.org/)
* [pybind](https://github.com/pybind/pybind11)


© 2019 Kishwar Shafin, Trevor Pesout.
