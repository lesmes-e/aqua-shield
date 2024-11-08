import pandas as pd
from datetime import datetime

def load_water_quality_data():
    """Carga los datos del archivo CSV en un DataFrame de pandas."""
    try:
        df = pd.read_csv("data/water_quality_data.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=['date', 'location', 'nutrient_level', 'algae_growth', 'oxygen_level'])
        df.to_csv("data/water_quality_data.csv", index=False)
    return df

def save_new_entry(location, nutrient_level, algae_growth, oxygen_level):
    """Guarda una nueva entrada con los resultados del cálculo en el archivo CSV."""
    df = load_water_quality_data()
    
    new_data = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'location': location,
        'nutrient_level': nutrient_level,
        'algae_growth': algae_growth,
        'oxygen_level': oxygen_level
    }

    # Reemplazar df.append() con pd.concat()
    new_df = pd.DataFrame([new_data])  # Convertir new_data en un DataFrame
    df = pd.concat([df, new_df], ignore_index=True)  # Concatenar los DataFrames
    df.to_csv("data/water_quality_data.csv", index=False)
