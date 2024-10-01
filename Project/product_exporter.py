import pandas as pd

def export_to_excel(df, file_name):
    """
    Function to export a DataFrame to an Excel file using openpyxl engine.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to export.
    file_name (str): The desired name of the Excel file.
    """
    df.to_excel(file_name, index=False, engine='openpyxl')
    print(f"Data exported to {file_name}")


def ask_to_export(df):
    """
    Function to ask the user if they want to export the DataFrame as an Excel file.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to potentially export.
    """
    export_choice = input("Do you want to export the data as an Excel file? (y/n): ").strip().lower()
    
    if export_choice == 'y':
        file_name = input("Enter the name of the Excel file (without extension): ").strip()
        
        # Ensure the file name has the correct extension
        if not file_name.endswith('.xlsx'):
            file_name += '.xlsx'
        
        export_to_excel(df, file_name)
    else:
        print("Skipping Excel export.")