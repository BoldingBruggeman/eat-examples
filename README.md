# How to install EAT

These instructions describe how to install EAT on Linux, Mac and Windows.

The commands below should be run in a terminal. On Windows, open a terminal by choosing "Anaconda prompt" in the start menu (instructions on how to install this below).

If you experience problems installing EAT, please [report these as an issue](https://github.com/BoldingBruggeman/eat-examples/issues) (GitHub account required) or send an email to jorn@bolding-bruggeman.com.

## Anaconda

Check if you have [Anaconda](https://new.anaconda.com/products/distribution) by executing `conda --version` (Linux, Mac) or verifying "Anaconda Prompt" is available from the Start Menu (Windows)

* If you do not have Anaconda yet, install Miniconda on [Linux](https://conda.io/projects/conda/en/stable/user-guide/install/linux.html), [Windows](https://conda.io/projects/conda/en/stable/user-guide/install/windows.html), or [Mac](https://conda.io/projects/conda/en/stable/user-guide/install/macos.html).

  Installing miniconda does not require root/administrator privileges. Allow the installer to initialize the conda environment, unless you know you want to control this manually.​

  After installing conda, you will have to close and reopen your terminal to activate conda support. On Windows, you specifically need to open the newly installed "Anaconda Prompt".

* If `conda --version` succeeds, great. Now execute `conda update conda` to ensure your conda is up to date. If this fails because you do not have sufficient permissions (common on HPC systems with a centralized conda installation), we recommend you install Miniconda instead, for instance in your homedir (see the previous item).

## Create an isolated environment

Create a new conda environment with EAT​:
   
```
conda create -n eat -c bolding-bruggeman -c conda-forge -y eatpy
```

Note: some administrators disable the use of custom conda channels (the `-c bolding-bruggeman` above). If the above command fails for this reason, follow [manual installation instructions](https://github.com/BoldingBruggeman/eat/wiki#building-and-installing-manually), with one change: use the `seamless` branch of EAT by cloning the code with `git clone --recursive -b seamless https://github.com/BoldingBruggeman/eat.git`.

## Add conda packages

Add packages that we will use for analysis and visualization​:

```
conda install -n eat -c conda-forge -y jupyterlab ipympl netcdf4
```

## Verify everything installed correctly

No errors should occur executing these commands​:

```
conda activate eat
python -c "import eatpy, matplotlib, netCDF4"
jupyter lab --version
eat-gotm --version
```

Any warnings about "unable to open mca_btl_openib" can be ignored.

The final command will report `model(no filter program present)`, among others - that is expected and not an error.

On Windows:
* if you get an alert stating that "Windows Defender Firewall has blocked some features of this app", you can click "Cancel".
This will not affect the functionality of EAT.
* if you receive a warning stating that "You seem to have a system wide installation of MSMPI", remove MPI from your conda environment with `conda remove --force -y msmpi`.
