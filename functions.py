import pandas as pd
import requests
import re
import zipfile
import io

def ga1_q12(question, files):
    print("Function Called")
    symbols = question.split(' OR ')
    symbols[0] = symbols[0][-1]
    symbols[-1] = symbols[-1][0]
    # sumer = 0
    # csv_data = {}
    # with zipfile.ZipFile("q-unicode-data.zip", 'r') as zip_ref:
    #     print("Files in ZIP:", zip_ref.namelist())
    #     decode = ["cp1252","UTF-8","UTF-16"]
    #     for i,file_name in enumerate(zip_ref.namelist()):
    #         if file_name.endswith('.csv') or file_name.endswith('.txt'):
    #             with zip_ref.open(file_name) as f:
    #                 csv_content = f.read().decode(decode[i])
    #                 df = pd.read_csv(io.StringIO(csv_content))
    #                 csv_data[file_name] = df
    # for i in csv_content:
    #     curr_data = csv_content[i]
    #     sumer += curr_data[(curr_data["symbol"] == "‘") | (curr_data["symbol"] == "‡") | (curr_data["symbol"] == "œ")]["value"].sum()
    # return sumer