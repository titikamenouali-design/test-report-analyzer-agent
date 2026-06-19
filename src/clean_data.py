import pandas as pd


def clean_data(df):
    """
    Clean and normalize test results.
    """

    # Normalisation des noms de colonnes
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # Normalisation de la colonne result
    if "result" in df.columns:

        df["result"] = (
            df["result"]
            .fillna("EMPTY")
            .astype(str)
            .str.strip()
            .str.upper()
        )

        result_mapping = {
            "PASSED": "PASS",
            "OK": "PASS",
            "ACCEPTED": "PASS",

            "FAILED": "FAIL",
            "NOK": "FAIL",
            "NOT OK": "FAIL",
            "REJECTED": "FAIL"
        }

        df["result"] = df["result"].replace(result_mapping)

        # Gestion des valeurs vides
        df.loc[df["result"].isin(["", "NAN"]), "result"] = "EMPTY"

    return df
