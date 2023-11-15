# How to install EAT

These instructions describe how to install EAT on Linux, Mac and Windows.

The commands below should be run in a terminal. On Windows, open a terminal by choosing "Anaconda prompt" in the start menu (instructions on how to install this below).

If you experience problems installing EAT, please [report these as an issue](https://github.com/BoldingBruggeman/eat-examples/issues) (GitHub account required) or send an email to jorn@bolding-bruggeman.com.

## Anaconda

Check if you have [Anaconda](https://new.anaconda.com/products/distribution) by executing `conda --version` (Linux, Mac) or verifying "Anaconda Prompt" is available from the Start Menu (Windows)

* If you do not have Anaconda yet, install Miniconda on [Linux](https://conda.io/projects/conda/en/stable/user-guide/install/linux.html), [Windows](https://conda.io/projects/conda/en/stable/user-guide/install/windows.html), or [Mac](https://conda.io/projects/conda/en/stable/user-guide/install/macos.html).

  Installing miniconda does not require root/administrator privileges. Allow the installer to initialize the conda environment, unless you know you want to control this manually.​

  After installing conda, you will have to close and reopen your terminal to activate conda support. On Windows, you need to open the newly installed "Anaconda Prompt".

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

Troubleshooting:
* *unable to open mca_btl_openib*. This is a warning that can be ignored. It indicates a lack of support for high-speed interconnects, which we do not need because we will run on a single workstation. Optionally, you can install this support just to remove the warning: `conda install -c conda-forge ucx libnl`.
* *model(no filter program present)*. This is expected output for the `eat-gotm` command.
* On Windows, if you get a firewall alert such as  *Windows Defender Firewall has blocked some features of this app*, you can click "Cancel". This will not affect the functionality of EAT.
* *You seem to have a system wide installation of MSMPI* (Windows-only). This can cause problems. Remove MPI from your conda environment with `conda remove --force -y msmpi`.

## Download and extract the example setup

*This could be done during the workshop, provided you have a reliable internet connection.*

First download [the zip file with an example setup, run scripts, and analysis notebooks](https://github.com/BoldingBruggeman/eat-examples/archive/refs/heads/main.zip).

Now extract this file to some location on your computer. On Windows, open the zip file and choose "Extract all". On Linux and Mac, execute `unzip <ZIPFILE>` in a terminal. Remember the location you extracted to, as we will revisit it during the workshop.

## Configure and download your own setup

*This could be done during the workshop, provided you have a reliable internet connection.*

* Visit [the iGOTM web site](https://igotm.bolding-bruggeman.com/?key=TVJKK65Z)
* Click a location to simulate
* Click the "Configure simulation" button (<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gear.svg" width="15" height="15">)
* Customize:
  - the time period (recommended: 3 years)
  - biogeochemistry (recommended: PISCES, ERSEM, BFM or ECOSMO)
  - include remotely sensed surface temperature and chlorophyll
* Click the "Download GOTM setup" button (<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/download.svg" width="15" height="15">)
* Extract the zip file to some location on your computer (remember this location, as we will need it during the workshop)


## Reference

The below commands are for use during the workshop itself.

* Load the EAT environment whenever you open a new terminal​
  ```
  conda activate eat​
  ```

* Commands should be executed from the directory with your GOTM setup (for instance, the one you downloaded from iGOTM)
  ```
  cd <SETUPDIR>​
  ```
* To run a stand-alone simulation (no ensemble, no data assimilation)​:
  ```
  eat-gotm​
  ```
* To generate an ensemble:
  ```
  python <GENERATE_SCRIPT>​
  ```
  In the example, `<GENERATE_SCRIPT>` would be one of `generate_ensemble*.py`.

* To run a data assimilation experiment:
  ```
  mpiexec -n 1 python <RUN_SCRIPT> : -n <NENS> eat-gotm [--separate_gotm_yaml] [--separate_restart_file]​
  ```    
  In the downloaded example, `<RUN_SCRIPT>` would be one of `assimilate*.py`.

  `<NENS>` is the number of ensemble members. This should match the number in your ensemble generation script (`<GENERATE_SCRIPT>​` above).

  At least one of `--separate_gotm_yaml` and `--separate_restart_file` should be specified to ensure that ensemble members differ from each other.

  If conda installed EAT with OpenMPI instead of MPICH (Linux and Mac only, you can check with `conda list mpi`), you will need to add `--oversubscribe` to be able to use large ensemble sizes (&ge; your number of cores).

* Analyze results:​
  ```
  jupyter lab​
  ```
  Allow the browser to open, then click one of the Jupyter notebooks (`*.ipynb`).​