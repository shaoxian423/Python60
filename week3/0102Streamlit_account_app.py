import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000"  # Flask API 地址

st.title("🏦 银行账户管理系统")

# ========================
# 创建账户
# ========================
with st.form("create_form"):
    st.header("🧨 创建账户")
    account_id = st.text_input("账户ID", key="create_id")
    owner = st.text_input("账户持有人", key="owner")
    initial_balance = st.number_input(
        "初始余额", min_value=0.0, value=0.0, key="balance")
    submitted = st.form_submit_button("创建账户")
    if submitted:
        if account_id and owner:
            resp = requests.post(f"{API_URL}/create", json={
                "account_id": account_id,
                "owner": owner,
                "balance": initial_balance
            })
            result = resp.json()
            if "error" in result:
                st.error(result["error"])
            else:
                st.success(result["message"])
        else:
            st.error("请输入账户ID和账户持有人")

# ========================
# 存款
# ========================
with st.form("deposit_form"):
    st.header("💰 存款")
    deposit_account = st.text_input("存款账户ID", key="deposit_id")
    deposit_amount = st.number_input(
        "存款金额", min_value=0.0, value=0.0, key="deposit_amount")
    submitted = st.form_submit_button("存款")
    if submitted:
        if deposit_account:
            resp = requests.post(
                f"{API_URL}/deposit/{deposit_account}", json={"amount": deposit_amount})
            result = resp.json()
            if "error" in result:
                st.error(result["error"])
            else:
                st.success(f"存款成功，当前余额：{result['balance']:.2f}")
        else:
            st.error("请输入账户ID")

# ========================
# 取款
# ========================
with st.form("withdraw_form"):
    st.header("🏧 取款")
    withdraw_account = st.text_input("取款账户ID", key="withdraw_id")
    withdraw_amount = st.number_input(
        "取款金额", min_value=0.0, value=0.0, key="withdraw_amount")
    submitted = st.form_submit_button("取款")
    if submitted:
        if withdraw_account:
            resp = requests.post(
                f"{API_URL}/withdraw/{withdraw_account}", json={"amount": withdraw_amount})
            result = resp.json()
            if "error" in result:
                st.error(result["error"])
            else:
                st.success(f"取款成功，当前余额：{result['balance']:.2f}")
        else:
            st.error("请输入账户ID")

# ========================
# 查询余额
# ========================
with st.form("balance_form"):
    st.header("🔍 查询余额")
    balance_account = st.text_input("查询账户ID", key="balance_id")
    submitted = st.form_submit_button("查询余额")
    if submitted:
        if balance_account:
            resp = requests.get(f"{API_URL}/balance/{balance_account}")
            result = resp.json()
            if "error" in result:
                st.error(result["error"])
            else:
                st.info(f"账户 {balance_account} 当前余额：{result['balance']:.2f}")
        else:
            st.error("请输入账户ID")

# ========================
# 利率计算
# ========================
with st.form("interest_form"):
    st.header("💹 利率计算")
    interest_account = st.text_input("计算利息账户ID", key="interest_id")
    submitted = st.form_submit_button("计算利息")
    if submitted:
        if interest_account:
            resp = requests.get(f"{API_URL}/apply_interest/{interest_account}")
            result = resp.json()
            if "error" in result:
                st.error(result["error"])
            else:
                st.success(f"利息计算完成，当前余额：{result['balance']:.2f}")
        else:
            st.error("请输入账户ID")
