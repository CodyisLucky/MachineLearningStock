import matplotlib.pyplot as plot

from sklearn import datasets #allows us to label our data
from sklearn import svm #support vector machine (divides groups on the data plot)

digits = datasets.load_digits()

#clarifier
clf = svm.SVC(gamma=0.001, C=100)

x,y = digits.data[:-1], digits.target[:-1] #testing set, stores all but last data to test against the last data
clf.fit(x,y)

print('Prediction:',clf.predict(digits.data[-1]))

plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")

plt.show()