import requests
import pandas as pd

def fetch_activesubstances(output_file_path):
    url = "https://api.fda.gov/drug/label.json"
    activesubstances_set = set()

    skip = 0
    limit = 900  # Adjust limit based on your requirements

    # First request to get the total number of records
    response = requests.get(url, params={'limit': 1})

    if response.status_code == 200:
        total_records = response.json()['meta']['results']['total']
        print(f"Total records available: {total_records}")

        while skip < total_records:
            query_params = {
                'limit': limit,
                'skip': skip
            }

            response = requests.get(url, params=query_params)

            if response.status_code == 200:
                data = response.json()
                results = data.get('results', [])

                # Check if results exist
                if not results:
                    print(f"No results found for skip value: {skip}")
                    break

                for i, result in enumerate(results):
                    openfda_data = result.get('openfda', {}).get('substance_name', ['N/A'])
                    ID = result.get('openfda', {}).get('spl_id', ['N/A'])[0]

                    # Main ingredient and additional ingredients
                    main_ingredient = openfda_data[0] if openfda_data != ['N/A'] else 'N/A'
                    ingredients = ', '.join(openfda_data)  # All substances as a string

                    print(f"{i}. Main Ingredient: {main_ingredient}, All Ingredients: {ingredients}")

                    # Add both ID and ingredients to the set
                    activesubstances_set.add((ID, main_ingredient, ingredients))

                skip += limit
            else:
                print(f"Error fetching data from FDA API: {response.status_code}")
                break
    else:
        print(f"Error fetching total records: {response.status_code}")

    # Convert the set to a sorted list to ensure uniqueness
    unique_activesubstances = sorted(list(activesubstances_set))

    # Save the unique active ingredients and IDs to a CSV file
    pd.DataFrame(unique_activesubstances, columns=["spl_id","Main ingredient", "Ingredients"]).to_csv(output_file_path, index=False)
    print(f"Active ingredients have been saved to {output_file_path}")
    print(f"Total unique active ingredients found: {len(unique_activesubstances)}")