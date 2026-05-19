import numpy as np
import h5py
import os
import streams_dic as sd

stream_list = ['t00_fwd', 't01_fwd']
main_location = os.path.expanduser('~')+'${YOUR_PATH_HERE}data/X451/'
### Creating a dictionary with the correlators for average
the_corr_dict = {}

### Loop over each stream
for stream in stream_list:
    
    ### getting the list of configs
    the_configs = sd.the_streams[stream].configs
    
    ### getting the name of the file
    the_file_name = sd.the_streams[stream].file_name
    
    ##3 opening the file
    with h5py.File(f'{main_location}{the_file_name}.hdf5', 'r') as f:
        
        ### Loop over the irreps
        for the_irrep in f.keys():
            
            ### creating an irrep in the dictionary
            if the_irrep not in the_corr_dict:
                the_corr_dict[the_irrep] = {}
                
            ### Storing the dataset
            the_data = f[the_irrep]['data'][:]
            
            ### Loop over the configs
            for cfg, corr in zip(the_configs, the_data):
                
                ### Checking if config exists here
                if cfg not in the_corr_dict[the_irrep]:
                    the_corr_dict[the_irrep][cfg] = []
                
                ### Adding the correlator now
                the_corr_dict[the_irrep][cfg].append(corr)

### Now we merge the correlators and average over the source times if there are repeated configs
the_merged_corr = {}
for the_irrep in the_corr_dict:
    the_sorted_cnfgs = sorted(the_corr_dict[the_irrep].keys())
    the_avg_corrs = []
    for cfg in the_sorted_cnfgs:
        the_avg_corrs.append(np.mean(the_corr_dict[the_irrep][cfg], axis=0))
    the_merged_corr[the_irrep] = {'configs': np.array(the_sorted_cnfgs), 
                                  'data': np.asarray(the_avg_corrs),}

the_merged_corr['PSQ0_G1g'].shape
