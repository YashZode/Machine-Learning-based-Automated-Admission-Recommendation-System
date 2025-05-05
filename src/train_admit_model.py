# --------------------------------------------
# File: train_admit_model.py
# Description:
#   Trains Linear Regression model for graduate admission prediction.
#   Final model saved to models/admit_model.pkl
# --------------------------------------------

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# 01- Load Data
csv_path = "E:/Spring_2025/CapstoneProject/13th April 2025______Final/ShowTime(YASH)/data/Admission_Predict.csv"
data = pd.read_csv(csv_path)
print(data.columns.tolist())

data.rename(columns=lambda x: x.strip().replace(" ", "_"), inplace=True)
data.drop(columns=["Serial_No."], errors='ignore', inplace=True)  # remove serial number if exists

# 02- Exploratory Data Analysis (optional heatmap)
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("E:/Spring_2025/CapstoneProject/13th April 2025______Final/ShowTime(YASH)/data/correlation_heatmap_updated.png")

# 03- Prepare training data
features = [
    "GRE_Score", "TOEFL_Score", "University_Rating",
    "SOP", "LOR", "CGPA", "Research"
]
target = "Chance_of_Admit"

X = data[features]
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 04- Train Linear Regression
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

# 05- Evaluation
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

# 06- Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/admit_model.pkl")

# 07- Report
print("\n✅ Model Training Completed")
print(f"MAE:  {mae:.4f} | RMSE: {rmse:.4f} | R²: {r2:.4f}")


import matplotlib.pyplot as plt
import numpy as np

# Assuming y_test and y_pred are already defined (from your model evaluation)
residuals = y_test.values - y_pred  # Get the residuals (errors)

# Create histogram for residuals
plt.figure(figsize=(4, 3))
plt.hist(residuals, bins=20, edgecolor='black')
plt.title("Error Distribution\n(Residuals of Linear Regression)")
plt.xlabel("Prediction Error (y_true – y_pred)")
plt.ylabel("Frequency")
plt.axvline(0, color='red', linestyle='--', linewidth=1)
plt.tight_layout()

# Save the plot
plt.savefig("E:/Spring_2025/CapstoneProject/13th April 2025______Final/ShowTime(YASH)/data/residuals_histogram.png", dpi=900)
# plt.savefig("histogram.png", dpi=900)


# Optionally display the plot
# plt.show()
