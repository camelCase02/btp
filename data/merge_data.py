import pandas as pd

# File paths
inflation_file = "inflation_data.csv"
pmi_file = "pmi_data.csv"
factory_file = "factory_data.csv"
tractor_file = "tractor_sales_data.csv"

# Load the data
inflation_df = pd.read_csv(inflation_file)
pmi_df = pd.read_csv(pmi_file)
factory_df = pd.read_csv(factory_file)
tractor_df = pd.read_csv(tractor_file)

# Display the first few rows of each dataframe to inspect their structure
inflation_df.head(), pmi_df.head(), factory_df.head(), tractor_df.head()

# Merging all data on 'Year' and 'Month' using outer join to keep all records
merged_df = (inflation_df
             .merge(pmi_df, on=["Year", "Month"], how="outer")
             .merge(factory_df, on=["Year", "Month"], how="outer")
             .merge(tractor_df, on=["Year", "Month"], how="outer"))

# Save the merged data to a new CSV file
merged_file_path = "final_data.csv"
merged_df.to_csv(merged_file_path, index=False)

# Display first few rows of the merged dataset
merged_df.head(5)
