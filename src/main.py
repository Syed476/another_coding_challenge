from src.data_processing import read_gov_jobs_data, clean_data, get_column_names
from src.analysis import analyze_jobs
import pandas as pd


def main(file_path):
    try:
        df = read_gov_jobs_data(file_path)
        cleaned_df = clean_data(df)
        columns = get_column_names(cleaned_df)
        jobs_by_department, top_5_paying_jobs = analyze_jobs(cleaned_df, columns)

        print("Jobs by Department:")
        print(jobs_by_department)
        print("\nTop 5 Highest Paying Jobs:")
        display_columns = [col for col in
                           [columns['title'], columns['department'], columns['salary'], columns['location']] if col]
        print(top_5_paying_jobs[display_columns])

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    file_path = "data/government_jobs.csv"
    main('../data/customer_data.csv')