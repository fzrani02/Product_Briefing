import pandas as pd

def load_database():
    return pd.read_csv("engineer_database.csv")


def get_customer_by_initial(df, initial):
    result = df[df["Initial"] == initial]

    if not result.empty:
        return result.iloc[0]["Customer"]

    return ""


def get_engineers_by_department(df, initial, department):
    data = df[
        (df["Initial"] == initial) &
        (df["Department"] == department)
    ]

    return data
