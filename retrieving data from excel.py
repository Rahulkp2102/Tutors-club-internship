import pandas as pd


def get_data(filename, sheet_name):
  # Read the Excel file
  df = pd.read_excel(filename, sheet_name=sheet_name)

  # Convert the dataframe to a list of rows
  rows = df.values.tolist()

  return rows

# Example usage
filename = 'tutorsclubexcel.xlsx'
sheet_name = 'student_info'
results = get_data(filename, sheet_name)

# Print the results
for row in results:
  print(row)

