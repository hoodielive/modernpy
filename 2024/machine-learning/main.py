from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

data = [
    ("Free entry in a competition to win!", "spam"),
    ("Call me now", "spam"),
    ("Hello, how are you?", "not spam"),
    ("Important meeting tomorrow", "not spam"),
    ("Win a brand-new car!", "spam"),
    ("Can we meet for coffee?", "not spam")
]

# Split the data into text and labels
texts, labels = zip(*data)

# Convert text data into numerical features using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts) # features (word counts)
y = labels # Labels

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Example prediction
new_text = ["Congratulations, you've won the prize!"]
new_text_features = vectorizer.transform(new_text)
prediction = model.predict(new_text_features)
print(f"Prediction for '{new_text[0]}': {prediction[0]}")
