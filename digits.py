from sklearn.datasets import load_digits
digits = load_digits()

#print(type(digits))
#print( digits.data)
#print( digits.target_names)

X = digits.data
y = digits.target

from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100)
clf.fit(X,y)
print('Prediction:',clf.predict(digits.data[-1]))
print('Actual:', y[-1])
