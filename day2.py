import tensorflow as tf
# TensorFlow 2.x 中的自动微分示例
x = tf.constant(3.0)
with tf.GradientTape() as tape:
    y = x ** 2 + 5 * x + 2
grad = tape.gradient(y, x)
print(grad)  # 输出 11.0
# TensorFlow 2.x 中的自动微分示例
# 数学解析法（手动计算）

# 步骤：

# 识别函数形式：y = x² + 5x + 2。
# 应用微分规则：

# 幂规则：$ \frac{d}{dx}(x^n) = n x^{n-1} $ → $ \frac{d}{dx}(x^2) = 2x $。
# 常数倍规则：$ \frac{d}{dx}(c \cdot f(x)) = c \cdot \frac{df}{dx} $ → $ \frac{d}{dx}(5x) = 5 $。
# 常数规则：$ \frac{d}{dx}(c) = 0 $ → $ \frac{d}{dx}(2) = 0 $。
# 和规则：将各部分相加 → $ 2x + 5 + 0 = 2x + 5 $。
#  代入具体 x 值：如 x=3，得到 11。

#  张量tensor，常量constant，变量variable
#  常量张量	tf.constant()	不可变，值固定	输入数据、超参数
#  变量张量	tf.Variable()	可变，可更新	模型权重、偏置