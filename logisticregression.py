import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('train(1).csv')
df['TotalSF'] = df['Parch'] + df['SibSp'] 
features = ['TotalSF','Pclass','Sex','Age','Fare']
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
X = df[features].copy()
y=df['Survived'].values
X = X.fillna(X.mean())

X_matrix = X.values
y_vector = y.reshape(-1, 1)

learning_rate = 0.01
epochs = 2000 #10 Epochs: The model has "re-read" the entire dataset 10 times.
cost_history = []

m, n = X_matrix.shape  # m = rows, n = features
W = np.zeros((n, 1))   # weights
b = 0     
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
for i in range(epochs):
  z=np.dot(X_matrix,W)+b
  
  f=sigmoid(z)
  p=y*np.log(f)+(1-y)*np.log(1-f)
  J=(-1/m)*np.sum(p)
  error=z-y

  dW = (1 / m) * np.sum( np.dot(X_matrix.T, error))
  db = (1 / m) * np.sum(error)

  W = W - learning_rate * dW
  b = b - learning_rate * db

  

  if(f>0.5):
    print("Can't survive")
 
  elif(f<0.5):
    print("survive")
  if i % 200 == 0:
        print(f"Epoch {i}: Error (Cost) is {J:.4f}")
  
  

#  VISUALIZING RESULTS 
plt.plot(cost_history)
plt.title("Error Over Time (Cost Function)")
plt.xlabel("Epochs")
plt.ylabel("Mean Squared Error")
plt.show()

print("\nFinal Model Parameters:")
print("Weights:", W.flatten())
print("Bias:", b)


    
