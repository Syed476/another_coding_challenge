import pytest
import pandas as pd
from src.data_processing import read_gov_jobs_data, clean_data, get_column_names
from src.analysis import analyze_jobs

def test_read_gov_jobs_data():
    with pytest.raises(FileNotFoundError):
        read_gov_jobs_data("non_existent_file.csv")

def test_clean_data():
    test_df = pd.DataFrame({
        'Date Posted': ['2023-01-01', '2023-01-02'],
        'Salary': ['£50,000', '£60,000'],
        'Department': ['Department1', 'Department2'],
        'Job Title': ['Job1', 'Job2'],
        'Location': ['London', 'Manchester']
    })
    cleaned_df = clean_data(test_df)
    assert cleaned_df['Salary'].dtype == float
    assert cleaned_df['Date Posted'].dtype == 'datetime64[ns]'

def test_analyze_jobs():
    test_df = pd.DataFrame({
        'Date Posted': pd.to_datetime(['2023-01-01', '2023-01-02']),
        'Salary': [50000.0, 60000.0],
        'Department': ['Department1', 'Department2'],
        'Job Title': ['Job1', 'Job2'],
        'Location': ['London', 'Manchester']
    })
    columns = get_column_names(test_df)  # Get the column names
    jobs_by_department, top_5_paying_jobs = analyze_jobs(test_df, columns)  # Pass both arguments
    assert len(jobs_by_department) == 2
    assert len(top_5_paying_jobs) == 2