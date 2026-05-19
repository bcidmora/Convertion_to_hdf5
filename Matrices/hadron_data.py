from dataclasses import dataclass

@dataclass
class HadronData:
    operator: list
    sqr_mom: str
    irrep: str
    irrep_dim: int
    size_matrix: str
    

isodoublet_P0_G1g = ["xi P=(0,0,0) G1g SS_0",
                     "xi P=(0,0,0) G1g SS_1", 
                     "isodoublet_kbar_lambda G1g [P=(0,0,1) A2 SS_1] [P=(0,0,-1) G1 SS_0",
                     "isodoublet_pion_xi G1g [P=(0,0,1) A2m SS_1] [P=(0,0,-1) G1 SS_0"]

isodoublet_P0_G1u = ["xi P=(0,0,0) G1u SS_0",
                     "xi P=(0,0,0) G1u SS_1",
                     "xi P=(0,0,0) G1u SS_2",
                     "xi P=(0,0,0) G1u SS_3",
                     "isodoublet_kbar_sigma G1u [P=(0,0,0) A1u SS_0] [P=(0,0,0) G1g SS_0]",
                     "isodoublet_kbar_lambda G1u [P=(0,0,0) A1u SS_0] [P=(0,0,0) G1g SS_0]",
                     "isodoublet_pion_xi G1u [P=(0,0,0) A1um SS_0] [P=(0,0,0) G1g SS_0]",
                     "isodoublet_kbar_lambda G1u [P=(0,0,1) A2 SS_1] [P=(0,0,-1) G1 SS_0]",
                     "isodoublet_pion_xi G1u [P=(0,0,1) A2m SS_1] [P=(0,0,-1) G1 SS_0]",     
                     ]

isodoublet_P0_Hg = ["xi P=(0,0,0) Hg SS_0", 
                    "xi P=(0,0,0) Hg SS_1", 
                    "isodoublet_kbar_lambda Hg [P=(0,1,0) A2 SS_1] [P=(0,-1,0) G1 SS_0]",
                    "isodoublet_pion_xi Hg [P=(0,1,0) A2m SS_1] [P=(0,-1,0) G1 SS_0]"]

isodoublet_P0_Hu = ["xi P=(0,0,0) Hu SS_0", 
                    "xi P=(0,0,0) Hu SS_1", 
                    "isodoublet_pion_xi Hu [P=(0,0,0) A1um SS_0] [P=(0,0,0) Hg SS_0]", 
                    "isodoublet_kbar_lambda Hu [P=(0,1,0) A2 SS_1] [P=(0,-1,0) G1 SS_0]",
                    "isodoublet_pion_xi Hu [P=(0,1,0) A2m SS_1] [P=(0,-1,0) G1 SS_0]"]

isodoublet_P1_G1 = ["xi P=(0,0,1) G1 SS_0", 
                    "xi P=(0,0,1) G1 SS_1",
                    "xi P=(0,0,1) G1 SS_2",
                    "xi P=(0,0,1) G1 SS_3",
                    "xi P=(0,0,1) G1 SS_4",
                    "xi P=(0,0,1) G1 SS_5",
                    "xi P=(0,0,1) G1 SS_6",
                    "xi P=(0,0,1) G1 SS_7",
                    "xi P=(0,0,1) G1 SS_8",
                    "xi P=(0,0,1) G1 SS_9",
                    "isodoublet_kbar_sigma G1 [P=(0,0,0) A1u SS_0] [P=(0,0,1) G1 SS_0]",
                    "isodoublet_kbar_lambda G1 [P=(0,0,0) A1u SS_0] [P=(0,0,1) G1 SS_0]",
                    "isodoublet_pion_xi G1 [P=(0,0,0) A1um SS_0] [P=(0,0,1) G1 SS_0]",
                    "isodoublet_kbar_lambda G1 [P=(0,0,1) A2 SS_1] [P=(0,0,0) G1g SS_0]",                    
                    "isodoublet_pion_xi G1 [P=(0,0,1) A2m SS_1] [P=(0,0,0) G1g SS_0]"]

isodoublet_P1_G2 = ["xi P=(0,0,1) G2 SS_0",
                    "xi P=(0,0,1) G2 SS_1",
                    "xi P=(0,0,1) G2 SS_2",
                    "xi P=(0,0,1) G2 SS_4",
                    "isodoublet_pion_xi G2 [P=(0,0,0) A1um SS_0] [P=(0,0,1) G2 SS_0]"]

isodoublet_P2_G = ["xi P=(1,1,0) G SS_0",
                   "xi P=(1,1,0) G SS_1",
                   "xi P=(1,1,0) G SS_2",
                   "xi P=(1,1,0) G SS_3",
                   "xi P=(1,1,0) G SS_4",
                   "xi P=(1,1,0) G SS_5",
                   "xi P=(1,1,0) G SS_6",
                   "xi P=(1,1,0) G SS_7",
                   "xi P=(1,1,0) G SS_8",
                   "xi P=(1,1,0) G SS_9",
                   "xi P=(1,1,0) G SS_10",
                   "xi P=(1,1,0) G SS_11",
                   "xi P=(1,1,0) G SS_12",
                   "xi P=(1,1,0) G SS_13",
                   "isodoublet_kbar_sigma G [P=(0,0,0) A1u SS_0] [P=(1,1,0) G SS_0]",
                   "isodoublet_kbar_lambda G [P=(0,0,0) A1u SS_0] [P=(1,1,0) G SS_0]",
                   "isodoublet_pion_xi G [P=(0,0,0) A1um SS_0] [P=(1,1,0) G SS_0]",     
                   "isodoublet_kbar_lambda G [P=(0,1,0) A2 SS_1] [P=(1,0,0) G1 SS_0]",    
                   "isodoublet_kbar_lambda G CG_1 [P=(0,1,0) A2 SS_1] [P=(1,0,0) G1 SS_0]",
                   "isodoublet_pion_xi G [P=(0,1,0) A2m SS_1] [P=(1,0,0) G1 SS_0]",   
                   "isodoublet_pion_xi G CG_1 [P=(0,1,0) A2m SS_1] [P=(1,0,0) G1 SS_0]"]

isodoublet_P3_G = ["xi P=(1,1,1) G SS_0", 
                   "xi P=(1,1,1) G SS_1",
                   "xi P=(1,1,1) G SS_2",
                   "xi P=(1,1,1) G SS_3",
                   "xi P=(1,1,1) G SS_4",
                   "xi P=(1,1,1) G SS_5",
                   "xi P=(1,1,1) G SS_6",
                   "xi P=(1,1,1) G SS_7",
                   "xi P=(1,1,1) G SS_8",
                   "xi P=(1,1,1) G SS_9",
                   "isodoublet_kbar_sigma G [P=(0,0,0) A1u SS_0] [P=(1,1,1) G SS_0]",
                   "isodoublet_kbar_lambda G [P=(0,0,0) A1u SS_0] [P=(1,1,1) G SS_0]",  
                   "isodoublet_pion_xi G [P=(0,0,0) A1um SS_0] [P=(1,1,1) G SS_0]"]

isodoublet_P3_F1 = ["xi P=(1,1,1) F1 SS_0",
                    "xi P=(1,1,1) F1 SS_1",
                    "xi P=(1,1,1) F1 SS_2",
                    "xi P=(1,1,1) F1 SS_3",
                    "isodoublet_kbar_lambda F1 [P=(0,0,1) A2 SS_1] [P=(1,1,0) G SS_0]",
                    "isodoublet_pion_xi F1 [P=(0,0,1) A2m SS_1] [P=(1,1,0) G SS_0]"]

isodoublet_P3_F2 = ["xi P=(1,1,1) F2 SS_0",
                    "xi P=(1,1,1) F2 SS_1",
                    "xi P=(1,1,1) F2 SS_2",
                    "xi P=(1,1,1) F2 SS_3",
                    "isodoublet_kbar_lambda F2 [P=(0,0,1) A2 SS_1] [P=(1,1,0) G SS_0]",
                    "isodoublet_pion_xi F2 [P=(0,0,1) A2m SS_1] [P=(1,1,0) G SS_0]"]

isodoublet_P4_G1 = ["xi P=(0,0,2) G1 SS_0",
                    "xi P=(0,0,2) G1 SS_1",
                    "xi P=(0,0,2) G1 SS_2",
                    "xi P=(0,0,2) G1 SS_3",
                    "xi P=(0,0,2) G1 SS_4",
                    "xi P=(0,0,2) G1 SS_5",
                    "xi P=(0,0,2) G1 SS_6",
                    "xi P=(0,0,2) G1 SS_7",
                    "xi P=(0,0,2) G1 SS_8",
                    "xi P=(0,0,2) G1 SS_9",
                    "isodoublet_kbar_sigma G1 [P=(0,0,0) A1u SS_0] [P=(0,0,2) G1 SS_0]",
                    "isodoublet_kbar_lambda G1 [P=(0,0,0) A1u SS_0] [P=(0,0,2) G1 SS_0]",
                    "isodoublet_pion_xi G1 [P=(0,0,0) A1um SS_0] [P=(0,0,2) G1 SS_0]",
                    "isodoublet_kbar_sigma G1 [P=(0,0,1) A2 SS_1] [P=(0,0,1) G1 SS_0]",
                    "isodoublet_kbar_lambda G1 [P=(0,0,1) A2 SS_1] [P=(0,0,1) G1 SS_0]",
                    "isodoublet_pion_xi G1 [P=(0,0,1) A2m SS_1] [P=(0,0,1) G1 SS_0]"]
    
    
the_list_of_xi = [
    HadronData(operator=isodoublet_P0_G1g, sqr_mom="0", irrep="G1g", irrep_dim=2, size_matrix=4),
    HadronData(operator=isodoublet_P0_G1u, sqr_mom="0", irrep="G1u", irrep_dim=2, size_matrix=9),
    HadronData(operator=isodoublet_P0_Hg, sqr_mom="0", irrep="Hg", irrep_dim=4, size_matrix=4),
    HadronData(operator=isodoublet_P0_Hu, sqr_mom="0", irrep="Hu", irrep_dim=4, size_matrix=5), 
    HadronData(operator=isodoublet_P1_G1, sqr_mom="1", irrep="G1", irrep_dim=2, size_matrix=15), 
    HadronData(operator=isodoublet_P1_G2, sqr_mom="1", irrep="G2", irrep_dim=2, size_matrix=5),
    HadronData(operator=isodoublet_P2_G, sqr_mom="2", irrep="G", irrep_dim=2, size_matrix=21), 
    HadronData(operator=isodoublet_P3_G, sqr_mom="3", irrep="G", irrep_dim=2, size_matrix=13), 
    HadronData(operator=isodoublet_P3_F1, sqr_mom="3", irrep="F1", irrep_dim=1, size_matrix=6), 
    HadronData(operator=isodoublet_P3_F2, sqr_mom="3", irrep="F2", irrep_dim=1, size_matrix=6),
    HadronData(operator=isodoublet_P4_G1, sqr_mom="4", irrep="G1", irrep_dim=2, size_matrix=16)]
    
