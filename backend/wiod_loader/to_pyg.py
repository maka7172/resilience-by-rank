import torch
from torch_geometric.data import Data
import pandas as pd, glob, os

DATA_DIR = "data/wiod2016"

class WIOD2PyG:
    @staticmethod
    def year(year):
        path = f"{DATA_DIR}/WIOT{year}_Nov16_ROW.xlsb"
        df = pd.read_excel(path, sheet_name=None, engine="pyxlsb")
        sheet = list(df.keys())[0]
        df = df[sheet]

        # ساخت یک نمونه ساده: گراف کامل با وزن ۱
        n = len(df)
        edge_index = torch.combinations(torch.arange(n), r=2).T
        edge_weight = torch.ones(edge_index.size(1))
        return Data(edge_index=edge_index, edge_weight=edge_weight, num_nodes=n)

if __name__ == "__main__":
    data = WIOD2PyG.year(2000)
    print("Graph 2000:", data)