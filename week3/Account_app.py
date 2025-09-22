import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000"

st.title("🏦 银行账户管理系统")

# --- 创建账户 ---
st.header("📌 创建账户")
account_id = st.text_input("账户ID", key="create_id")
owner = st.text_input("账户持有人", key="owner")
initial_balance = st.number_input(
    "初始余额", min_value=0.0, value=0.0, key="balance")
if st.button("创建账户"):
    if account_id and owner:
        resp = requests.post(f"{API_URL}/create", json={
            "account_id": account_id,
            "owner": owner,
            "balance": initial_balance
        })
        st.write(resp.json())
    else:
        st.error("请输入账户ID和账户持有人")

# --- 存款 ---
st.header("💰 存款")
deposit_account = st.text_input("存款账户ID", key="deposit_id")
deposit_amount = st.number_input(
    "存款金额", min_value=0.0, value=0.0, key="deposit_amount")
if st.button("存款"):
    if deposit_account:
        resp = requests.post(
            f"{API_URL}/deposit/{deposit_account}", json={"amount": deposit_amount})
        st.write(resp.json())
    else:
        st.error("请输入账户ID")

# --- 取款 ---
st.header("🏧 取款")
withdraw_account = st.text_input("取款账户ID", key="withdraw_id")
withdraw_amount = st.number_input(
    "取款金额", min_value=0.0, value=0.0, key="withdraw_amount")
if st.button("取款"):
    if withdraw_account:
        resp = requests.post(
            f"{API_URL}/withdraw/{withdraw_account}", json={"amount": withdraw_amount})
        st.write(resp.json())
    else:
        st.error("请输入账户ID")

# --- 查询余额 ---
st.header("🔍 查询余额")
balance_account = st.text_input("查询账户ID", key="balance_id")
if st.button("查询余额"):
    if balance_account:
        resp = requests.get(f"{API_URL}/balance/{balance_account}")
        st.write(resp.json())
    else:
        st.error("请输入账户ID")
