#신경망 모델 클래스
class my_NN01:
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):      
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        
        # 은닉층 가중치  W2  Xavier/He 방법으로 self.W2 가중치 초기화
        self.W1 = np.random.rand(self.input_nodes, self.hidden_nodes) / np.sqrt(self.input_nodes/2)
        self.B1 = np.random.rand(self.hidden_nodes)      
        
        # 출력층 가중치는 W3  Xavier/He 방법으로 self.W3 가중치 초기화
        self.W2 = np.random.rand(self.hidden_nodes, self.output_nodes) / np.sqrt(self.hidden_nodes/2)
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

        return  -np.sum(self.target_data*np.log(y + delta) + (1-self.target_data)*np.log((1 - y)+delta ))

    # 비용 값 계산
    def cost(self):      
        delta = 1e-7
        A1 = np.dot(self.input_data, self.W1) + self.B1
        Z1 = sigmoid(A1)     
        A2 = np.dot(Z1, self.W2) + self.B2
        y = sigmoid(A2)
        cost_val=-np.sum(self.target_data*np.log(y + delta) + (1-self.target_data)*np.log((1 - y)+delta ))

        return  cost_val

    # 수치미분을 이용하여 손실함수가 최소가 될때 까지 학습하는 함수
    def train(self, input_data, target_data):
        self.input_data = input_data
        self.target_data = target_data
        
        f = lambda x : self.feed_forward()
        
        self.W1 -= self.learning_rate * numerical_derivative(f, self.W1)
        self.B1 -= self.learning_rate * numerical_derivative(f, self.B1)
        self.W2 -= self.learning_rate * numerical_derivative(f, self.W2)
        self.B2 -= self.learning_rate * numerical_derivative(f, self.B2)

        return 0
    
    # 미래 값 예측 함수
    def predict(self, input_data):          
        A1 = np.dot(self.input_data, self.W1) + self.B1
        Z1 = sigmoid(A1)   
        A2 = np.dot(Z1, self.W2) + self.B2
        y = sigmoid(A2)
        # MNIST 경우는 one-hot encoding 을 적용하기 때문에 0 또는 1 이 아닌 argmax() 를 통해 최대 인덱스를 넘겨주어야 함
        predicted_num = np.argmax(y)

        return predicted_num

    # 정확도 측정함수
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

        print("정확도 : ", 100*(len(matched_list)/(len(test_data))), " %")

        return matched_list, not_matched_list