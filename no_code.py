import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=100):
        self.weights = np.random.rand(input_size + 1)
        self.learning_rate = learning_rate
        self.epochs = epochs

    def weighted_sum(self, inputs):
        return np.dot(inputs, self.weights)

    def activation_function(self, x):
        return np.where(x >= 0, 1, 0)

    def predict(self, inputs):
        z = self.weighted_sum(inputs)
        return self.activation_function(z)

    def loss_function(self, prediction, target):
        return (prediction - target) ** 2

    def fit(self, training_inputs, labels):
        for epoch in range(1, self.epochs + 1):
            epoch_loss = 0
            correct = 0

            for inputs, label in zip(training_inputs, labels):

                inputs = np.insert(inputs, 0, 1)  # bias

                z = self.weighted_sum(inputs)
                prediction = self.activation_function(z)

                update = self.learning_rate * (label - prediction)
                self.weights += update * inputs

                epoch_loss += self.loss_function(prediction, label)

                if prediction == label:
                    correct += 1

            acc = correct / len(labels)
            print(f"Epoch {epoch} | Accuracy: {acc:.2%} | Loss: {epoch_loss:.4f}")
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

iris = load_iris()

X = iris.data
y = (iris.target == 0).astype(int)  # 1 for Setosa, 0 for non-Setosa

# scaler = MinMaxScaler()
# X = scaler.fit_transform(X)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# perceptron = Perceptron(input_size=4)
# perceptron.fit(X_train, y_train)