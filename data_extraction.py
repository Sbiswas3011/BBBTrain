import pandas as pd 

negdata1_file_path = "BBB_Data/B3Pred Dataset 1 negative Training.txt"
posdata1_file_path = "BBB_Data/B3Pred Dataset 1 positive training.txt" 
negdata2_file_path = "BBB_Data/B3Pred Dataset 2 Negative Training.txt" 
posdata2_file_path = "BBB_Data/B3Pred Dataset 2 Positive training.txt" 
file_paths = [posdata1_file_path,posdata2_file_path,negdata1_file_path,negdata2_file_path]

negdata = []
posdata = []
count = 0
for files in file_paths:
    with open(files, "r") as file:
        for line in file:
            if line.strip().startswith(">"):
                continue
            elif count == 0 or count == 1:
                posdata.append(line.strip())
            elif count == 2 or count == 3:
                negdata.append(line.strip())
        count += 1

columns = ["Proteins"]

posdf = pd.DataFrame(posdata, columns=columns)
posdf.to_csv("BBB_Data/PosData.csv", index=False)
negdf = pd.DataFrame(posdata, columns=columns)
negdf.to_csv("BBB_Data/NegData.csv", index=False)