import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load preprocessed data
preprocessed_data = pd.read_csv('preprocessed_data.csv')
# Labels (outcome of battle between two decks)
labels = preprocessed_data['winner']
# Drop labels
data = preprocessed_data.drop(['winner'], axis=1)
# Split data into train/test sets
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
# Train model using Random Forest Classifier
clf = RandomForestClassifier(n_estimators=10, max_depth=None, random_state=42)
clf.fit(x_train, y_train)
# Evaluate model performance
predictions = clf.predict(x_test)
acc = accuracy_score(y_test, predictions)
print(f'Accuracy score: {acc}')
