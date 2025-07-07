from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(X_train, y_train, save_path="model.pkl"):
    clf = RandomForestClassifier(class_weight='balanced', random_state=42)
    clf.fit(X_train, y_train)
    joblib.dump(clf, save_path)
    return clf

def load_model(path="model.pkl"):
    return joblib.load(path)
