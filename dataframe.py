import pandas as pd
import numpy as np
import logging
from datetime import datetime
import os

# ========== Logging Setup ==========
log_file = 'employee_analysis.log'
logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # ========== Data Setup ==========
    logging.info("Starting DataFrame creation...")

    data = {
        'EmployeeID': range(101, 111),
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'],
        'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
        'Salary': [50000, 70000, 65000, 80000, 52000, 62000, 72000, 51000, 63000, 75000],
        'JoiningDate': pd.to_datetime(['2020-01-15', '2019-03-10', '2021-07-23', '2018-11-05', '2022-06-19',
                                       '2017-04-01', '2020-08-08', '2023-01-01', '2016-12-12', '2022-10-10']),
        'PerformanceRating': [3, 4, 3, 5, 2, 4, 4, 3, 5, 4]
    }

    df = pd.DataFrame(data)

    # ========== Feature Engineering ==========
    logging.info("Calculating Experience...")
    df['Experience'] = (pd.to_datetime('today') - df['JoiningDate']).dt.days // 365

    logging.info("Calculating SalaryGrade using conditions...")
    conditions = [
        (df['Salary'] >= 75000),
        (df['Salary'] >= 65000) & (df['Salary'] < 75000),
        (df['Salary'] < 65000)
    ]
    choices = ['A', 'B', 'C']
    df['SalaryGrade'] = np.select(conditions, choices, default='Unknown')

    logging.info("Ranking performance within departments...")
    df['PerfRank'] = df.groupby('Department')['PerformanceRating'].rank(method='dense', ascending=False)

    logging.info("Calculating bonus based on performance...")
    df['Bonus'] = df.apply(lambda row: round((row['Salary'] * row['PerformanceRating']) / 100, 2), axis=1)

    logging.info("Calculating rolling average salary...")
    df['RollingSalaryAvg'] = df['Salary'].rolling(window=3).mean()

    # ========== Analysis ==========
    logging.info("Generating department-wise average metrics...")
    dept_summary = df.groupby('Department')[['Salary', 'PerformanceRating']].mean().reset_index()

    logging.info("Extracting top 3 highest paid employees...")
    top_3_paid = df.nlargest(3, 'Salary')

    logging.info("Filtering high performers with above-average salary...")
    mean_salary = df['Salary'].mean()
    mean_perf = df['PerformanceRating'].mean()
    high_achievers = df[(df['Salary'] > mean_salary) & (df['PerformanceRating'] > mean_perf)]

    logging.info("Identifying promotion watchlist candidates...")
    promotion_watchlist = df[df['PerfRank'] == 1].sort_values(by='Experience', ascending=False)

    # ========== Output ==========
    report_dir = f'reports/{datetime.now():%Y%m%d_%H%M%S}'
    os.makedirs(report_dir, exist_ok=True)
    df.to_csv('reports/employee_full_report.csv', index=False)
    dept_summary.to_csv('reports/department_summary.csv', index=False)
    top_3_paid.to_csv('reports/top_3_paid.csv', index=False)
    high_achievers.to_csv('reports/high_achievers.csv', index=False)
    promotion_watchlist.to_csv('reports/promotion_watchlist.csv', index=False)

    logging.info("Reports successfully generated in the 'reports/' folder.")

except Exception as e:
    logging.error(f"An error occurred: {e}")
    print("Oops! Something broke. Check the logs for more info.")
else:
    print("✅ Analysis complete. Check 'reports/' for CSV outputs.")
