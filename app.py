from flask import Flask
from web.routes import routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)



# from logic.csv_processor import process_csv

# result = process_csv("sample_data.csv")
# print(result)

# # import pandas as pd

# # def load_csv(file_path):
# #     """
# #     Load a CSV file into a pandas DataFrame.
# #     """
# #     try:
# #         df = pd.read_csv(file_path)
# #         return df
# #     except Exception as e:
# #         print(f"Error loading CSV file: {e}")
# #         return None


# # if __name__ == "__main__":
# #     file_path = "sample_data.csv"
# #     data = load_csv(file_path)

# #     if data is not None:
# #         print("CSV loaded successfully!")
# #         print("Shape (rows, columns):", data.shape)
# #         print("\nColumn names:")
# #         print(data.columns)
# #         print("\nFirst 5 rows:")
# #         print(data.head())
