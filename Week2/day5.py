import tensorflow as tf
import numpy as np
from tensorflow.keras import Model, Input
from tensorflow.keras.layers import Dense

# 1. 准备模拟数据：1000 个样本，每个样本有 10 个特征，对应一个标签（就是特征加总）
X = np.random.rand(1000, 10).astype(np.float32)       # 训练特征，float32 是 TensorFlow 默认数据类型
y = np.sum(X, axis=1, keepdims=True).astype(np.float32)  # 标签为各特征加总（回归任务）

# 2. 构建 tf.data 数据集对象
dataset = tf.data.Dataset.from_tensor_slices((X, y))  # 把 numpy 数据变成 TensorFlow 数据集
dataset = dataset.shuffle(buffer_size=100)            # 打乱样本（防止模型记顺序）
dataset = dataset.batch(32)                           # 每批 32 条数据
dataset = dataset.prefetch(tf.data.AUTOTUNE)          # 自动预取数据，提升性能（边训练边准备下一批数据）

# 3. 定义模型（使用 Functional API）
inputs = Input(shape=(10,))                           # 输入层：10个特征
x = Dense(32, activation='relu')(inputs)              # 隐藏层：32个神经元
outputs = Dense(1)(x)                                 # 输出层：1个预测值（回归）
model = Model(inputs, outputs)

# 4. 编译模型
model.compile(
    optimizer='adam',    # 使用 Adam 优化器
    loss='mse',          # 使用均方误差作为损失函数
    metrics=['mae']      # 评估指标为平均绝对误差
)

# 5. 训练模型（用我们刚刚创建的 dataset）
model.fit(dataset, epochs=5)
# Evaluate the model on the training dataset to get MAE
loss, mae = model.evaluate(dataset, verbose=0)
print(f"Test MAE:{mae:.3f}")


# ✅ 这样就可以训练一个完整的模型，并使用 tf.data 提升效率