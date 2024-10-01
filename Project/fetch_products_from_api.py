import requests
import pandas as pd

def fetch_products_from_api_by_spl_id(spl_ids):
    """
    Function to fetch and display products from the FDA API based on SPL IDs and return product details.
    
    Parameters:
    spl_ids (list): List of SPL IDs to search for.
    
    Returns:
    pd.DataFrame: DataFrame containing product details such as main ingredient, manufacturer, product name, etc.
    """
    
    base_url = "https://api.fda.gov/drug/label.json"
    product_details = []

    for spl_id in spl_ids:
        # Make a request to the FDA API with the SPL ID
        response = requests.get(base_url, params={"search": f"openfda.spl_id:{spl_id}"})
        
        if response.status_code == 200:
            data = response.json()
            
            # Check if there are any results
            if 'results' in data and len(data['results']) > 0:
                product_info = data['results'][0]  # Assuming the first result is the relevant one
                main_ingredient = ', '.join(product_info.get('openfda', {}).get('substance_name', ['N/A']))
                manufacturer_name = ', '.join(product_info.get('openfda', {}).get('manufacturer_name', ['N/A']))
                product_name = ', '.join(product_info.get('openfda', {}).get('brand_name', ['N/A']))

                # Append all the details to the product_details list
                product_details.append({
                    'Main Ingredient': main_ingredient,
                    'Manufacturer': manufacturer_name,
                    'Product Name': product_name
                })
            else:
                print(f"No product found for SPL ID {spl_id}.")
        else:
            print(f"Error fetching data for SPL ID {spl_id}: {response.status_code}")
    
    # Always return a DataFrame, even if no products were found
    return pd.DataFrame(product_details) if product_details else pd.DataFrame(columns=['Main Ingredient', 'Manufacturer', 'Product Name'])