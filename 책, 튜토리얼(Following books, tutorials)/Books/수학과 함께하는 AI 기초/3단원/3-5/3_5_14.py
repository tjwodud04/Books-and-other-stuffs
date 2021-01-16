import pandas as pd
import numpy as np

class my_NN01:
    # 클래스 생성자(객체 생성시 호출됨)를 선언한다.
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # 입력층, 은닉층, 출력층 노드 갯수
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        # 은닉층의 파라미터 W1,B1을 초기화
        self.W1 = np.random.rand(self.input_nodes, self.hidden_nodes) / np.sqrt(self.input_nodes / 2)
        self.B1 = np.random.rand(self.hidden_nodes)
        # 출력층 파라미터 W2,B2을 초기화
        self.W2 = np.random.rand(self.hidden_nodes, self.output_nodes) / np.sqrt(self.hidden_nodes / 2)
        self.B2 = np.random.rand(self.output_nodes)
        # 학습률 learning rate 초기화
        self.learning_rate = learning_rate

    # 순전파
    def feed_forward(self):
        delta = 1e-7
        A1 = np.dot(self.input_data, self.W1) + self.B1
        Z1 = sigmoid(A1)
        A2 = np.dot(Z1, self.W2) + self.B2
        y = sigmoid(A2)

        return -np.sum(self.target_data * np.log(y + delta) + (1 - self.target_data) * np.log((1 - y) + delta))

    # 손실
    def cost(self):
        delta = 1e-7
        A1 = np.dot(self.input_data, self.W1) + self.B1
        Z1 = sigmoid(A1)
        A2 = np.dot(Z1, self.W2) + self.B2
        y = sigmoid(A2)
        cost_val = -np.sum(self.target_data * np.log(y + delta) + (1 - self.target_data) * np.log((1 - y) + delta))

        return cost_val

    # 학습
    def train(self, input_data, target_data):
        self.input_data = input_data
        self.target_data = target_data

        f = lambda x: self.feed_forward()

        self.W1 -= self.learning_rate * numerical_derivative(f, self.W1)
        self.B1 -= self.learning_rate * numerical_derivative(f, self.B1)
        self.W2 -= self.learning_rate * numerical_derivative(f, self.W2)
        self.B2 -= self.learning_rate * numerical_derivative(f, self.B2)

    # 예측
    def predict(self, input_data):
        A1 = np.dot(self.input_data, self.W1) + self.B1
        Z1 = sigmoid(A1)
        A2 = np.dot(Z1, self.W2) + self.B2
        y = sigmoid(A2)
        predicted_num = np.argmax(y)

        return predicted_num

    # 정확도
    def accuracy(self, test_data):
        matched_list = []
        not_matched_list = []

        for index in range(len(test_data)):
            label = int(test_data[index, 0])
            data = (test_data[index, 1:] / 255.0 * 0.99) + 0.01
            predicted_num = self.predict(np.array(data, ndmin=2))

            if label == predicted_num:
                matched_list.append(index)
            else:
                not_matched_list.append(index)

        print("정확도 : ", 100 * (len(matched_list) / (len(test_data))), " %")

        return matched_list, not_matched_list

# 데이터
df_train = pd.read_csv('fashion-mnist_train.csv')
df_test = pd.read_csv('fashion-mnist_test.csv')

# 학습(train) 데이터를 입력변수와 출력변수로 나누기
data_train = np.array(df_train, dtype=np.float32)

# 테스트(test) 데이터를 입력변수와 출력변수로 나누기
data_test = np.array(df_test, dtype=np.float32)

def sigmoid(X):
    return 1 / (1 + np.exp(-X))

def numerical_derivative(f, x):
    delta_x = 1e-4  # 0.0001
    grad = np.zeros_like(x)
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])

    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + delta_x
        fx1 = f(x)
        x[idx] = tmp_val - delta_x
        fx2 = f(x)
        grad[idx] = (fx1 - fx2) / (2 * delta_x)
        x[idx] = tmp_val
        it.iternext()

    return grad

# 모델 객체를 만들기
my_model = my_NN01(784, 100, 10, 0.01)
cost_val_list = []

for step in range(len(data_train)):
    input_data = ((data_train[step, 1:] / 255.0) * 0.99) + 0.01
    target_data = np.zeros(10) + 0.01
    target_data[int(data_train[step, 0])] = 0.99

    my_model.train(input_data, target_data)

    if (step % 200 == 0):
        print("단계: ", step, ", 비용(손실)값: ", my_model.cost())

    cost_val_list.append(my_model.cost())

my_model.accuracy(data_test)
