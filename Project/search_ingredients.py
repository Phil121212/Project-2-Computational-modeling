import pandas as pd
import pandas as pd

def search_main_ingredient(main_ingredients_path, ingredients_path, search_ingredient):
    """
    Function to search for a main ingredient and return matching entries from the Ingredients file.
    
    Parameters:
    main_ingredients_path (str): Path to the CSV file with Main Ingredients.
    ingredients_path (str): Path to the CSV file with Ingredients.
    search_ingredient (str): The ingredient to search for.
    
    Returns:
    pd.DataFrame: DataFrame containing the matching entries from the Ingredients file, or None if no matches found.
    """
    
    # Load the Main Ingredients and Ingredients data
    Main_Ingredients = pd.read_csv(main_ingredients_path)['Main ingredient'].tolist()
    Ingredients_df = pd.read_csv(ingredients_path)

    # Search for matches in the Main Ingredients list
    matching_main_ingredients = [
        ingredient for ingredient in Main_Ingredients 
        if isinstance(ingredient, str) and search_ingredient.lower() in ingredient.lower()
    ]

    if matching_main_ingredients:
        print("\nMatching Main Ingredients:")
        for index, ingredient in enumerate(matching_main_ingredients, start=1):
            print(f"{index}. {ingredient}")
    else:
        print("No matches found in Main Ingredients.")
        return None  # Return None if no matches are found

    # Ask the user to select a number from the list of matching Main Ingredients
    selection = int(input("\nPlease enter the number corresponding to the Main Ingredient: ")) - 1

    # Ensure the selection is valid
    if 0 <= selection < len(matching_main_ingredients):
        selected_main_ingredient = matching_main_ingredients[selection]
        print(f"\nYou selected: {selected_main_ingredient}")

        # Search for all entries in the Ingredients file that contain the selected Main Ingredient
        matching_ingredients_in_df = Ingredients_df[
            Ingredients_df['Ingredients'].str.contains(selected_main_ingredient, case=False, na=False)
        ]

        if not matching_ingredients_in_df.empty:
            print("\nMatching entries in the Ingredients file:")
            print(matching_ingredients_in_df)
            return matching_ingredients_in_df  # Return the DataFrame
        else:
            print("No matching entries found in the Ingredients file.")
            return None
    else:
        print("Invalid selection. Exiting.")
        return None