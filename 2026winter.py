import pandas as pd

# 构建岗位数据
data = [
    ["Loblaw", "Brand Marketing, Discount – Co-op Student", "Internship/Co-op", "4个月（Jan–Apr 2026）", "基础办公软件（Word/Excel/PowerPoint），营销工具",
        "数据分析偏基础（分析campaign效果）", "无", "高，零售与品牌营销", "协助策划与执行营销活动，分析campaign结果，跨部门沟通", "Hybrid，Brampton, ON"],
    ["RBC", "Analyst, Commercial Performance Management",
        "Student (Full-time)", "4个月（Jan–Apr 2026）", "Jira Service Desk，Kanban管理，Office", "数据处理与指标自动化", "无", "中，高度商业分析与绩效管理", "自动化流程，增强报表与指标管理，知识库建设", "Toronto, ON"],
    ["Siemens", "HR Intern (Oakville)", "Full-time", "≥6个月", "MS Office，HR系统",
     "基础数据管理", "无", "中，HR及行政管理", "招聘与入职协助，行政任务，专项项目支持", "Oakville, ON"],
    ["Bell", "Data Analytics & AI Internship", "Full-time", "未指定", "Python/Scala/R，SQL，Looker/Kibana/Microstrategy",
        "高", "高，AI/ML项目", "中", "数据分析、建模、支持业务决策，参与Cloud/AI/ML项目", "Mississauga, ON"],
    ["RBC", "Capital Markets, Global Equities, Quantitative Trading Analyst",
        "Co-op (16个月)", "16个月", "Python编程，量化建模", "高，统计与优化", "高，机器学习用于交易策略", "高，金融量化", "开发量化交易策略，算法优化，市场数据分析", "Toronto, ON"],
    ["Scotiabank", "Quantitative Trading Developer – Electronic Execution Services", "PEY 12个月", "12个月",
        "Python/Java/JavaScript，数据库(MSSQL/MongoDB)，Pandas, Angular/Django", "高，数据管理与分析", "高，深度学习用于交易策略", "高，金融量化", "开发算法交易系统，智能路由，内网工具，自动化报表", "Toronto, ON"],
    ["TD L&H", "Business Performance Analyst", "Internship/Co-op", "4个月",
        "Excel, Tableau, Python", "中", "中", "高，商业与金融分析", "报表自动化，战略分析支持", "Toronto, ON"],
    ["Hydro One", "Emergency Management Intern", "Internship/Co-op", "4个月",
        "Excel, PowerQuery, 基础编程", "中", "低", "中，公共事业与应急管理", "支持应急管理技术与流程", "Toronto, ON"],
    ["Richter", "Transfer Pricing Intern", "Internship/Co-op", "4个月",
        "Excel建模，财务分析", "中", "高", "高，CPA轨道，跨境税务", "协助转让定价建模与财务分析", "Toronto, ON"],
    ["Balfour Clothing", "Invoicing / Accounting Assistant", "Full-time", "未指定",
        "QuickBooks, Excel", "中，财务数据处理", "无", "中，财务/会计", "发票处理，账务核对，月末结算", "North York, ON"]
]

# 创建DataFrame
columns = ["公司", "岗位", "类型", "工作周期", "技术深度", "数据/统计能力",
           "ML/AI应用", "金融/商业相关", "项目职责亮点", "工作形式/地点"]
df = pd.DataFrame(data, columns=columns)

# 保存为Excel
output_file = "E:/MacMaster/Python60Winter_2026_Internships.xlsx"
df.to_excel(output_file, index=False)
output_file
