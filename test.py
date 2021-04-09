from sklearn import *
import pandas
import pickle
loaded_model = pickel.load(open(file,'rb'))
result = loaded_model.score(X_test, y_test)
print(result)