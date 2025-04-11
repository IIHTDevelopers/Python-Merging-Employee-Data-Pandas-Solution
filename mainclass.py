import pandas as pd

class EmployeeDataAnalysis:
    def __init__(self, employee_file, salary_file):
        """Load CSV data into Pandas DataFrames."""
        self.employee_df = pd.read_csv(employee_file)
        self.salary_df = pd.read_csv(salary_file)
        self.merged_df = None

    def merge_data(self):
        """Merge employee and salary data on Employee_ID."""
        self.merged_df = pd.merge(self.employee_df, self.salary_df, on="Employee_ID")
        return self.merged_df

    def display_head(self):
        """Return the first 5 rows of the merged DataFrame."""
        return self.merged_df.head()

    def dataframe_info(self):
        """Return DataFrame column names and data types."""
        return self.merged_df.info()

    def calculate_average_salary(self):
        """Calculate the average salary per department."""
        return self.merged_df.groupby("Department")["Salary"].mean()

    def save_to_excel(self, output_file="merged_employee_data.xlsx"):
        """Save the merged DataFrame to an Excel file."""
        self.merged_df.to_excel(output_file, index=False)
