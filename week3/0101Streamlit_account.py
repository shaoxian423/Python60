from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟数据库
accounts = {}

# =========================
# 银行账户类
# =========================


class Account:
    """使用构造函数，并用了两个默认数据“="""

    def __init__(self, account_id, owner, balance=0.0, interest_rate=0.01):
        self.account_id = account_id
        self.owner = owner
        self._balance = balance
        self.interest_rate = interest_rate

    # 🔹 余额属性"""属性通常表示对象的状态，就是一个变量的值，读取不会触发逻辑"""
    @property  # 用装饰器封装，把它由私有变成只读属性
    def balance(self):
        return self._balance

    # 🔹 存款
    """以下三种皆属于方法（存，取和计算利息),方法需要执行逻辑，或产生副作用
    不仅是读取数据，而且会改变动作的状态"""

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金额必须大于 0")
        self._balance += amount

    # 🔹 取款
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("取款金额必须大于 0")
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("余额不足")

    # 🔹 利息计算
    def apply_interest(self):
        self._balance += self._balance * self.interest_rate


# =========================
# API 路由
# =========================

# 创建账户
"""Flask的路由定义语法，其中HTTP的请求方法主要有：post,get,delete等，HTTP方法在标准里要大写，这是规范要求
这个方法是接收来自http的请求，因此用[]"""


@app.route("/create", methods=["POST"])
def create_account():
    data = request.json  # 把前端发过来的数据变成字典
    required_fields = ["account_id", "owner"]  # 定义发过来的数据里必须有这两项
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"缺少字段: {field}"}), 400

    acc_id = data["account_id"]
    if acc_id in accounts:
        return jsonify({"error": "账户已存在"}), 400

    acc = Account(
        account_id=acc_id,
        owner=data["owner"],
        balance=data.get("balance", 0.0),
        interest_rate=data.get("interest_rate", 0.01)
    )
    accounts[acc_id] = acc  # 把这个新建的账号存在字典里，用id作为key方便索引
    return jsonify({"message": "账户创建成功"}), 200


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

    try:
        acc.deposit(amount)
        return jsonify({"balance": acc.balance}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# 取款
"""注意这个动态路由的写法：<>,用<>占位，它表示url路径的参数，里面的名字会传递给函数参数"""


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

# 利率计算


@app.route("/apply_interest/<account_id>", methods=["POST"])
def apply_interest_api(account_id):
    acc = accounts.get(account_id)
    if not acc:
        return jsonify({"error": "账户不存在"}), 404

    # 调用 Account 类的方法
    acc.apply_interest()
    return jsonify({"balance": acc.balance}), 200


# =========================
# 启动服务
# =========================
if __name__ == "__main__":
    app.run(debug=True)
