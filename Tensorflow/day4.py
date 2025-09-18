import numpy as np
from tensorflow.keras import Model, Input
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# 1. 生成虚拟训练数据（1000 个样本，每个样本是 10 维输入）
x_train = np.random.rand(1000, 10)
y_train = np.sum(x_train, axis=1, keepdims=True)  # 简单的加和作为输出目标

# 2. 定义模型结构（Functional API）
inputs = Input(shape=(10,))                     # 输入层（10维向量）
x = Dense(32, activation='relu')(inputs)        # 隐藏层 1
outputs = Dense(1)(x)                           # 输出层（1维回归输出）
# 可以去掉 X=，改成outputs = Dense(1)(inputs)     # 变成线性回归了 
model = Model(inputs, outputs)                  # 构建模型

# 3. 编译模型
model.compile(
    optimizer=Adam(learning_rate=0.01),         # 使用 Adam 优化器
    loss='mse',                                 # 回归问题使用均方误差（MSE）作为损失函数
    metrics=['mae']                             # 使用平均绝对误差 MAE 评估
)

# 4. 训练模型
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# 5. 评估模型
x_test = np.random.rand(100, 10)
y_test = np.sum(x_test, axis=1, keepdims=True)
loss, mae = model.evaluate(x_test, y_test)

print(f"Test MAE: {mae:.4f}")

# Input (10维)
#    ↓
# Dense(32, ReLU)
#    ↓
# Dense(1, Linear)
#    ↓
# 输出

# 函数式编程风格的建模接口
