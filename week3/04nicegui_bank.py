# dash_bank_nicegui.py
from nicegui import ui
import sqlite3
import os

DB_FILE = 'bank.db'

# 初始化数据库


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            account_id TEXT PRIMARY KEY,
            owner TEXT,
            balance REAL
        )
    ''')
    conn.commit()
    conn.close()


init_db()

# 银行账户类


class Account:
    def __init__(self, account_id, owner, balance=0.0):
        self.account_id = account_id
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        self.save()

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("余额不足")
        self._balance -= amount
        self.save()

    def save(self):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO accounts(account_id, owner, balance)
            VALUES (?, ?, ?)
        ''', (self.account_id, self.owner, self._balance))
        conn.commit()
        conn.close()

    @staticmethod
    def get(account_id):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            'SELECT account_id, owner, balance FROM accounts WHERE account_id=?', (account_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Account(*row)
        return None

# ===============================
# NiceGUI 前端部分
# ===============================


ui.label('🏦 银行账户管理系统').style(
    'font-size:32px; font-weight:bold; margin-bottom:20px;')

# --- 创建账户 ---
with ui.card().tight().style('padding: 10px; margin: 10px'):
    ui.label("📌 创建账户")
    create_id = ui.input("账户ID")
    create_owner = ui.input("账户持有人")
    create_balance = ui.number("初始余额", value=0.0)
    create_result = ui.label("")

    def create_account():
        if not create_id.value or not create_owner.value:
            create_result.set_text("请输入账户ID和账户持有人")
            return
        acc = Account(create_id.value, create_owner.value,
                      float(create_balance.value))
        acc.save()
        create_result.set_text(f"账户 {acc.account_id} 创建成功")

    ui.button("创建账户", on_click=create_account)

# --- 存款 ---
with ui.card().tight().style('padding: 10px; margin: 10px'):
    ui.label("💰 存款")
    deposit_id = ui.input("账户ID")
    deposit_amount = ui.number("存款金额", value=0.0)
    deposit_result = ui.label("")

    def do_deposit():
        acc = Account.get(deposit_id.value)
        if not acc:
            deposit_result.set_text("账户不存在")
            return
        acc.deposit(float(deposit_amount.value))
        deposit_result.set_text(f"存款成功，余额：{acc.balance:.2f}")

    ui.button("存款", on_click=do_deposit)

# --- 取款 ---
with ui.card().tight().style('padding: 10px; margin: 10px'):
    ui.label("🏧 取款")
    withdraw_id = ui.input("账户ID")
    withdraw_amount = ui.number("取款金额", value=0.0)
    withdraw_result = ui.label("")

    def do_withdraw():
        acc = Account.get(withdraw_id.value)
        if not acc:
            withdraw_result.set_text("账户不存在")
            return
        try:
            acc.withdraw(float(withdraw_amount.value))
            withdraw_result.set_text(f"取款成功，余额：{acc.balance:.2f}")
        except ValueError as e:
            withdraw_result.set_text(str(e))

    ui.button("取款", on_click=do_withdraw)

# --- 查询余额 ---
with ui.card().tight().style('padding: 10px; margin: 10px'):
    ui.label("🔍 查询余额")
    query_id = ui.input("账户ID")
    query_result = ui.label("")

    def query_balance():
        acc = Account.get(query_id.value)
        if not acc:
            query_result.set_text("账户不存在")
            return
        query_result.set_text(f"余额：{acc.balance:.2f}")

    ui.button("查询余额", on_click=query_balance)

# ===============================
# 运行
# ===============================
ui.run()
