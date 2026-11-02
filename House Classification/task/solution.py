import os
import requests
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if 'house_class.csv' not in os.listdir('../Data'):
        sys.stderr.write("[INFO] Dataset is loading.\n")
        url = "https://www.dropbox.com/s/7vjkrlggmvr5bc1/house_class.csv?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/house_class.csv', 'wb').write(r.content)
        sys.stderr.write("[INFO] Loaded.\n")

    # # Stage 1
    df = pd.read_csv("house_class.csv")
    # # df.head()
    # rows, cols = list(df.shape)
    # a = sum(df.isna().sum())  # Are there any missing values in the DataFrame (True or False)
    # room_max = df['Room'].max()
    # area_mean = round(df['Area'].agg('mean'), 1)
    # unique_zip_loc = len(df['Zip_loc'].unique().tolist())
    #
    # print(rows, cols, bool(a), room_max, area_mean, unique_zip_loc, sep="\n")

    # Stage 2
    # Create two separate datasets X, y
    y = df['Price'].astype(int)
    X = df.drop('Price', axis=1)
    x_cols = X.columns.tolist()

    # Split the two datasets using the train_test_split function
    X_train, X_val, y_train, y_val = train_test_split(
        X.values, y.values,
        stratify=X['Zip_loc'].values,
        random_state=1,
        test_size=0.3
    )

    # Print the value count dictionary of the Zip_loc column
    X_train = pd.DataFrame(X_train, columns=x_cols)
    zip_loc_dict = X_train['Zip_loc'].value_counts().to_dict()

    # Result
    print(zip_loc_dict)
