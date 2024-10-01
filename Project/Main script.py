import pandas as pd
from fetch_activesubstances import fetch_activesubstances   # file for fetching active substances
from compare_ingredients import save_sorted_ingredients, save_unique_ingredients # file for comparing substances
from search_ingredients import search_main_ingredient # file for searching substances
from fetch_products_from_api import fetch_products_from_api_by_spl_id  # file for fetching products by SPL ID
from product_exporter import ask_to_export  # Import the export functions


# Define the path for the output CSV file
output_file_path = 'initial_unique_activesubstances.csv'

def fetch_active_substances():
    """
    Function to prompt the user to fetch active substances from the FDA API.
    """
    print("Do you want to fetch active substances from the FDA API? (y/n)")
    user_choice = input('Please type 1 for yes and 0 for no: ')
    
    if user_choice == '1':
        fetch_activesubstances(output_file_path)
        print('File has been created')
    else:
        print("Skipping data fetch from the FDA API.")


def process_ingredients():
    """
    Function to process ingredients: sorting and saving unique ingredients.
    """
    input_file_path = 'initial_unique_activesubstances.csv'
    output_file_path_sorted = 'sorted_active_ingredients.csv'  # For the sorted ingredients
    output_file_path_unique = 'unique_active_ingredients.csv'  # For the unique ingredients
    
    # Save the alphabetically sorted CSV
    save_sorted_ingredients(input_file_path, output_file_path_sorted)
    
    # Save the unique ingredients CSV
    save_unique_ingredients(input_file_path, output_file_path_unique)

    print("Ingredients processing completed.")


def search_and_fetch_products():
    """
    Function to search for a main ingredient and fetch related products by SPL ID from the FDA API.
    """
    main_ingredients_path = 'unique_active_ingredients.csv'  # For the Main Ingredients
    ingredients_path = 'sorted_active_ingredients.csv'  # For the Ingredients

    # Ask the user for an ingredient to search
    search_ingredient = input("Please enter an ingredient to search for: ").strip()

    # Call the function to search and display the results, return matching DataFrame
    matching_ingredients_in_df = search_main_ingredient(main_ingredients_path, ingredients_path, search_ingredient)

    # Extract SPL IDs from the matching entries (if matching_ingredients_in_df is not None)
    if matching_ingredients_in_df is not None and not matching_ingredients_in_df.empty:
        spl_ids = matching_ingredients_in_df['spl_id'].tolist()  # Extract SPL IDs
        
        # Fetch products by SPL ID from the FDA API and return the product details DataFrame
        product_details_df = fetch_products_from_api_by_spl_id(spl_ids)
        
        # Check if product_details_df contains data before attempting to export
        if not product_details_df.empty:
            ask_to_export(product_details_df)
        else:
            print("No product details found to export.")
    else:
        print("No SPL IDs were found for the selected ingredient.")

def main():
    """
    Main function to orchestrate fetching, processing, and searching ingredients.
    """
    # Step 1: Optionally fetch active substances from the FDA API
    fetch_active_substances()
    
    # Step 2: Process ingredients (sorting and saving unique ingredients)
    process_ingredients()

    # Step 3: Search for ingredients and fetch products based on SPL ID
    search_and_fetch_products()


# Run the main function
if __name__ == "__main__":
    main()