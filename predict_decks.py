import pandas as pd
import numpy as np
from sklearn.externals import joblib

model = joblib.load('trained_model.pkl')

# Input decks
x = []
for i in range(2):
  d = pd.read_csv(f'deck{i+1}.csv')
  x.append(d)

# Process decks
selected_columns = ['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'height', 'weight']
for i in range(2):
  # Select features
  x[i] = x[i][selected_columns]
  # Fill missing values
  imp = SimpleImputer(strategy='mean')
  x[i] = imp.fit_transform(x[i])
  # Scale data
  scaler = StandardScaler()
  x[i] = scaler.fit_transform(x[i])

d1, d2 = x
scores = []

# Run decks against each other multiple times
for i in range(100):
  # Run deck against each other
  y1, y2 = model.predict(d1), model.predict(d2)
  scores.append(np.mean(y1 > y2))

# Obtain prediction results
wins_player_1 = np.ceil(np.mean(scores)*100)
wins_player_2 = 100 - wins_player_1
print(f'Player 1 wins {wins_player_1}% of the time.')
print(f'Player 2 wins {wins_player_2}% of the time.')