import pandas as pd

def readData(dataPath):
    data=pd.read_csv(dataPath,header=None,names=["username","passwd","email","RealAddress","RealCity","RealCounty","RealProvince","IsInCampus"])
    return data.values

if __name__ == '__main__':
    data = readData("../data/user.csv")
    print(data)