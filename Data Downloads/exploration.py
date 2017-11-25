import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
    print(data["JJ"].value_counts())
    print(data["SCH_STATUS_MAGNET"].value_counts())
    
    pivot1 = pd.pivot_table(data, "TOT_ENR_M", columns=['JJ', 'SCH_STATUS_MAGNET'])
    pivot2 = pd.pivot_table(data, "TOT_ENR_F", columns=['JJ', 'SCH_STATUS_MAGNET'])
    print(pivot1)
    print(pivot2)
    