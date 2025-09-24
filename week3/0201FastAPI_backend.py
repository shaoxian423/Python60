from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="银行账户管理系统")

# 模拟数据库
accounts = {}

# 请求数据模型


class AccountCreate(BaseModel):
    account_id: str
    owner: str
    balance: Optional[float] = 0.0
    interest_rate: Optional[float] = 0.01


class Transaction(BaseModel):
    amount: float

# -------------------
# 银行账户类
# -------------------


class Account:
    def __init__(self, account_id, owner, balance=0.0, interest_rate=0.01):
        self.account_id = account_id
        self.owner = owner
        self._balance = balance
        self.interest_rate = interest_rate

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("余额不足")

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate

# -------------------
# API 路由
# -------------------


@app.post("/create")
def create_account(data: AccountCreate):
    if data.account_id in accounts:
        raise HTTPException(status_code=400, detail="账户已存在")
    acc = Account(data.account_id, data.owner,
                  data.balance, data.interest_rate)
    accounts[data.account_id] = acc
    return {"message": "账户创建成功"}


@app.post("/deposit/{account_id}")
def deposit(account_id: str, data: Transaction):
    acc = accounts.get(account_id)
    if not acc:
        raise HTTPException(status_code=404, detail="账户不存在")
    acc.deposit(data.amount)
    return {"balance": acc.balance}


@app.post("/withdraw/{account_id}")
def withdraw(account_id: str, data: Transaction):
    acc = accounts.get(account_id)
    if not acc:
        raise HTTPException(status_code=404, detail="账户不存在")
    try:
        acc.withdraw(data.amount)
        return {"balance": acc.balance}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/balance/{account_id}")
def balance(account_id: str):
    acc = accounts.get(account_id)
    if not acc:
        raise HTTPException(status_code=404, detail="账户不存在")
    return {"balance": acc.balance}
