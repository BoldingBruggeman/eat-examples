# How to install EAT

1. If you do not have [Anaconda](https://new.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) yet (try executing `conda`)​

   Install Miniconda on [Linux](https://conda.io/projects/conda/en/stable/user-guide/install/linux.html), [Windows](https://conda.io/projects/conda/en/stable/user-guide/install/windows.html), or [Mac](https://conda.io/projects/conda/en/stable/user-guide/install/macos.html). This does not require root/administrator privileges. Allow the installer to initialize the conda environment, unless you know you want to control this manually.​

2. Create a new conda environment with EAT​:
   
   ```
   conda create -n eat -c bolding-bruggeman -c conda-forge eatpy
   ```

3. Test – no errors should occur executing these commands​:

   ```
   conda activate eat​
   python -c "import eatpy"​
   eat-gotm -h​
   ```

4. Add packages for analysis/visualization​:

   ```bash
   conda install -n eat -c conda-forge jupyterlab ipympl netcdf4
   ```
