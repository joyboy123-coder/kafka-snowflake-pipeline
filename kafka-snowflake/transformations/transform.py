import pandas as pd

def clean_data(raw_data):
    """Takes a list of messy JSON data and cleans it."""
    df = pd.DataFrame(raw_data)

    # Convert column names to uppercase
    df.columns = df.columns.str.upper()

    # Sort by ID
    df = df.sort_values('ID', ascending=True)

    # Clean text fields
    df['NAME'] = df['NAME'].str.title().str.strip()
    df['CITY'] = df['CITY'].str.title().str.strip()

    # Convert AGE to integer
    df['AGE'] = df['AGE'].astype(int)

    # Standardize email format
    df['EMAIL'] = df['EMAIL'].apply(lambda x: x.split('@')[0] + '@gmail.com')

    # Clean ADDRESS field
    df['ADDRESS'] = df['ADDRESS'].apply(lambda x: x.split(',')[0].strip())

    # Create timestamp column
    df['TIME_STAMP'] = pd.to_datetime(df['DATE'] + ' ' + df['TIME'])

    # Drop unwanted columns
    df.drop(columns=['PHONE_NUMBER', 'RANDOM_FIELD', 'SPECIAL_CHARS', 'DATE', 'TIME', 'INVALID_DATA'], inplace=True, errors='ignore')

    return df
