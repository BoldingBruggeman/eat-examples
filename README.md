# How to install EAT

These instructions describe how to install EAT on Linux, Mac and Windows.

The commands below should be run in a terminal. On Windows, this called a "Command Prompt" which you can open by clicking Start and typing `cmd`. On [a Mac with an M1 processor](https://en.wikipedia.org/wiki/Apple_M1#Products_that_use_the_Apple_M1_series), you will need to [open the terminal with Rosetta](https://www.byran.tech/html/how-to-make-a-rosetta-2-emulated-x86-terminal-on-arm-apple-silicon-chips.html).

If you experience problems installing EAT, please [report these as an issue](https://github.com/BoldingBruggeman/eat-examples/issues) (GitHub account required) or send an email to jorn@bolding-bruggeman.com.

## Anaconda

Check if you have [Anaconda](https://new.anaconda.com/products/distribution) by executing `conda --version`

* If `conda --version` fails (you get `command not found` or `"conda" is not recognized as an internal or external command`), install Miniconda on [Linux](https://conda.io/projects/conda/en/stable/user-guide/install/linux.html), [Windows](https://conda.io/projects/conda/en/stable/user-guide/install/windows.html), or [Mac](https://conda.io/projects/conda/en/stable/user-guide/install/macos.html). Note: on Mac, always pick an Intel x86 installer, even if you have an M1 processor.

  Installing miniconda does not require root/administrator privileges. Allow the installer to initialize the conda environment, unless you know you want to control this manually.​

* If `conda --version` succeeds, great. Now execute `conda update conda` to ensure your conda is up to date. If this fails because you do not have sufficient permissions (common on HPC systems with a centralized conda installation), we recommend you install Miniconda instead, for instance in your homedir (see the previous item).

## Create an isolated environment

Create a new conda environment with EAT​:
   
```
conda create -n eat -c bolding-bruggeman -c conda-forge eatpy
```

Note: some administrators disable the use of custom conda channels (the `-c bolding-bruggeman` above). If the above command fails for this reason, follow [manual installation instructions](https://github.com/BoldingBruggeman/eat/wiki#building-and-installing-manually), with one change: use the `seamless` branch of EAT by cloning the code with `git clone --recursive -b seamless https://github.com/BoldingBruggeman/eat.git`.

## Add conda packages

Add packages that we will use for analysis and visualization​:

```
conda install -n eat -c conda-forge jupyterlab ipympl netcdf4
```

## Verify everything installed correctly

No errors should occur executing these commands​:

```
conda activate eat
python -c "import eatpy, matplotlib, netCDF4"
jupyter lab --version
eat-gotm --version
```

The final command will report `model(no filter program present)`, among others - that is expected and not an error.
