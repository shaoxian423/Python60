import re

text = "Contact me: john.doe@example.com or 13800138000. Website: https://example.com. Date: 2025-10-05"

# 找出所有邮箱
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# 找出手机号
phones = re.findall(r"1[3-9]\d{9}", text)

# 找出日期
dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)

# 替换 URL 为 <URL>
new_text = re.sub(r"https?://[^\s]+", "<URL>", text)

print("Emails:", emails)
print("Phones:", phones)
print("Dates:", dates)
print("New Text:", new_text)
