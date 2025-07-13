import pandas as pd, os, glob

DATA_DIR = "data/wiod2016"

def load_all_years():
    pattern = os.path.join(DATA_DIR, "**", "WIOT*_Nov16_ROW.xlsb")
    files = glob.glob(pattern, recursive=True)
    if not files:
        raise FileNotFoundError("فایل‌های .xlsb در هیچ زیر-فولدری یافت نشد.")
    data = {}
    for f in files:
        year = int(os.path.basename(f).split("_")[0][4:])  # WIOT2000 -> 2000
        print("خواندن", f)
        # sheet_name=None → اولین شیت (همان سال)
        df = pd.read_excel(f, sheet_name=None, engine="pyxlsb")
        sheet_name = list(df.keys())[0]  # نام واقعی شیت
        data[year] = df[sheet_name]
    return data

if __name__ == "__main__":
    d = load_all_years()
    print("سال‌های موجود:", sorted(d.keys()))