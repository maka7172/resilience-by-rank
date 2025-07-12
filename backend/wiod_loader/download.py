# backend/wiod_loader/load_offline.py
import pandas as pd
import os, glob

DATA_DIR = "data/wiod2016"

def load_all_years():
    files = glob.glob(os.path.join(DATA_DIR, "WIOT*_Nov16_ROW.xlsx"))
    if not files:
        raise FileNotFoundError("فایل‌های WIOD در data/wiod2016 یافت نشد.")
    data = {}
    for f in files:
        year = int(os.path.basename(f).split("_")[1])
        data[year] = pd.read_excel(f, sheet_name="2016")  # یا sheet مناسب
    return data

if __name__ == "__main__":
    print("بارگذاری آفلاین WIOD...")
    d = load_all_years()
    print("سال‌های موجود:", list(d.keys()))