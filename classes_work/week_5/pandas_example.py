import numpy as np
import pandas as pd

    # NumPy array
arr = np.array([1, 2, 3, 4, 5])

    # Pandas DataFrame from a dictionary
# Create a Pandas DataFrame from a dictionary
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})
print("\nPandas DataFrame:\n", df)

# Filter data in the DataFrame
print("\nFiltered data (Age > 30):\n", df[df['Age'] > 30])
