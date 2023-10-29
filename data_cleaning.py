import pandas as pd 
from Bio.SeqUtils.ProtParam import ProteinAnalysis

pos_file_path = 'BBB_Data/PosData.csv'
neg_file_path = 'BBB_Data/NegData.csv'

pos_df = pd.read_csv(pos_file_path)
pos_df['Value'] = 1
neg_df = pd.read_csv(neg_file_path)
neg_df['Value'] = 0

combined_df = pd.concat([pos_df, neg_df], ignore_index=True)
combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)

aa_counts = []
aa_percentages = []
molecular_weights = []
aromaticities = []
instability_indices = []
isoelectric_points = []
helix_fractions = []
reduced_extinction_coefficients = []
oxidized_extinction_coefficients = []

for i, sequence in combined_df.iterrows():
    X = ProteinAnalysis(sequence['Proteins'])

    # Calculate properties for each peptide
    aa_count = X.count_amino_acids()
    aa_percentage = X.get_amino_acids_percent()
    mw = X.molecular_weight()
    aromaticity = X.aromaticity()
    instability_index = X.instability_index()
    isoelectric_point = X.isoelectric_point()
    sec_struc = X.secondary_structure_fraction()
    epsilon_prot = X.molar_extinction_coefficient()

    # Append results to respective lists
    aa_counts.append(aa_count)
    aa_percentages.append(aa_percentage)
    molecular_weights.append(mw)
    aromaticities.append(aromaticity)
    instability_indices.append(instability_index)
    isoelectric_points.append(isoelectric_point)
    helix_fractions.append(sec_struc[0])
    reduced_extinction_coefficients.append(epsilon_prot[0])
    oxidized_extinction_coefficients.append(epsilon_prot[1])

combined_df['AA_Counts'] = aa_counts
combined_df['AA_Percentages'] = aa_percentages
combined_df['Molecular_Weights'] = molecular_weights
combined_df['Aromaticities'] = aromaticities
combined_df['Instability_Indices'] = instability_indices
combined_df['Isoelectric_Points'] = isoelectric_points
combined_df['Helix_Fractions'] = helix_fractions
combined_df['Reduced_Extinction_Coefficients'] = reduced_extinction_coefficients
combined_df['Oxidized_Extinction_Coefficients'] = oxidized_extinction_coefficients

combined_df.to_csv("BBB_Data/CleanedData.csv", index=False)