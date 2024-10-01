import pandas as pd

def save_sorted_ingredients(input_file_path, output_file_path_sorted):
    """
    Function to alphabetically sort active ingredients and save to a CSV file.
    
    Parameters:
    input_file_path (str): The path to the input CSV file.
    output_file_path_sorted (str): The path where the sorted CSV file will be saved.
    
    Returns:
    None
    """
    
    # Load the input CSV file
    df = pd.read_csv(input_file_path)
    
    # Sort the DataFrame by the Ingredients column alphabetically
    df_sorted = df.sort_values(by="Main ingredient", ascending=True)
    length_df_sorted = len(df_sorted)
    # Save the sorted data to the first output CSV file
    df_sorted.to_csv(output_file_path_sorted, index=False)
    
    print(f"Alphabetically sorted CSV has been saved to {output_file_path_sorted}")
    print(f"Total active ingredients found: {length_df_sorted}")


def save_unique_ingredients(input_file_path, output_file_path_unique):
    """
    Function to save unique active ingredients (only one entry per ingredient) to a CSV file.
    
    Parameters:
    input_file_path (str): The path to the input CSV file.
    output_file_path_unique (str): The path where the unique ingredients CSV will be saved.
    
    Returns:
    None
    """
    
    # Load the input CSV file
    df = pd.read_csv(input_file_path)
    
    # Drop duplicate ingredients
    df_unique = df.drop_duplicates(subset="Main ingredient")
    length_df_unique = len(df_unique)
    # Sort the unique ingredients alphabetically
    df_unique_sorted = df_unique.sort_values(by="Main ingredient", ascending=True)
    
    # Save the unique and sorted ingredients to the second output CSV file
    df_unique_sorted.to_csv(output_file_path_unique, index=False)
    
    print(f"Unique ingredients CSV has been saved to {output_file_path_unique}")
    print(f"Total unique active ingredients found: {length_df_unique}")
    print(f'Dubble entries: {len(df) - len(df_unique)}')