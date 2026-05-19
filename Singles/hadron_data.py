from dataclasses import dataclass

@dataclass
class HadronData:
    file_name: str
    operator: str
    irrep: str
    size_matrix: str
    psq: str
    hadron_type: str
    
    
pion = [
    HadronData(file_name='pion_dsq0', operator="pion P=(0,0,0) A1um SS_0", irrep="A1um", size_matrix=1, psq="PSQ0_", hadron_type="meson"), 
    HadronData(file_name='pion_dsq1', operator="pion P=(0,0,1) A2m SS_1", irrep="A2m", size_matrix=1, psq="PSQ1_", hadron_type="meson"), 
    HadronData(file_name='pion_dsq2', operator="pion P=(0,1,1) A2m SS_0", irrep="A2m", size_matrix=1, psq="PSQ2_", hadron_type="meson"), 
    HadronData(file_name='pion_dsq3', operator="pion P=(1,1,1) A2m SS_0", irrep="A2m", size_matrix=1, psq="PSQ3_", hadron_type="meson"),
    ]

kaon = [
    HadronData(file_name='kaon_dsq0', operator="kaon P=(0,0,0) A1u SS_0", irrep="A1u", size_matrix=1, psq="PSQ0_", hadron_type="meson"), 
    HadronData(file_name='kaon_dsq1', operator="kaon P=(0,0,1) A2 SS_1", irrep="A2", size_matrix=1, psq="PSQ1_", hadron_type="meson"), 
    HadronData(file_name='kaon_dsq2', operator="kaon P=(0,1,1) A2 SS_0", irrep="A2", size_matrix=1, psq="PSQ2_", hadron_type="meson"), 
    HadronData(file_name='kaon_dsq3', operator="kaon P=(1,1,1) A2 SS_0", irrep="A2", size_matrix=1, psq="PSQ3_", hadron_type="meson"),
    ]

nucleon_baryon = [
    HadronData(file_name='nucleon_dsq0', operator="nucleon P=(0,0,0) G1g SS_0", irrep="G1g", size_matrix=1, psq="PSQ0_", hadron_type="baryon"), 
    HadronData(file_name='nucleon_dsq1', operator= "nucleon P=(0,0,1) G1 SS_0", irrep="G1", size_matrix=1, psq="PSQ1_", hadron_type="baryon"), 
    HadronData(file_name='nucleon_dsq2', operator="nucleon P=(0,1,1) G SS_0", irrep="G", size_matrix=1, psq="PSQ2_", hadron_type="baryon"), 
    HadronData(file_name='nucleon_dsq3', operator="nucleon P=(1,1,1) G SS_0", irrep="G", size_matrix=1, psq="PSQ3_", hadron_type="baryon"),
    HadronData(file_name='nucleon_dsq4', operator="nucleon P=(0,0,2) G1 SS_0", irrep="G1", size_matrix=1, psq="PSQ4_", hadron_type="baryon"),
    ]


lambda_baryon = [
    HadronData(file_name='lambda_dsq0', operator="lambda P=(0,0,0) G1g SS_0", irrep="G1g", size_matrix=1, psq="PSQ0_", hadron_type="baryon"), 
    HadronData(file_name='lambda_dsq1', operator= "lambda P=(0,0,1) G1 SS_0", irrep="G1", size_matrix=1, psq="PSQ1_", hadron_type="baryon"), 
    HadronData(file_name='lambda_dsq2', operator="lambda P=(0,1,1) G SS_0", irrep="G", size_matrix=1, psq="PSQ2_", hadron_type="baryon"), 
    HadronData(file_name='lambda_dsq3', operator= "lambda P=(1,1,1) G SS_0", irrep="G", size_matrix=1, psq="PSQ3_", hadron_type="baryon"),
    HadronData(file_name='lambda_dsq4', operator="lambda P=(0,0,2) G1 SS_0", irrep="G1", size_matrix=1, psq="PSQ4_", hadron_type="baryon"),
    ]

sigma_baryon = [
    HadronData(file_name='sigma_dsq0', operator="sigma P=(0,0,0) G1g SS_0", irrep="G1g", size_matrix=1, psq="PSQ0_", hadron_type="baryon"), 
    HadronData(file_name='sigma_dsq1', operator= "sigma P=(0,0,1) G1 SS_0", irrep="G1", size_matrix=1, psq="PSQ1_", hadron_type="baryon"), 
    HadronData(file_name='sigma_dsq2', operator="sigma P=(0,1,1) G SS_0", irrep="G", size_matrix=1, psq="PSQ2_", hadron_type="baryon"), 
    HadronData(file_name='sigma_dsq3', operator="sigma P=(1,1,1) G SS_0", irrep="G", size_matrix=1, psq="PSQ3_", hadron_type="baryon"),
    HadronData(file_name='sigma_dsq4', operator="sigma P=(0,0,2) G1 SS_0", irrep="G1", size_matrix=1, psq="PSQ4_", hadron_type="baryon"),
    ]

xi_baryon = [
    HadronData(file_name='xi_dsq0', operator="xi P=(0,0,0) G1g SS_0", irrep="G1g", size_matrix=1, psq="PSQ0_", hadron_type="baryon"), 
    HadronData(file_name='xi_dsq1', operator= "xi P=(0,0,1) G1 SS_0", irrep="G1", size_matrix=1, psq="PSQ1_", hadron_type="baryon"), 
    HadronData(file_name='xi_dsq2', operator="xi P=(0,1,1) G SS_0", irrep="G", size_matrix=1, psq="PSQ2_", hadron_type="baryon"), 
    HadronData(file_name='xi_dsq3', operator="xi P=(1,1,1) G SS_0", irrep="G", size_matrix=1, psq="PSQ3_", hadron_type="baryon"),
    HadronData(file_name='xi_dsq4', operator="xi P=(0,0,2) G1 SS_0", irrep="G1", size_matrix=1, psq="PSQ4_", hadron_type="baryon"),
    ]


the_list_of_SH = (pion + kaon + lambda_baryon + sigma_baryon + xi_baryon)
