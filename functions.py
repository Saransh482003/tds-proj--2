import pandas as pd
import requests
import re
import zipfile
import io

def extract_zip_data(file_bytes):
    return zipfile.ZipFile(io.BytesIO(file_bytes), 'r')

def ga1_q12(question, file_bytes):
    symbols = question.split(' OR ')
    symbols[0] = symbols[0][-1]
    symbols[-1] = symbols[-1][0]
    csv_data = []
    zip_ref = extract_zip_data(file_bytes)
    decode = ["cp1252","UTF-8","UTF-16"]
    for i, file_name in enumerate(zip_ref.namelist()):
        if file_name.endswith('.csv'):
            with zip_ref.open(file_name) as f:
                csv_content = f.read().decode(decode[i])
                df = pd.read_csv(io.StringIO(csv_content))
                csv_data.append(df)

        elif file_name.endswith('.txt'):
            with zip_ref.open(file_name) as f:
                csv_content = f.read().decode(decode[i])
                df = pd.read_csv(io.StringIO(csv_content), sep="\t")
                csv_data.append(df)
    csv_data = pd.concat(csv_data)
    csv_data.reset_index(drop=True, inplace=True)
    sumer = csv_data[csv_data["symbol"].isin(symbols)]["value"].sum()
    return int(sumer)

