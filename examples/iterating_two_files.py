import os
import similarity_calc
import making_excel
import pandas as pd


def separate_numbers(code_string):
    # Remove the "risk_factors_" prefix
    code = code_string.replace("risk_factors_", "")
    # Split the remaining string into separate numbers
    numbers = code.split("-")
    return numbers

def process_files(folder_path):
    risk_factor_files = [f for f in os.listdir(folder_path) if f.startswith("risk_factors")]
    risk_factor_files.sort()

    for i in range(0, len(risk_factor_files) - 1):
        file1 = risk_factor_files[i]
        name1 = file1
        file2 = risk_factor_files[i+1]
        name2 = file2
        process_pair_of_files(os.path.join(folder_path, file1), os.path.join(folder_path, file2), name1, name2, folder_path)

def process_pair_of_files(file1, file2, name1, name2, folder_path):
    print("Processing files: {} and {}".format(file1, file2))
    
    #open files
    with open(file1, "r", encoding='utf-8') as f:
        text1 = f.read()
    with open(file2, "r", encoding='utf-8') as f:
        text2 = f.read()

    cosine = similarity_calc.cosine_similarity(text1, text2)
    jaccard = similarity_calc.jaccard_similarity(text1, text2)
    levenshtein = similarity_calc.levenshtein_distance(text1, text2)

    similarity = (cosine + jaccard + levenshtein)/3
    (txt, diff) = similarity_calc.find_longest(text1, text2)

    num1 = separate_numbers(name1)
    num2 = separate_numbers(name2)

    cik = int(num1[0])
    years = f"{int(num1[1])}-{int(num2[1])}"

    # ---------- ADD ROW TO EXCEL ----------
    df = pd.read_excel(f'{folder_path}\output.xlsx') 
    making_excel.append_excel(folder_path, df, cik, years, similarity, txt, diff)

   

