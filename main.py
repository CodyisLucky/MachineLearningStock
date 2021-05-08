import matplotlib.pyplot as plot

from sklearn import datasets #allows us to label our data
from sklearn import svm #support vector machine (divides groups on the data plot)

digits = datasets.load_digits()

#clarifier
clf = svm.SVC(gamma=0.001, C=100)

x,y = digits.data[:-10], digits.target[:-10] #testing set, stores all but last data to test against the last data
clf.fit(x,y)

print('Prediction:',clf.predict(digits.data[[-7]]))

plot.imshow(digits.images[-7], cmap=plot.cm.gray_r, interpolation="nearest")

plot.show()

