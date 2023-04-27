import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
def preprocess_data(data):
    # Drop columns with constant values
    data = data.loc[:, (data != data.iloc[0]).any()]
    # Fill missing values
    imp = SimpleImputer(strategy='mean')
    data = imp.fit_transform(data)
    # Scale data
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    return data

# Read data using pandas
data = pd.read_csv('pokemon_tcg_api.csv')
# Select features
selected_columns = ['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'height', 'weight']
data = data[selected_columns]
# Preprocess data
preprocessed_data = preprocess_data(data)
# Save preprocessed data
pd.DataFrame(preprocessed_data).to_csv('preprocessed_data.csv', index=False)