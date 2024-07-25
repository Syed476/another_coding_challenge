import pandas as pd
def analyze_jobs(df, columns):
    """
    Analyze the government jobs data.

    Args:
    df (pd.DataFrame): Cleaned DataFrame
    columns (dict): Dictionary with column names

    Returns:
    tuple: Jobs by department, Top 5 highest paying jobs
    """
    # Jobs by department
    if columns['department']:
        jobs_by_department = df[columns['department']].value_counts()
    else:
        jobs_by_department = pd.Series({"N/A": len(df)})

    # Top 5 highest paying jobs
    if columns['salary']:
        top_5_paying_jobs = df.nlargest(5, columns['salary'])
    else:
        top_5_paying_jobs = df.head()

    return jobs_by_department, top_5_paying_jobs