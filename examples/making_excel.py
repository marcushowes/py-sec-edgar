import pandas as pd

# Creating an excel document that displays the file name of all files that failed to extract 'Risk Factors'
def create_failed_excel(folderpath):
    df = pd.DataFrame(columns=['File Key'])
    df.to_excel(f'{folderpath}\failed_files.xlsx', index=False)

# Adding a row to the failed files excel
def append_failed_excel(folderpath, df, key):
    new_row = {'File Key': key}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_excel(f'{folderpath}\output.xlsx', index=False)

def create_excel(folderpath):
    # Create an empty DataFrame to store the data
    df = pd.DataFrame(columns=['CIK', 'Years', 'Similarity', 'Longer', 'Difference', 'Later Publish Date', 'Length 1', 'Length 2'])

    # Save the DataFrame to an Excel file in a specified folder
    df.to_excel(f'{folderpath}\output.xlsx', index=False)

# Function to add new row to excel
def append_excel(folderpath, df, cik, years, similarity, txt, diff, date, length1, length2):
    new_row = {'CIK': cik, 'Years': years, 'Similarity': similarity, 'Longer': txt, 'Difference': diff, 'Later Publish Date': date, 'Length 1': length1, 'Length 2': length2}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    # Save the DataFrame to an Excel file in a specified folder
    df.to_excel(f'{folderpath}\output.xlsx', index=False)


