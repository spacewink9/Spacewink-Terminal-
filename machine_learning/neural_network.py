import numpy as np
import tensorflow as tf

class NeuralNetwork:
    def __init__(self, input_size, output_size, hidden_layers, learning_rate=0.001, activation_function='relu', optimizer='adam'):
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_layers = hidden_layers
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.optimizer = optimizer
        self.model = self._build_model()

    def _build_model(self):
        model = tf.keras.Sequential()
        # Input layer
        model.add(tf.keras.layers.Input(shape=(self.input_size,)))
        # Hidden layers
        for num_neurons in self.hidden_layers:
            model.add(tf.keras.layers.Dense(num_neurons, activation=self.activation_function))
        # Output layer
        model.add(tf.keras.layers.Dense(self.output_size, activation='softmax'))
        # Compile model
        model.compile(optimizer=self.optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def train(self, X_train, y_train, epochs=100, batch_size=32, verbose=1):
        y_train = np.eye(self.output_size)[y_train] # One-hot encode the labels
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, verbose=verbose)

    def predict(self, X):
        return np.argmax(self.model.predict(X), axis=1)

    def evaluate(self, X_test, y_test):
        y_test = np.eye(self.output_size)[y_test] # One-hot encode the labels
        return self.model.evaluate(X_test, y_test)
    
    def save_model(self, path):
        self.model.save(path)
        
    def load_model(self, path):
        self.model = tf.keras.models.load_model(path)
