import numpy as np
import h5py
import streams_dic as sd
import hadron_data as hd
import os

#This function is meant to reshape the multihadron correlators from [N,N, Ncfgs,nt] -> [Ncfgs, N,N,nt]. It receives:
# a: The original data with that shape
# s: the amount of operators to construct the NxN "matrix".
def RESHAPING(a):
    return np.transpose(a, (2,0,1,3))

# a.shape = [Ncnfgs,nt,N,N]
# b.shape = [Ncnfgs,N,N,nt]
def RESHAPING_FINAL(a):
    return np.transpose(a, (0,2,3,1))
            

# a.shape = [N,N,Nrows, Ncnfgs,nt]
# b.shape = [N.rows, Ncnfgs, nt, N,N]
def RESHAPE_FOR_ROW_AVRG(a):
    return np.transpose(a, (2,3,4,0,1))
    
    
def SQUARED_MOM(the_mom_str):
    the_mod_mom = list(the_mom_str.split('_'))
    if len(the_mod_mom[0])==2:
        return [str(the_mod_mom[0][1]),the_mod_mom[1]]
    elif len(the_mod_mom[0])>2:
        the_new_mom = 0
        for i in range(1,len(the_mod_mom[0])):
            if the_mod_mom[0][i]=='m': the_new_mom+=1
            elif the_mod_mom[0][i]=='d': the_new_mom+=4
            else: the_new_mom+=int(the_mod_mom[0][i])
        return [str(the_new_mom),the_mod_mom[1]]

def WRAP_AROUND(the_temp_nt, the_positions, a_counter, the_configs_list, the_fwd_bwd):
    if the_fwd_bwd=='fwd':
        the_factor = (-1. if the_temp_nt>=(128 - the_positions[(the_configs_list[a_counter])-1]) else 1.)
    elif the_fwd_bwd=='bwd':
        if the_temp_nt<=the_positions[(the_configs_list[a_counter])-1]:
            the_factor = -1.
        else:
            the_factor = 1.
    return the_factor

myStream = 't00_bwd'

the_configs = sd.the_streams[myStream].configs
the_nt_min = sd.the_streams[myStream].nt_min
the_nt_max = sd.the_streams[myStream].nt_max
the_file_name = sd.the_streams[myStream].file_name
the_string_name = sd.the_streams[myStream].name
the_propagation = sd.the_streams[myStream].propagation
the_start_positions = sd.the_streams[myStream].the_start_positions


main_location = os.path.expanduser('~')+'${YOUR_PATH_DIR}/data/X451/'
name_folder = 'IsodoubletStrangeFermionic/'
correlator_data = h5py.File(f'{main_location}{the_file_name}.hdf5','w') 
print(f"Data saved to: \n{main_location}{the_file_name}.hdf5") 

mom_comb = ["P0_G1g", "P0_G1u", "P0_Hg", "P0_Hu", "P001_G1", "P010_G1", "P100_G1", "P00m_G1", "P0m0_G1", "Pm00_G1", "P001_G2", "P010_G2", "P100_G2", "P00m_G2", "P0m0_G2", "Pm00_G2", "P110_G", "P101_G", "P011_G", "Pm10_G",  "P10m_G", "P0m1_G",  "P1m0_G",  "Pm01_G", "P01m_G", "Pmm0_G", "Pm0m_G", "P0mm_G", "P111_G", "P11m_G", "P1m1_G", "Pm11_G", "P1mm_G", "Pmm1_G", "Pm1m_G", "Pmmm_G", "P111_F1", "P11m_F1", "P1m1_F1", "Pm11_F1", "P1mm_F1", "Pmm1_F1", "Pm1m_F1", "Pmmm_F1", "P111_F2", "P11m_F2", "P1m1_F2", "Pm11_F2", "P1mm_F2", "Pmm1_F2", "Pm1m_F2","Pmmm_F2","P002_G1", "P020_G1", "P200_G1", "P00d_G1", "P0d0_G1", "Pd00_G1"]

mom_squared = {}
for item in mom_comb:
    sqr_mom, the_irrep = SQUARED_MOM(item)
    key = (sqr_mom, the_irrep)
    if key not in mom_squared:
        mom_squared[key] = []
    mom_squared[key].append(item)
    
list_of_xi = hd.the_list_of_xi

for hadron in list_of_xi:
    size_matrix = hadron.size_matrix
    irrep_dim = hadron.irrep_dim
    da_irrep = hadron.irrep
    da_sqr_mom = hadron.sqr_mom
    the_operators = hadron.operator
    
    matching_moms = mom_squared[(da_sqr_mom, da_irrep)]
    n_moms = len(matching_moms)
    n_cfgs = len(the_configs)
    corr_all = np.zeros((size_matrix, size_matrix, n_moms, irrep_dim, n_cfgs, the_nt_max - 1), dtype=np.complex128)
    print("-----------------------------------------------------------")
    print(f"Irrep: {da_irrep}")
    print(f"Matching momenta: {matching_moms}")
    for jj in range(size_matrix):
        # for kk in range(size_matrix):
        ### Loop over the upper triangle (FIXING THE HERMITIAN ISSUE)
        for kk in range(jj, size_matrix):
            for mm, item in enumerate(matching_moms):
                for zz in range(irrep_dim):
                    the_file = np.loadtxt(f'{main_location}{name_folder}{item}_{zz+1}/corr_{the_string_name}_{item}_{zz+1}_Ops{jj}_{kk}.dat', skiprows=1, unpack=True)
                    nt_temp=0
                    counter=0
                    corr_nt = []
                    correlator=[]
                    for ll in range(len(the_file[0])):
                        the_factor_temp = WRAP_AROUND(nt_temp, the_start_positions, counter, the_configs, the_propagation)
                        the_real_corr = the_factor_temp * the_file[1][ll]
                        the_imag_corr = the_factor_temp * the_file[2][ll]
                        the_complex_corr = the_real_corr + 1j * the_imag_corr
                        corr_nt.append(the_complex_corr)
                        if nt_temp<the_nt_max:
                            nt_temp+=1
                        else:
                            correlator.append(corr_nt[the_nt_min:])
                            nt_temp=0
                            counter+=1
                            corr_nt = []
                    corr_all[jj,kk,mm,zz]=np.asarray(correlator)
                    ### This adds the conjugated part of the matrix
                    if jj!=kk:
                        corr_all[kk,jj,mm,zz]=np.conjugate(corr_all[jj,kk,mm,zz])
    correlator_avg = RESHAPING(np.mean(corr_all, axis=(2,3)))
    corr_data = correlator_data.create_group(f"PSQ{da_sqr_mom}_{da_irrep}")
    corr_data.create_dataset('data', data = np.asarray(correlator_avg))
    corr_data.attrs.create('op_list', np.array(hadron.operator, dtype=object))
    corr_data.attrs.create('Other_Info', f'min time slice = {the_nt_min} \n max time slice = {the_nt_max}')
    corr_data.attrs.create('configs', data = the_configs)

