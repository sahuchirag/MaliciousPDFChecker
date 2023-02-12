from pandas import read_csv
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

df = read_csv('normalized_pdfdataset.csv')
X = df.iloc[:, 0: 21]
y = df.iloc[:, 21]
X_train, X_test, y_train, y_test = train_test_split(X.values, y, test_size=0.3)

print("---Random Forest---")
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
pickle.dump(clf, open('model.pkl', 'wb'))
y_pred = clf.predict(X_test)
acs = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
print("Accuracy:", acs)
print("\nConfusion Matrix:\n", cm)

print("---Naives Bayes---")
#Naives Bayes
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X.values, y, test_size = 0.3) #, random_state = 42)

from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(x_train, y_train)
y_pred = nb.predict(x_test)
from sklearn import metrics
print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)
# print("Naive Bayes score: ",nb.score(x_test, y_test))

print("---Decision Tree---")
from sklearn.tree import DecisionTreeClassifier  
from sklearn.model_selection import train_test_split  
xdt_train, xdt_test, ydt_train, ydt_test= train_test_split(X.values, y, test_size= 0.3, random_state=0)
classifier= DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier.fit(xdt_train, ydt_train) 
ydt_pred= classifier.predict(xdt_test)
print("DT Accuracy: ", metrics.accuracy_score(ydt_test, ydt_pred))

# path = '/home/chirag/Documents/Malicious_pdf_detection-master/test2.pdf'
# features = feature_extraction(path)
# result = clf.predict(features)
# print(result)

# result2 = nb.predict(features)
# print(result2)

# result3 = classifier.predict(features)
# print(result3)

