# Train a model.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y)
clr = RandomForestClassifier()
clr.fit(X_train, y_train)

# wrap the model

# --- these lines ensure that the live code at the root is used 
# --- above the installed package
import sys
sys.path.insert(0, '.')
# ---

import fair4ai_client.main as f4a

from skl2onnx.common.data_types import FloatTensorType

# 1. directly upload the onnx representation to the server, 
#    but have cli inputs (doesnt work in notebooks, but is more convenient)
# f4a.wrap(clr, 'upload', {'initial_types': [('float_input', FloatTensorType([None, 4]))]})

# 2. store the onnx representation to local disk, to upload it to the 
#    
f4a.wrap_store(clr, 'output/iris_model', {'initial_types': [('float_input', FloatTensorType([None, 4]))]})
