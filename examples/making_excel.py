import pandas as pd

def create_excel(folderpath):
    # Create an empty DataFrame to store the data
    df = pd.DataFrame(columns=['CIK', 'Years', 'Similarity', 'Longer', 'Difference'])

    # Save the DataFrame to an Excel file in a specified folder
    df.to_excel(f'{folderpath}\output.xlsx', index=False)

# Function to add new row to excel
def append_excel(df, cik, years, similarity, txt, diff):
    new_row = {'CIK': cik, 'Years': years, 'Similarity': similarity, 'Longer': txt, 'Difference': diff}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    # Save the DataFrame to an Excel file in a specified folder
    df.to_excel(r'C:\sec_gov\Archives\edgar\data\732717\output.xlsx', index=False)


