import numpy as np
import h5py
import os
import streams_dic as sd

stream_list = ['t00_fwd', 't01_fwd']
main_location = os.path.expanduser('~')+'${YOUR_PATH}/data/X451/'
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
                the_corr_dict[the_irrep] = {'data':{}, 'op_list': []}
                
            ### Storing the dataset
            the_data = f[the_irrep]['data'][:]
            
            ### Storing the operators
            the_corr_dict[the_irrep]['op_list'] = f[the_irrep].attrs['op_list']
            
            ### Loop over the configs
            for cfg, corr in zip(the_configs, the_data):
                
                ### Checking if config exists here
                if cfg not in the_corr_dict[the_irrep]:
                    the_corr_dict[the_irrep]['data'][cfg] = []
                
                ### Adding the correlator now
                the_corr_dict[the_irrep]['data'][cfg].append(corr)


the_name_new_file = f'{main_location}cls21_X451_r001_isodoublet_Sm2_fwd.hdf5'
the_new_corr_file = h5py.File(the_name_new_file, 'w')

### Now we merge the correlators and average over the source times if there are repeated configs
the_merged_corr = {}
for the_irrep in the_corr_dict:
    the_sorted_cnfgs = sorted(the_corr_dict[the_irrep]['data'].keys())
    the_avg_corrs = []
    for cfg in the_sorted_cnfgs:
        the_avg_corrs.append(np.mean(the_corr_dict[the_irrep]['data'][cfg], axis=0))
    the_merged_corr[the_irrep] = {'configs': np.array(the_sorted_cnfgs), 
                                  'data': np.asarray(the_avg_corrs),
                                  'op_list': np.array(the_corr_dict[the_irrep]['op_list'], dtype=object)}
    the_dataset = the_new_corr_file.create_group(the_irrep)
    the_dataset.create_dataset('data', data = the_merged_corr[the_irrep]['data'])
    the_dataset.attrs.create('op_list', the_merged_corr[the_irrep]['op_list'])
    the_dataset.attrs.create('Other_Info', f'min time slice = {the_nt_min} \n max time slice = {the_nt_max}')
    the_dataset.attrs.create('configs', data = the_merged_corr[the_irrep]['configs'])

# the_merged_corr['PSQ0_G1g'].shape
