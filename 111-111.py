import pandas as pd
import json

# Step 0: Data
data = [
    {"Date": "2025-10-20", "UserID": 102, "Username": "Alice",
        "Email": "alice@mail.com", "Score": 88},
    {"Date": "2025-10-21", "UserID": 101,
        "Username": "Bob", "Email": "", "Score": 92},
    {"Date": "2025-10-22", "UserID": None, "Username": "alice",
        "Email": "alice@mail.com", "Score": "error"},
    {"Date": "2025-10-23", "UserID": 102, "Username": "Bob",
        "Email": "bob@mail.com", "Score": 85},
    {"Date": "2025-10-24", "UserID": 0.5,
        "Username": "", "Email": None, "Score": 90},
    {"Date": "2025-10-24", "UserID": 102, "Username": "Alice",
        "Email": "alice@mail.com", "Score": 88}
]

# Step 1: Create DataFrame
df = pd.DataFrame(data)

# Step 2: Clean numeric columns
for col in ['UserID', 'Score']:
    df[col] = pd.to_numeric(df[col], errors='coerce')
# 数字列用 Pandas 的 to_numeric 方法转换，非数字值会变为 NaN

# Step 3: Clean string columns
for col in ['Username', 'Email']:
    df[col] = df[col].replace('', pd.NA)
# 字符串列用 DataFrame/Series 自身方法替换空字符串为缺失值

# Step 4: Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.sort_values('Date')
# Date 列用 Pandas 的 to_datetime 方法转换为 datetime 类型，然后按日期排序
print("=== Cleaned DataFrame ===")
print(df)

# Step 5: Overall statistics
report = {}
for col in ['UserID', 'Username', 'Email', 'Score']:
    series = df[col].dropna()
    report[col] = {
        'valid_count': int(series.count()),
        'unique_count': int(series.nunique()),
        'duplicates_count': int(series.count() - series.nunique()),
        'values': [v.item() if hasattr(v, 'item') else v for v in series.tolist()]
    }

# Step 6: Daily stats
daily_stats = df.groupby('Date').agg({
    'UserID': 'count',
    'Username': 'count',
    'Email': 'count',
    'Score': 'count'
}).rename(columns=lambda x: f'{x}_valid_count').reset_index()

# Convert Timestamp and numpy to native Python types
daily_records = []
for _, row in daily_stats.iterrows():
    daily_records.append({k: (v.item() if hasattr(v, 'item') else str(v) if isinstance(v, pd.Timestamp) else v)
                          for k, v in row.items()})

# Step 7: Combine
final_report = {
    'overall': report,
    'daily': daily_records
}

# Step 8: Write JSON safely
with open('user_data_report.json', 'w') as f:
    json.dump(final_report, f, indent=4)

# Print
print(json.dumps(final_report, indent=4))
