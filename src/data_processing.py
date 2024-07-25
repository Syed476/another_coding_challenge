import pandas as pd


def read_gov_jobs_data(file_path):
    """
    Read the CSV file containing government job postings.

    Args:
    file_path (str): Path to the CSV file

    Returns:
    pd.DataFrame: DataFrame containing the job data
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The CSV file is empty.")
    except pd.errors.ParserError:
        raise ValueError("Unable to parse the CSV file. Please check the file format.")


def clean_data(df):
    """
    Clean the government jobs data.

    Args:
    df (pd.DataFrame): Raw DataFrame

    Returns:
    pd.DataFrame: Cleaned DataFrame
    """
    # Handle missing values
    df = df.dropna()

    # Convert data types
    date_column = next((col for col in df.columns if 'date' in col.lower()), None)
    if date_column:
        df[date_column] = pd.to_datetime(df[date_column], errors='coerce')

    salary_column = next((col for col in df.columns if 'salary' in col.lower() or 'amount' in col.lower()), None)
    if salary_column:
        df[salary_column] = df[salary_column].replace('£', '', regex=True).replace(',', '', regex=True).astype(float)

    return df


def get_column_names(df):
    """
    Get the appropriate column names for analysis.

    Args:
    df (pd.DataFrame): DataFrame

    Returns:
    dict: Dictionary with column names
    """
    columns = {
        'date': next((col for col in df.columns if 'date' in col.lower()), None),
        'salary': next((col for col in df.columns if 'salary' in col.lower() or 'amount' in col.lower()), None),
        'department': next((col for col in df.columns if 'department' in col.lower()), None),
        'title': next((col for col in df.columns if 'title' in col.lower() or 'job' in col.lower()), None),
        'location': next((col for col in df.columns if 'location' in col.lower()), None)
    }
    return columns