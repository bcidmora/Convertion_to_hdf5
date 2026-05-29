import numpy as np
import h5py
import streams_dic as sd
import hadron_data as hd
import os
import matplotlib.pyplot as plt

def WRAP_AROUND(the_temp_nt, the_positions, a_counter, the_configs_list, the_fwd_bwd):
    if the_fwd_bwd=='fwd':
        the_factor = (-1. if the_temp_nt>=(128 - the_positions[(the_configs_list[a_counter])-1]) else 1.)
    elif the_fwd_bwd=='bwd':
        if the_temp_nt<=the_positions[(the_configs_list[a_counter])-1]:
            the_factor = -1.
        else:
            the_factor = 1.
    return the_factor
    

main_location = os.path.expanduser('~')+'${YOUR_PATH_HERE}/data/X451/'
name_folder = 'SingleHadrons'

myStream = 't01_bwd' # 't00_bwd' # 't00_fwd' # 't01_fwd'

the_configs = sd.the_streams[myStream].configs
the_nt_min = sd.the_streams[myStream].nt_min
the_nt_max = sd.the_streams[myStream].nt_max
the_file_name = sd.the_streams[myStream].file_name
the_string_name = sd.the_streams[myStream].name
the_propagation = sd.the_streams[myStream].propagation
the_start_positions = sd.the_streams[myStream].the_start_positions
list_of_SH = hd.the_list_of_SH

correlator_data = h5py.File(f'{main_location}{the_file_name}.hdf5','w') 
print(f"Data saved to: \n {main_location}{the_file_name}.hdf5")

for hadron in list_of_SH:
    correlator = []
    corr_nt = []
    if hadron.hadron_type=='meson':
        the_file = np.loadtxt(f'{main_location}{name_folder}/{hadron.file_name}_{the_string_name}.dat',skiprows=1)
        nt_temp = 0
        for ll in range(len(the_file)):
            the_value = np.complex128(float(the_file[ll][1]) + float(the_file[ll][2])*1j)
            corr_nt.append(the_value)
            if nt_temp<the_nt_max:
                nt_temp+=1
            else:
                correlator.append(np.asarray(corr_nt[the_nt_min:]))
                nt_temp=0
                corr_nt = []
        correlator = np.asarray(correlator)
    elif hadron.hadron_type=='baryon':
        the_file_1 = np.loadtxt(f'{main_location}{name_folder}/{hadron.file_name}_{the_string_name}_1.dat',skiprows=1)
        the_file_2 = np.loadtxt(f'{main_location}{name_folder}/{hadron.file_name}_{the_string_name}_2.dat',skiprows=1)
        nt_temp = 0
        counter=0
        for ll in range(len(the_file_1)):
            the_factor_temp = WRAP_AROUND(nt_temp, the_start_positions, counter, the_configs, the_propagation)
            the_real_part = ((the_factor_temp * float(the_file_1[ll][1])) + (the_factor_temp * float(the_file_2[ll][1])))/float(2.)
            the_imag_part = (( the_factor_temp * float(the_file_1[ll][2]))+ (the_factor_temp * float(the_file_2[ll][2])))/float(2.)
            the_value = np.complex128(the_real_part + the_imag_part*1j)
            corr_nt.append(the_value)
            if nt_temp<the_nt_max:
                nt_temp+=1
            else:
                correlator.append(np.asarray(corr_nt[the_nt_min:]))
                counter+=1
                nt_temp=0;
                corr_nt = []
        correlator = np.asarray(correlator)
    the_name_irrep = f'{hadron.psq}{hadron.irrep}_{hadron.file_name[0].capitalize()}'
    corr_data = correlator_data.create_group(the_name_irrep)
    corr_data.create_dataset('data', data=correlator)
    corr_data.attrs.create('op_list', np.array([hadron.operator], dtype=object))
    corr_data.attrs.create('Other_Info', f'min time slice = {the_nt_min} \n max time slice = {the_nt_max}')
    corr_data.attrs.create(f'configs_{the_string_name}', list(the_configs))
    correlator = []

            



