import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# 1. 加载数据
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 2. 数据预处理
x_train = x_train / 255.0  # 归一化到 0-1
x_test = x_test / 255.0

# 转成 one-hot 编码（因为是多分类）
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

# 3. 构建模型
model = Sequential([
    Flatten(input_shape=(28, 28)),              # 把图片拉成 784 维向量
    Dense(128, activation='relu'),              # 第一层，全连接 + ReLU
    Dense(64, activation='relu'),               # 第二层
    Dense(10, activation='softmax')             # 输出层，10 类 → softmax 概率
])

# 4. 编译模型
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',            # 多分类问题 → crossentropy
    metrics=['accuracy']
)

# 5. 训练模型
model.fit(x_train, y_train, epochs=5, batch_size=16, validation_split=0.1)

# 6. 评估模型
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")