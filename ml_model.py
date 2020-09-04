import pickle

def classify(text):

    with open('vectorizer.pkl', 'rb') as file:
        cv = pickle.load(file)

    with open('spam_classifier.pkl', 'rb') as file:
        model = pickle.load(file)

    return model.predict(cv.transform([text]))

if __name__ == '__main__':
    print(classify(text))