# ==========================
# Dash 银行账户管理系统
# Week3 知识点注释版
# - 函数定义、参数传递
# - if __name__ == "__main__"
# - 类/对象使用 (这里用函数操作数据库模拟对象行为)
# - 条件语句 if/else
# - 异常处理 try/except
# - 数据结构（dict/SQLite表）
# - 回调函数
# - 输入/输出操作
# ==========================

import dash
from dash import html, dcc, Input, Output, State  # Dash组件
import sqlite3  # 数据库操作
import os       # 文件操作

# --------------------------
# 数据库文件与初始化
# --------------------------
DB_FILE = 'bank.db'


def init_db():
    """
    初始化 SQLite 数据库
    - 如果数据库文件不存在，则创建 accounts 表
    """
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE accounts (
                account_id TEXT PRIMARY KEY,
                owner TEXT NOT NULL,
                balance REAL NOT NULL DEFAULT 0
            )
        ''')
        conn.commit()
        conn.close()


init_db()  # 调用初始化函数

# --------------------------
# 数据库操作函数
# --------------------------


def create_account(account_id, owner, balance=0.0):
    """
    创建账户函数
    try/except 用于异常处理（KeyError, IntegrityError）
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        # SQL 插入操作
        c.execute('INSERT INTO accounts (account_id, owner, balance) VALUES (?, ?, ?)',
                  (account_id, owner, balance))
        conn.commit()
        return True, "账户创建成功"
    except sqlite3.IntegrityError:  # 捕获账户ID重复
        return False, "账户ID已存在"
    finally:
        conn.close()


def deposit(account_id, amount):
    """
    存款函数
    条件判断账户是否存在
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT balance FROM accounts WHERE account_id=?', (account_id,))
    row = c.fetchone()
    if row:
        new_balance = row[0] + amount  # 算术运算
        c.execute('UPDATE accounts SET balance=? WHERE account_id=?',
                  (new_balance, account_id))
        conn.commit()
        conn.close()
        return True, new_balance
    else:
        conn.close()
        return False, "账户不存在"


def withdraw(account_id, amount):
    """
    取款函数
    条件判断余额是否足够
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT balance FROM accounts WHERE account_id=?', (account_id,))
    row = c.fetchone()
    if row:
        if amount > row[0]:  # 条件语句 if
            conn.close()
            return False, "余额不足"
        new_balance = row[0] - amount
        c.execute('UPDATE accounts SET balance=? WHERE account_id=?',
                  (new_balance, account_id))
        conn.commit()
        conn.close()
        return True, new_balance
    else:
        conn.close()
        return False, "账户不存在"


def get_balance(account_id):
    """
    查询余额函数
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT balance FROM accounts WHERE account_id=?', (account_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return True, row[0]
    else:
        return False, "账户不存在"


# --------------------------
# Dash App 初始化
# --------------------------
app = dash.Dash(__name__)
app.title = "银行账户管理系统"

# --------------------------
# Dash 页面布局（HTML + 组件）
# --------------------------
app.layout = html.Div([
    html.H1("🏦 银行账户管理系统", style={'textAlign': 'center'}),

    # --- 创建账户 ---
    html.H2("📌 创建账户"),
    dcc.Input(id='create_id', placeholder='账户ID', type='text'),  # 文本输入
    dcc.Input(id='owner', placeholder='账户持有人', type='text'),
    dcc.Input(id='balance', placeholder='初始余额', type='number', value=0),
    html.Button("创建账户", id='create_btn', n_clicks=0),  # 按钮点击事件
    html.Div(id='create_msg', style={
             'marginBottom': '20px', 'color': 'green'}),

    # --- 存款 ---
    html.H2("💰 存款"),
    dcc.Input(id='deposit_id', placeholder='账户ID', type='text'),
    dcc.Input(id='deposit_amount', placeholder='存款金额', type='number', value=0),
    html.Button("存款", id='deposit_btn', n_clicks=0),
    html.Div(id='deposit_msg', style={
             'marginBottom': '20px', 'color': 'blue'}),

    # --- 取款 ---
    html.H2("🏧 取款"),
    dcc.Input(id='withdraw_id', placeholder='账户ID', type='text'),
    dcc.Input(id='withdraw_amount', placeholder='取款金额',
              type='number', value=0),
    html.Button("取款", id='withdraw_btn', n_clicks=0),
    html.Div(id='withdraw_msg', style={
             'marginBottom': '20px', 'color': 'red'}),

    # --- 查询余额 ---
    html.H2("🔍 查询余额"),
    dcc.Input(id='balance_id', placeholder='账户ID', type='text'),
    html.Button("查询余额", id='balance_btn', n_clicks=0),
    html.Div(id='balance_msg', style={
             'marginBottom': '20px', 'color': 'purple'}),
])

# ==========================
# Dash 回调函数（交互逻辑）
# Input/State 对应 Week3 学到的函数参数传递
# ==========================


@app.callback(
    Output('create_msg', 'children'),
    Input('create_btn', 'n_clicks'),
    State('create_id', 'value'),
    State('owner', 'value'),
    State('balance', 'value')
)
def handle_create(n, account_id, owner, balance):
    if n > 0:  # 判断按钮点击次数
        if not account_id or not owner:  # 条件判断
            return "请输入账户ID和账户持有人"
        success, msg = create_account(account_id, owner, balance or 0)  # 调用函数
        return msg
    return ""


@app.callback(
    Output('deposit_msg', 'children'),
    Input('deposit_btn', 'n_clicks'),
    State('deposit_id', 'value'),
    State('deposit_amount', 'value')
)
def handle_deposit(n, account_id, amount):
    if n > 0:
        if not account_id:
            return "请输入账户ID"
        success, result = deposit(account_id, amount or 0)
        return f"存款成功, 当前余额: {result}" if success else result
    return ""


@app.callback(
    Output('withdraw_msg', 'children'),
    Input('withdraw_btn', 'n_clicks'),
    State('withdraw_id', 'value'),
    State('withdraw_amount', 'value')
)
def handle_withdraw(n, account_id, amount):
    if n > 0:
        if not account_id:
            return "请输入账户ID"
        success, result = withdraw(account_id, amount or 0)
        return f"取款成功, 当前余额: {result}" if success else result
    return ""


@app.callback(
    Output('balance_msg', 'children'),
    Input('balance_btn', 'n_clicks'),
    State('balance_id', 'value')
)
def handle_balance(n, account_id):
    if n > 0:
        if not account_id:
            return "请输入账户ID"
        success, result = get_balance(account_id)
        return f"当前余额: {result}" if success else result
    return ""


# --------------------------
# 程序入口
# --------------------------
if __name__ == "__main__":
    app.run(debug=True)  # 新版 Dash 用 run() 替代 run_server()
