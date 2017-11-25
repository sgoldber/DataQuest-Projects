import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
    data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
    all_enrollment = data["total_enrollment"].sum()
    print(all_enrollment)
    filter_col = [col for col in data if col.startswith('SCH_ENR')]
    #data = pd.to_numeric(data, errors='coerce')
    data = data[filter_col]
    sums = data.sum()
    sums = sums/all_enrollment
    print(sums)
