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
import fair4ai_client.main as f4a
from skl2onnx.common.data_types import FloatTensorType

f4a.wrap(clr, {'initial_types': [('float_input', FloatTensorType([None, 4]))]})