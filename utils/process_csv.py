import pandas as pd

def csv_to_dict():
    df = pd.read_csv('profile.csv', delimiter=';')
    columns_dict = pd.Series(df["Terrain height [m a.s.l.]"].values, index=df["Distance from Tx [km]"]).to_dict()
    return columns_dict # keys = distances, values = heights
