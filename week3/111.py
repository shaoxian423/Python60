from flask import Flask, request, jsonify

app = Flask(__name__)

accounts = {}


class Account:
    def __init__(self, account_id, owner, balance=0, interest_rate=0.01):
        self.account_id = accounts
        self.owner = owner
        self._balance = balance
        self.interest_rate = interest_rate

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("must max 0")
        if amount > self._balance:
            raise ValueError("yue buzu")
        self._balance -= amount

    def apply_interest(self):
        self._balance += self.interest_rate * self._balance


# Falsk API

@app.route("/create", methods=["POST"])
def create_account():
    data = request.json
    required_field = ["account_id", "owner"]
    for field in required_field:
        if field not in data:
            return jsonify("缺少字段")
    acc_id = data["account_id"]
    if acc_id in accounts:
        return jsonify("账户已存在"), 400
    acc = Account(
        account_id=acc_id,
        owner=data["owner"],
        balance=data.get("balance", 0.0),
        interest_rate=data.get("interest_rate", 0.01)
    )
    accounts[acc_id] = acc
    return jsonify("账户创建成功"), 200


@app.route("/deposit/<account_id>", methosds=["POST"])
def deposit(account_id):
    data = request.json
    amount = data.get("amount")
    if amount is None:
        return jsonify("缺少amount")

    acc = accounts.get("account_id")
    if not acc:
        return jsonify("账户不存在")
    try:
        acc.deposit(amount)
        return jsonify({"balance": acc.balance}), 200
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
