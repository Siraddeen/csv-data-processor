import pandas as pd

MAX_PREVIEW_ROWS = 1000

def process_csv(csv_file, preview_rows: int = MAX_PREVIEW_ROWS):
    df = pd.read_csv(csv_file)

    rows, columns = df.shape
    column_names = list(df.columns)

    duplicate_count = df.duplicated().sum()
    df_cleaned = df.drop_duplicates()

    missing_values = df_cleaned.isna().sum().to_dict()

    preview_data = (
        df_cleaned.head(preview_rows)
        .fillna("N/A")
        .to_dict(orient="records")
    )

    return {
        "rows": rows,
        "columns": columns,
        "column_names": column_names,
        "duplicate_rows": int(duplicate_count),
        "missing_values": missing_values,
        "preview": preview_data
    }


# import pandas as pd

# MAX_PREVIEW_ROWS = 1000

# def process_csv(csv_file, preview_rows: int = MAX_PREVIEW_ROWS):
#     df = pd.read_csv(csv_file)

#     rows, columns = df.shape
#     column_names = list(df.columns)

#     duplicate_count = df.duplicated().sum()
#     df_cleaned = df.drop_duplicates()

#     missing_values = df_cleaned.isna().sum().to_dict()

#     preview_data = (
#         df_cleaned.head(preview_rows)
#         .fillna("N/A")
#         .to_dict(orient="records")
#     )

#     result = {
#         "rows": rows,
#         "columns": columns,
#         "column_names": column_names,
#         "duplicate_rows": int(duplicate_count),
#         "missing_values": missing_values,
#         "preview": preview_data,
#         "cleaned_df": df_cleaned   # ← important
#     }

#     return result

# # import pandas as pd

# # MAX_PREVIEW_ROWS = 1000
# # def process_csv(csv_file, preview_rows: int = MAX_PREVIEW_ROWS):
# #     """
# #     Process a CSV file and return structured insights.

# #     Parameters:
# #         csv_file: file path (str) or file-like object
# #         preview_rows: number of rows to preview

# #     Returns:
# #         dict with CSV insights
# #     """

# #     # Load CSV
# #     df = pd.read_csv(csv_file)

# #     # Basic info
# #     rows, columns = df.shape
# #     column_names = list(df.columns)

# #     # Duplicate handling
# #     duplicate_count = df.duplicated().sum()
# #     df_deduplicated = df.drop_duplicates()

# #     # Missing values
# #     missing_values = df.isna().sum().to_dict()

# #     # Preview rows (convert to records for JSON/HTML friendliness)
# #     preview_data = (
# #         df_deduplicated.head(preview_rows)
# #         .fillna("N/A")
# #         .to_dict(orient="records")
# #     )

# #     # Final structured result
# #     result = {
# #         "rows": rows,
# #         "columns": columns,
# #         "column_names": column_names,
# #         "duplicate_rows": int(duplicate_count),
# #         "missing_values": missing_values,
# #         "preview": preview_data,
# #     }

# #     return result
