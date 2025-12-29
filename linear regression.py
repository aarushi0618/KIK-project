import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('train.csv')# .read_csv=parse the text from folder train.csv and store in structured way,df=dataframe i.e variable name

#  FEATURE ENGINEERING (Bonus Task)

df['TotalSF'] = df['TotalBsmtSF'] + df['1stFlrSF'] + df['2ndFlrSF']#Go into the table (df), create a new column called 'TotalSF', and for every single row, add up the values found in 'TotalBsmtSF', '1stFlrSF', and '2ndFlrSF

# Let's pick a few strong numerical features i.e feature selection
features = ['TotalSF', 'OverallQual', 'GrLivArea', 'GarageCars']
X = df[features].copy()#jate kokhono original df change na hoy
y = df['SalePrice'].values#.values: This converts the Pandas column into a NumPy array.

# Handle missing values - simple mean imputation
X = X.fillna(X.mean())#This technique is called Mean Imputation. By filling a gap with the average, you are making a "safe bet."


# FEATURE SCALING (Crucial for Gradient Descent)
# If we don't do this, the 'TotalSF' (thousands) will overwhelm 'OverallQual' (1-10)OverallQual: A rating of the house's material and finish.
X_mean = X.mean()#calculates the mean of each column
X_std = X.std()#calculates the standard deviation of each column
X_scaled = (X - X_mean) / X_std

# Convert to numpy arrays for the math
X_matrix = X_scaled.values
y_vector = y.reshape(-1, 1)#-1 joto gulo rows lagbe and column=1

# IMPLEMENTING LINEAR REGRESSION FROM SCRATCH 
m, n = X_matrix.shape  # m = rows, n = features
W = np.zeros((n, 1))   # weights
b = 0                  # bias

learning_rate = 0.01
epochs = 2000
cost_history = []

print(f"Training on {m} samples with {n} features...")

for i in range(epochs):
    
    predictions = np.dot(X_matrix, W) + b
    
    # Cost Function (Mean Squared Error)
    
    error = predictions - y_vector
    cost = (1 / (2 * m)) * np.sum(np.square(error))
    cost_history.append(cost)
    
    # Gradient Descent 
   
    dW = (1 / m) * np.dot(X_matrix.T, error)
    db = (1 / m) * np.sum(error)
    
    
    W = W - learning_rate * dW
    b = b - learning_rate * db
    
    if i % 200 == 0:
        print(f"Epoch {i}: Error (Cost) is {cost:.4f}")

#  VISUALIZING RESULTS 
plt.plot(cost_history)
plt.title("Error Over Time (Cost Function)")
plt.xlabel("Epochs")
plt.ylabel("Mean Squared Error")
plt.show()

print("\nFinal Model Parameters:")
print("Weights:", W.flatten())
print("Bias:", b)

