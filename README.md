The catalog file and uvbeam file need to be downloaded from here: 
https://drive.google.com/drive/folders/14hH-zBhHGddVacc0ncqRWq7ofhGLWfND?usp=drive_link

Filepaths:
gleam.vot --> issue_rep/catalog_files/gleam.vot
HERA_NicCST_fullfreq.uvbeam --> issue_rep/simulations/telescope_config/HERA_NicCST_fullfreq.uvbeam

From there use the environment.yml file to create a conda environment and activate it (this is just the environment.yml file from a relatively recent pull of main on pyuvsim)
After that locally install pyuvsim from source as usual 

Can then recreate the conversion attempt I made by running:
`python3 convert.py`

From there run the two doctored reference simulation files with (in the top directory of this repo):
"""
mpirun python scripts/run_param_pyuvsim.py simulations/obsparam_ref_2.2_uvbeam_gleam.yaml
mpirun python scripts/run_param_pyuvsim.py simulations/obsparam_ref_2.2_uvbeam_skyh5.yaml
"""

The result can be analyzed with the test.py file in results_data (matplotlib needs to be installed)
