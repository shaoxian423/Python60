from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟数据库
accounts = {}

# 银行账户类


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

# 创建账户


@app.route("/create", methods=["POST"])
def create_account():
    data = request.json
    try:
        acc = Account(
            data["account_id"],
            data["owner"],
            data.get("balance", 0),
            data.get("interest_rate", 0.01)
        )
        accounts[data["account_id"]] = acc
        return jsonify({"message": "账户创建成功"}), 200
    except KeyError as e:
        return jsonify({"error": f"缺少字段: {e}"}), 400

# 存款


@app.route("/deposit/<account_id>", methods=["POST"])
def deposit(account_id):
    data = request.json
    amount = data.get("amount")
    if amount is None:
        return jsonify({"error": "缺少 amount"}), 400
    acc = accounts.get(account_id)
    if not acc:
        return jsonify({"error": "账户不存在"}), 404
    acc.deposit(amount)
    return jsonify({"balance": acc.balance}), 200

# 取款


@app.route("/withdraw/<account_id>", methods=["POST"])
def withdraw(account_id):
    data = request.json
    amount = data.get("amount")
    if amount is None:
        return jsonify({"error": "缺少 amount"}), 400
    acc = accounts.get(account_id)
    if not acc:
        return jsonify({"error": "账户不存在"}), 404
    try:
        acc.withdraw(amount)
        return jsonify({"balance": acc.balance}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# 查询余额


@app.route("/balance/<account_id>", methods=["GET"])
def balance(account_id):
    acc = accounts.get(account_id)
    if not acc:
        return jsonify({"error": "账户不存在"}), 404
    return jsonify({"balance": acc.balance}), 200


if __name__ == "__main__":
    app.run(debug=True)
