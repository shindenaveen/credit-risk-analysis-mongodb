import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def feature_selection(input_csv, output_csv, target):
    df = pd.read_csv(input_csv)
    
    # Separate features and target
    X = df.drop(target, axis=1)
    y = df[target]
    
    # Convert categorical columns to one-hot encoding
    X_encoded = pd.get_dummies(X)
    
    # Fit RandomForest
    model = RandomForestClassifier(random_state=42)
    model.fit(X_encoded, y)
    
    # Get feature importances
    importances = model.feature_importances_
    
    # Select features with importance > 0.02
    selected_features = X_encoded.columns[importances > 0.02].tolist()
    
    # Since X_encoded has dummies, but original df does not,
    # select those columns from encoded X and add target
    selected_df = pd.concat([X_encoded[selected_features], y], axis=1)
    
    # Save selected features + target to output CSV
    selected_df.to_csv(output_csv, index=False)
    print(f"Selected features saved to {output_csv}: {selected_features}")

if __name__ == "__main__":
    feature_selection("mongo_data.csv", "selected.csv", target='default')
