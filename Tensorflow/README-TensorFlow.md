✅ 第一阶段：基础入门 —— 理解框架结构和基本用法

🎯 目标
	•	搭建 TensorFlow 环境
	•	掌握基本张量操作、自动微分、神经网络建模
📚 学习内容
内容                           推荐方式
TensorFlow 安装与环境配置       官方文档、conda、pip
Tensor 基本操作 (tf.Tensor)    数据类型、维度、切片、广播
自动微分 (tf.GradientTape)     基本的梯度求解、反向传播
Keras 快速建模 (tf.keras)      Sequential, Functional API
模型训练流程                    compile, fit, evaluate, predict
常用层和损失函数                 Dense, Conv2D, LSTM, MSE, Crossentropy

✅ 第二阶段：深入机制 —— 掌握训练优化与自定义组件

🎯 目标
	•	理解训练原理
	•	学会自定义模型、层、损失、训练流程
	•	掌握数据加载优化

📚 学习内容
内容                            推荐方式
tf.data                        数据预处理、批处理、shuffle、prefetch
自定义 Layer                    继承 tf.keras.layers.Layer
自定义 Loss/Metric              继承 tf.keras.losses.Loss, tf.keras.metrics.Metric
自定义 Model                    继承 tf.keras.Model，重写 call()
手动训练 Loop                   GradientTape + apply_gradients()
Callback 控制训练               EarlyStopping, ModelCheckpoint, TensorBoard

✅ 第三阶段：工业实践 —— 分布式训练、部署、性能优化

🎯 目标
	•	学会模型部署、分布式训练、多设备优化
	•	性能调优，迁移学习，模型压缩

📚 学习内容
内容                              推荐方式
分布式训练 tf.distribute           Multi-GPU, Multi-node
TensorFlow Serving 部署           REST API 部署模型                   
TFLite / TensorFlow.js            移动端和 Web 端部署
XLA 编译加速                       自动图优化、低延迟推理
模型剪枝 & 量化                     轻量化部署
Transfer Learning 迁移学习         复用预训练模型

✅ 第四阶段：深度优化 & 源码层理解

🎯 目标
	•	阅读 TensorFlow 源码，理解框架架构
	•	理解张量计算、Graph 编译、设备调度
	•	参与社区贡献 / 自主研发深度模型

📚 学习内容
内容                               推荐方式
Eager Execution vs Graph        动态图与静态图的关系
tf.function 编译原理             GraphDef, SavedModel, Autograph
Kernel 实现                     C++ 实现的底层操作符
分布式策略源码                    MirroredStrategy、ParameterServerStrategy 源码分析
XLA 编译器                      TensorFlow 图优化器

🔨 推荐系统学习路线

阶段                                建议时长                            推荐项目
基础入门                            1 ~ 2 周                            图像分类、回归预测、小型 RNN
深入机制                            2 ~ 4 周                            自定义 Attention、时间序列预测
工业实践                            3 ~ 6 周                            迁移学习 API、部署 REST 服务
源码理解                            1 ~ 3 个月                          自己实现 Loss、优化器、训练 Loop

🚀 推荐实践项目
	•	MNIST 手写数字分类
	•	CIFAR-10 图像分类
	•	IMDB 情感分析
	•	股票价格预测（LSTM）
	•	人脸识别（Triplet Loss）
	•	微服务部署 TensorFlow Serving
	•	TFLite 部署到 Android / Raspberry Pi

    
### ✅ Day 1 - TensorFlow 安装与环境配置
- 安装 TensorFlow：`pip install tensorflow`
- 环境：推荐使用 conda 虚拟环境或 pyenv
- 推荐开发环境：
  - VS Code + Python Extension
  - Google Colab（快速实验）
- 验证：
```python
import tensorflow as tf
print(tf.__version__)
```
- CPU / GPU 检测：
```python
print(tf.config.list_physical_devices('GPU'))
```

---

### ✅ Day 2 - Tensor 基本操作 & 自动微分
- 创建张量：`tf.constant`, `tf.Variable`
- 基本算术：`+ - * /`, `tf.matmul()`
- 自动微分：`tf.GradientTape()`

示例：
```python
x = tf.constant(3.0)
with tf.GradientTape() as tape:
    y = x ** 2 + 5 * x + 2
grad = tape.gradient(y, x)
print(grad)  # 输出 11.0
```

---

### ✅ Day 3 - Keras Sequential 快速建模
- 创建简单神经网络：
```python
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(32, activation='relu', input_shape=(10,)),
    Dense(1)
])
```
# 回归和分类：回归regression就是dense（1），\text{output} = \sum_{i=1}^{32} (x_i \times w_i) + b
# i=1就是前一层的32个输出， w_i就是这一层神经元的权重（这一层的神经元只有一个），b就是偏置。
# 分类classification就是：Dense(3, activation='softmax')（例如：预测涨 or 跌 or 横盘）
# Dense就是全连接层的意思Fully Connected Layer，
# relu是非线性函数Rectified Linear Unit，activation='relu'就是通过非线性函数激活，把所有负数变成0，\text{ReLU}(x) = \max(0, x)为什么要用 ReLU？
	•	✅ 引入非线性，使神经网络可以学习复杂函数；
	•	✅ 计算简单，收敛快；
	•	✅ 相比 sigmoid 或 tanh，更不容易梯度消失；
	•	❗缺点：ReLU 会“抛弃”所有负值，可能导致神经元“死亡”。
# shape就是维度，shape=（10，）就是10个维度的向量，不是10个数，也就是每条输入样本有 10 个特征。Dense（32.。。）后把10个维度的向量分别乘以不同的权重，变成32个维度的向量，也就是说：把输入的 10 维向量，通过 32 个神经元的加权计算，转换成一个新的 32 维向量）
- compile & fit：
```python
model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=5)
```
# 这一步是 模型编译，告诉 Keras：
	•	优化器 optimizer=‘adam’：
	•	Adam 是一种自适应学习率的优化算法，非常常用；
	•	它根据每个参数的梯度历史自适应调整学习率；
	•	简单说：它帮你智能地“找最小损失点”。
	•	损失函数 loss=‘mse’：
	•	mse 是 Mean Squared Error（均方误差），用于衡量预测值与真实值之间的差距：
# \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
#	•	它是回归任务的常见选择，当你预测的是一个连续值（如房价、温度、涨幅）时非常合适
# loss= focalloss，焦点损失，是设计用来分类用的（特别是多分类或不平衡分类），减少对“容易分类样本”的关注，强调困难样本的学习，：Focal Loss = CrossEntropy × 聚焦系数
✅ 对“预测很准”的样本，惩罚轻；
✅ 对“预测错得离谱”的样本，惩罚重；
✅ 适合少数类被淹没的大数据分类问题。 
# loss= mse是回归用的，预测数值，如房价、温度、涨跌幅度等，让预测值更接近真实数值，要研究mse的公式
# Adam = Adaptive Moment Estimation（自适应矩估计）Adam 是一种结合了 Momentum（动量）和 RMSProp（自适应学习率）的优化算法。它能在训练神经网络时更快、更稳定地找到最优参数。
# 格式代码
示例
含义/效果
输出示例
:.nf
{x:.2f}
保留小数点后 n 位
3.14159 → 3.14
:d
{x:d}
十进制整数（默认）
42
:>n
{x:>5}
右对齐，宽度为 n
'   42'
:<n
{x:<5}
左对齐，宽度为 n
'42   '
:^n
{x:^5}
居中对齐，宽度为 n
' 42  '
:0n
{x:05d}
用 0 补齐，长度为 n
42 → 00042
:b
{x:b}
转换为二进制
42 → 101010
:x / :X
{x:x} / {x:X}
转换为十六进制（小写 / 大写）
42 → 2a / 2A
:%
{x:.2%}
转换为百分比，保留 2 位小数
0.876 → 87.60%
:,
{x:,}
添加千分位逗号分隔符
1234567 → 1,234,567



- 实战：MNIST 手写数字识别

---

### ✅ Day 4 - Functional API 多输入 / 多输出
- Functional API 语法：
```python
from tensorflow.keras import Model, Input
from tensorflow.keras.layers import Dense

inputs = Input(shape=(10,))
x = Dense(32, activation='relu')(inputs)
outputs = Dense(1)(x)
model = Model(inputs, outputs)
```
- 适用场景：多输入、多输出、复杂连接结构
![alt text](image.png)
---

### ✅ Day 5 - tf.data 数据处理流水线
- tf.data.Dataset.from_tensor_slices()
- shuffle()、batch()、prefetch()
- 实战：批量读取图片、标签

示例：
```python
dataset = tf.data.Dataset.from_tensor_slices((X, y))
dataset = dataset.shuffle(100).batch(32).prefetch(tf.data.AUTOTUNE)
```

---

### ✅ Day 6 - 损失函数 / 优化器 / 指标
- 常用损失：MSE, CrossEntropy
- 常用优化器：Adam, SGD
- 常用指标：Accuracy, MAE
- 自定义 Loss：
```python
from tensorflow.keras.losses import Loss

class MyLoss(Loss):
    def call(self, y_true, y_pred):
        return tf.reduce_mean(tf.square(y_true - y_pred)) + 0.1 * tf.reduce_mean(tf.abs(y_pred))
```

---

### ✅ Day 7 - callback 与训练优化
- EarlyStopping
- ModelCheckpoint
- TensorBoard 日志记录

示例：
```python
from tensorflow.keras.callbacks import EarlyStopping

early_stop = EarlyStopping(monitor='val_loss', patience=3)
model.fit(X, y, validation_split=0.2, epochs=10, callbacks=[early_stop])
```
### ✅ Day 8 - 自定义 Layer
- 基本语法：继承 `tf.keras.layers.Layer`
- 示例：自定义标准化层
```python
from tensorflow.keras.layers import Layer

class CustomLayer(Layer):
    def call(self, inputs):
        return (inputs - tf.reduce_mean(inputs)) / tf.math.reduce_std(inputs)
```
- 应用场景：特殊的非现成层

---

### ✅ Day 9 - 自定义 Model
- 继承 `tf.keras.Model`
- 重写 `__init__()` 和 `call()`
```python
from tensorflow.keras import Model

class MyModel(Model):
    def __init__(self):
        super().__init__()
        self.dense1 = tf.keras.layers.Dense(32, activation='relu')
        self.out = tf.keras.layers.Dense(1)

    def call(self, inputs):
        x = self.dense1(inputs)
        return self.out(x)
```

---

### ✅ Day 10 - 自定义 Loss 和 Metric
- 自定义 Loss:
```python
from tensorflow.keras.losses import Loss

class CustomMSE(Loss):
    def call(self, y_true, y_pred):
        return tf.reduce_mean(tf.square(y_true - y_pred))
```
- 自定义 Metric：继承 `tf.keras.metrics.Metric`

---

### ✅ Day 11 - 手动训练 Loop
- 使用 `GradientTape`
```python
for epoch in range(epochs):
    for batch in dataset:
        with tf.GradientTape() as tape:
            predictions = model(batch)
            loss = loss_fn(batch_labels, predictions)
        grads = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(grads, model.trainable_variables))
```

---

### ✅ Day 12 - 分布式训练 tf.distribute
- MirroredStrategy：单机多 GPU
```python
strategy = tf.distribute.MirroredStrategy()
with strategy.scope():
    model = build_model()
    model.compile(...)
```
- MultiWorkerMirroredStrategy：多机训练

---

### ✅ Day 13 - tf.function 静态图优化
- 使用 `@tf.function` 编译训练函数，提高效率
- 自动将 Python 动态代码转换为 TensorFlow 静态计算图
```python
@tf.function
def train_step(inputs):
    ...
```

---

### ✅ Day 14 - tf.data 加速优化
- prefetch：提前准备数据
- cache：内存缓存
```python
dataset = dataset.batch(32).prefetch(tf.data.AUTOTUNE)
```
- autotune：自动选择最优参数

---

### ✅ Day 15 - Transfer Learning
- 使用预训练模型，如 ResNet、Inception
```python
base_model = tf.keras.applications.ResNet50(include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False
```
- 应用场景：小数据集、微调

---
### ✅ Day 16 - TensorFlow Serving 部署
- 安装 Serving：
```bash
docker pull tensorflow/serving
```
- 部署 SavedModel：
```bash
docker run -p 8501:8501 --mount type=bind,source=$(pwd)/models/,target=/models/serving_model -e MODEL_NAME=serving_model tensorflow/serving
```
- REST API 调用：
```bash
curl -d '{"instances": [[1.0, 2.0, 5.0]]}' -H "Content-Type: application/json" -X POST http://localhost:8501/v1/models/serving_model:predict
```

---

### ✅ Day 17 - SavedModel 与 Checkpoint
- SavedModel：完整保存模型结构、权重
```python
model.save('saved_model/your_model')
```
- 加载：
```python
loaded_model = tf.keras.models.load_model('saved_model/your_model')
```
- Checkpoint：保存训练状态、便于恢复训练
```python
ckpt = tf.train.Checkpoint(model=model, optimizer=optimizer)
ckpt.save('checkpoints/ckpt')
```

---

### ✅ Day 18 - TensorFlow Lite 转换
- 导出 TFLite：
```python
converter = tf.lite.TFLiteConverter.from_saved_model('saved_model/your_model')
tflite_model = converter.convert()
```
- 推理：适用于移动端、嵌入式设备

---

### ✅ Day 19 - TPU 训练
- 在 Colab 上启用 TPU：
```python
resolver = tf.distribute.cluster_resolver.TPUClusterResolver()
tf.config.experimental_connect_to_cluster(resolver)
tf.tpu.experimental.initialize_tpu_system(resolver)
strategy = tf.distribute.TPUStrategy(resolver)
```
- TPU 特性：高吞吐、低延迟、大规模训练

---

### ✅ Day 20 - 模型剪枝 & 量化
- 使用 `tensorflow_model_optimization`
```bash
pip install tensorflow-model-optimization
```
- 剪枝：减少模型冗余
- 量化：压缩模型大小，提升推理速度

---

### ✅ Day 21 - TensorFlow Hub 预训练模型
- 直接加载 Hub 模型：
```python
import tensorflow_hub as hub
model = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/nnlm-en-dim50/2", input_shape=[], dtype=tf.string)
])
```
- 场景：文本嵌入、图像特征提取、迁移学习

---


## 📒 第四阶段学习笔记：Day 22 ~ Day 30+

---

### ✅ Day 22 - Eager Execution 与 Graph 模式
- Eager：即时执行，调试方便
- Graph：静态图，优化后速度快
- 使用 `@tf.function` 自动转换：
```python
@tf.function
def f(x):
    return x ** 2
```

---
### ✅ Day 23 - tf.function 源码机制
- Autograph：将 Python 控制流转为 TensorFlow op
- GraphDef：TensorFlow 计算图的底层数据结构
- Trace / ConcreteFunction：缓存优化机制

---

### ✅ Day 24 - TensorFlow I/O 与自定义 Dataset
- TensorFlow I/O：CSV、Parquet、AVRO、Video、Kafka 等数据读取
- 自定义 Dataset：
```python
class MyDataset(tf.data.Dataset):
    def _generator():
        for i in range(1000):
            yield i, i**2
    def __new__(cls):
        return tf.data.Dataset.from_generator(cls._generator, output_types=(tf.int32, tf.int32))
```

---

### ✅ Day 25 - 分布式策略源码剖析
- MirroredStrategy、MultiWorkerStrategy、TPUStrategy
- 分布式变量同步机制
- Collective Ops 通信框架

---

### ✅ Day 26 - 自定义 Kernel（C++ 实现）
- 自定义 op 实现：C++ + TensorFlow Python 包装
- 实战：自定义矩阵求逆 Kernel
- 参考：https://www.tensorflow.org/guide/create_op

---

### ✅ Day 27 - XLA 编译优化
- XLA：Accelerated Linear Algebra，图优化编译器
- 减少 op 次数、优化数据布局
- 启用方式：
```bash
TF_XLA_FLAGS=--tf_xla_enable_xla_devices python your_script.py
```

---

### ✅ Day 28 - Serving 源码阅读
- 主要组件：loader、predictor、request handler
- gRPC 与 RESTful API 交互机制

---

### ✅ Day 29 - TPU Runtime 与分布式调度
- TPU Runtime：TPU 上的 op 调度器
- 分布式训练：任务调度、Fault Recovery

---

### ✅ Day 30 - TensorFlow 社区贡献
- 阅读 issue / pull request
- 按照 Contributor Guide 贡献代码：https://www.tensorflow.org/community/contribute
- 常见贡献方式：修复 bug、完善文档、添加测试

---

### ✅ 后续持续学习方向
- 深入学习 XLA、MLIR、TensorFlow Core
- 与 PyTorch、JAX、ONNX 框架对比学习
- 参与开源社区，持续维护项目


# ✅ TensorFlow 系统学习全流程方案

...（前略）...

## 📓 第五阶段学习计划：Scikit-learn 入门 7 天

---

### ✅ Day 1 - Scikit-learn 安装与数据探索
- 安装：
```bash
pip install scikit-learn
```
- 常用数据集：iris, digits, wine
- 数据加载与探索：
```python
from sklearn.datasets import load_iris
import pandas as pd

data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
print(df.describe())
```

---

### ✅ Day 2 - 线性回归 / 逻辑回归
- 回归问题：预测连续值
- 分类问题：预测类别标签
- 示例：
```python
from sklearn.linear_model import LinearRegression, LogisticRegression
model = LinearRegression().fit(X_train, y_train)
print(model.score(X_test, y_test))
```

---

### ✅ Day 3 - 决策树 / 随机森林
- 决策树：可视化好、易于理解
- 随机森林：集成多个树，防止过拟合
- 示例：
```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100).fit(X_train, y_train)
preds = model.predict(X_test)
```

---

### ✅ Day 4 - 支持向量机 (SVM)
- 适用于小规模、高维数据
- 示例：
```python
from sklearn.svm import SVC
model = SVC(kernel='linear').fit(X_train, y_train)
```

---

### ✅ Day 5 - 无监督学习 (KMeans / PCA)
- KMeans 聚类：
```python
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3).fit(X)
```
- PCA 降维：
```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2).fit_transform(X)
```

---

### ✅ Day 6 - 模型评估与优化
- 交叉验证：`cross_val_score`
- 网格搜索：`GridSearchCV`
```python
from sklearn.model_selection import GridSearchCV
param_grid = {'C': [0.1, 1, 10]}
gs = GridSearchCV(SVC(), param_grid, cv=3)
gs.fit(X_train, y_train)
```

---

### ✅ Day 7 - Pipeline 与持久化
- Pipeline：将预处理、训练、预测串联
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC())
])
pipeline.fit(X_train, y_train)
```
- 模型保存：
```python
import joblib
joblib.dump(pipeline, 'model.pkl')
```

---


## 📔 第六阶段学习计划：NumPy & Pandas 7 天

---
🛠 1. NumPy 是什么？

Python 的 “科学计算引擎”

	•	高效矩阵运算：数组（ndarray）
	•	线性代数、傅里叶变换、统计分析
	•	性能高，底层用 C 实现

📊 2. Pandas 是什么？

Python 的 “数据表处理专家”

	•	类似 Excel、SQL 的表格处理
	•	读写 CSV、Excel、SQL、JSON
	•	数据清洗、筛选、聚合、透视表



### ✅ Day 1 - NumPy 基础
- ndarray 创建
- 基本属性：shape、dtype
- 常用初始化：zeros、ones、arange、linspace

示例：
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.zeros((2, 3))
c = np.arange(0, 10, 2)
```

---

### ✅ Day 2 - NumPy 运算
- 数学运算：加减乘除、矩阵乘法
- 广播机制
- 聚合函数：sum、mean、max、std

示例：
```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x + y)
print(np.dot(x, y))
```

---

### ✅ Day 3 - Pandas 基础
- Series、DataFrame 创建
- 读取 CSV / Excel / JSON
- head(), describe(), info()

示例：
```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())
```

---

### ✅ Day 4 - Pandas 数据清洗
- 缺失值处理：fillna, dropna
- 重命名列名：rename
- 类型转换：astype

示例：
```python
df = df.dropna()
df["price"] = df["price"].astype(float)
```

---

### ✅ Day 5 - Pandas 数据筛选与切片
- 按列、行筛选
- 条件筛选：df[df["price"] > 100]
- loc / iloc 的使用

示例：
```python
print(df.loc[0:5, ["name", "price"]])
```

---

### ✅ Day 6 - Pandas 分组与聚合
- groupby：按某列统计
- pivot_table：透视表
- apply：自定义函数处理

示例：
```python
print(df.groupby("category")["price"].mean())
```

---

### ✅ Day 7 - Pandas 合并与存储
- merge：数据表关联
- concat：多表拼接
- to_csv(), to_excel()

示例：
```python
result = pd.merge(df1, df2, on="id", how="inner")
result.to_csv("result.csv", index=False)
```

🔍 1. Matplotlib 是什么？

Python 最基础、最底层的绘图库，类似于 Excel 里的 折线图、柱状图、散点图。

	•	API 类似 MATLAB，几乎所有 Python 绘图库都基于它
	•	可绘制：折线、散点、柱状、饼图、直方图、热力图、3D 图
🌟 2. Seaborn 是什么？

基于 Matplotlib，做了更高级、更漂亮的封装，默认主题美观，适合统计图表绘制。

	•	一行代码画出漂亮图表
	•	常用统计图：分类条形图、箱线图、热力图、回归图、分布图
	•	与 Pandas DataFrame 配合最好用
    
🔧 3. 常见图表类型
图表        Matplotlib 函数     Seaborn 函数
折线图      plt.plot()          无直接支持
散点图      plt.scatter()       sns.scatterplot()
柱状图      plt.bar()           sns.barplot()
直方图      plt.hist()          sns.histplot()
箱线图      plt.boxplot()       sns.boxplot()
热力图      需手工绘制            sns.heatmap()
分布图      plt.hist()          sns.displot()
回归拟合图   无直接支持           sns.lmplot()

---

### ✅ Day 1 - Matplotlib 基础绘图
- 绘制折线图、散点图、柱状图
- 添加标题、坐标轴标签

示例：
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y, label='Line')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Simple Plot')
plt.legend()
plt.show()
```

---

### ✅ Day 2 - Matplotlib 高级设置
- 多子图（subplot）
- 自定义颜色、线型、刻度
- 保存图像：`plt.savefig()`

示例：
```python
plt.subplot(2, 1, 1)
plt.plot([1, 2, 3], [1, 4, 9])

plt.subplot(2, 1, 2)
plt.bar(['A', 'B', 'C'], [5, 7, 3])
plt.savefig('output.png')
plt.show()
```

---

### ✅ Day 3 - Seaborn 快速可视化
- 读取示例数据：tips、iris
- 绘制分类柱状图、箱线图、散点图

示例：
```python
import seaborn as sns
df = sns.load_dataset('tips')
sns.barplot(x='day', y='total_bill', data=df)
plt.show()
```

---

### ✅ Day 4 - Seaborn 分布图与回归图
- 绘制直方图、核密度估计：`sns.histplot()`, `sns.kdeplot()`
- 绘制回归拟合图：`sns.lmplot()`

示例：
```python
sns.histplot(df['total_bill'])
sns.lmplot(x='total_bill', y='tip', data=df)
plt.show()
```

---

### ✅ Day 5 - 热力图与相关性分析
- 计算相关系数：`df.corr()`
- 绘制热力图：`sns.heatmap()`

示例：
```python
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()
```

---

### ✅ Day 6 - 图表美化
- 调整颜色：`palette`, `cmap`
- 主题风格切换：`sns.set_theme()`
- 图表布局优化：`plt.tight_layout()`

示例：
```python
sns.set_theme(style='whitegrid')
sns.boxplot(x='day', y='total_bill', data=df, palette='pastel')
plt.tight_layout()
plt.show()
```

---

### ✅ Day 7 - 实战项目：销售数据可视化
- 加载 CSV，绘制时间序列趋势
- 产品销量对比、区域销售热力图

示例：
```python
df = pd.read_csv('sales.csv')
sns.lineplot(x='date', y='sales', hue='product', data=df)
plt.show()
```

---

