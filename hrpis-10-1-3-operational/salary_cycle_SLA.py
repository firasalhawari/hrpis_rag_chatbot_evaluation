# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 11:26:18 2025

@author: Firas.Alhawari
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import timedelta
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import calendar

# --- File path ---
file_path = r"./salary_posting.csv"

# --- Load CSV ---
df = pd.read_csv(file_path)

# --- Parse start/end dates ---
date_format = '%d-%b-%y %I.%M.%S.%f %p'
df['MIN_DATE_BULK'] = pd.to_datetime(df['MIN_DATE_BULK'], format=date_format, errors='coerce')
df['MAX_DATE_BULK'] = pd.to_datetime(df['MAX_DATE_BULK'], format=date_format, errors='coerce')

# --- Filter months ---
start_year, start_month = 2024, 2
end_year, end_month = 2025, 8
df = df[
    ((df['YEAR'] > start_year) | ((df['YEAR'] == start_year) & (df['MONTH'] >= start_month))) &
    ((df['YEAR'] < end_year) | ((df['YEAR'] == end_year) & (df['MONTH'] <= end_month)))
]

# --- Month-year for x-axis ---
df['month_year'] = pd.to_datetime(df['YEAR'].astype(str) + '-' + df['MONTH'].astype(str) + '-01')

# --- Cycle duration in minutes ---
df['cycle_minutes'] = df['DURATION_MINUTES_BULK']

# --- Compute SLA compliance: on time if MAX_DATE_BULK ≤ last Thursday of month ---
def last_thursday(year, month):
    last_day = calendar.monthrange(year, month)[1]
    d = pd.Timestamp(year=year, month=month, day=last_day)
    while d.weekday() != 3:  # Thursday
        d -= pd.Timedelta(days=1)
    return d

df['SLA_compliant'] = df.apply(lambda row: 1 if row['MAX_DATE_BULK'] <= last_thursday(row['YEAR'], row['MONTH']) else 0, axis=1)

# --- Aggregate SLA compliance by month ---
sla_monthly = df.groupby('month_year')['SLA_compliant'].mean() * 100  # %
cycle_monthly = df.groupby('month_year')['cycle_minutes'].mean()

# --- Plot 1: Cycle time per payroll run ---
#fig1, ax1 = plt.subplots(figsize=(12,5))
#ax1.scatter(df['month_year'], df['cycle_minutes'], color='orange', s=80)
#ax1.set_title('Bulk Salary Slip Generation Time for All Employees per Month', fontsize=14)
#ax1.set_xlabel('Month', fontsize=12)
#ax1.set_ylabel('Duration (minutes)', fontsize=12)
#ax1.grid(axis='y', linestyle='--', alpha=0.5, color='gray')
#ax1.xaxis.set_major_locator(mdates.MonthLocator())
#ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b-%Y'))
#plt.setp(ax1.get_xticklabels(), rotation=45, fontsize=12)
#plt.setp(ax1.get_yticklabels(), fontsize=12)
#fig1.tight_layout()
#fig1.savefig('cycle_time_per_month.png', dpi=300, bbox_inches='tight', facecolor='white')
#plt.show()

# --- Plot 2: SLA compliance per month ---
fig2, ax2 = plt.subplots(figsize=(12,5))
ax2.plot(sla_monthly.index, sla_monthly.values, marker='o', color='green', linewidth=2)
ax2.set_title('Monthly SLA Compliance (% Payroll Runs Completed by Last Thursday)', fontsize=14)
ax2.set_xlabel('Month', fontsize=14)
ax2.set_ylabel('SLA Compliance (%)', fontsize=14)
ax2.set_ylim(0, 110)
ax2.grid(axis='y', linestyle='--', alpha=0.5, color='gray')
ax2.xaxis.set_major_locator(mdates.MonthLocator())
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b-%Y'))
plt.setp(ax2.get_xticklabels(), rotation=45, fontsize=13)
plt.setp(ax2.get_yticklabels(), fontsize=13)
fig2.tight_layout()
fig2.savefig('sla_compliance_per_month.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()