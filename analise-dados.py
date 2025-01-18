import pandas as pd

# Load the dataset
# For this example, let's assume we have a CSV file named 'data.csv'
dataset_path = 'data.csv'
df = pd.read_csv(dataset_path)

# Display the first few rows of the dataframe
print("First 5 rows of the dataset:")
print(df.head())

# Display basic information about the dataset
print("\nDataset Information:")
print(df.info())

# Display basic statistics of the dataset
print("\nBasic Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Example analysis: Finding the correlation between numerical columns
print("\nCorrelation Matrix:")
print(df.corr())

# Example analysis: Grouping data by a specific column and calculating mean
# Assuming there's a column named 'category' and we want to group by this column
if 'category' in df.columns:
    print("\nMean values grouped by 'category':")
    print(df.groupby('category').mean())

# Example analysis: Filtering the dataset based on a condition
# Assuming there's a column named 'value' and we want to filter rows where 'value' > 50
filtered_df = df[df['value'] > 50]
print("\nRows where 'value' > 50:")
print(filtered_df)

# Save the filtered data to a new CSV file
filtered_df.to_csv('filtered_data.csv', index=False)

print("\nFiltered data has been saved to 'filtered_data.csv'")