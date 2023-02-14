import pandas as pd

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


