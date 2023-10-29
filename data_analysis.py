import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV 
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn import metrics 
import matplotlib.pyplot as plt

def display(results):
    print(f'Best parameters are: {results.best_params_}')
    print("\n")
    mean_score = results.cv_results_['mean_test_score']
    std_score = results.cv_results_['std_test_score']
    params = results.cv_results_['params']
    for mean,std,params in zip(mean_score,std_score,params):
        print(f'{round(mean,3)} + or -{round(std,3)} for the {params}')

ready_file_path = 'BBB_Data/ReadyData.csv'

ready_df = pd.read_csv(ready_file_path)

matrix = ready_df.drop(columns=['Proteins']).corr()

result_df = pd.DataFrame(ready_df.pop('Value'))
ready_df.pop('Proteins')
ready_df.pop('A')
ready_df.pop('C')
ready_df.pop('D')
ready_df.pop('E')
ready_df.pop('F')
ready_df.pop('G')
ready_df.pop('H')
ready_df.pop('I')
ready_df.pop('K')
ready_df.pop('L')
ready_df.pop('M')
ready_df.pop('N')
ready_df.pop('P')
ready_df.pop('Q')
ready_df.pop('R')
ready_df.pop('S')
ready_df.pop('T')
ready_df.pop('V')
ready_df.pop('W')
ready_df.pop('Y')

ready_df.round(3)

feature_list = list(ready_df.columns)

X_train, X_test, y_train, y_test = train_test_split(ready_df, result_df, test_size = 0.30) 
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#*****GridSearchForRandomForrest******
# parameters = {
#     "n_estimators":[5,10,50,100,250,500,1000,2000],
#     "max_depth":[2,4,8,16,32,65,128,256,512,1024]  
# }
# cv = GridSearchCV(RandomForestClassifier(),parameters,cv=5)
# cv.fit(X_train, y_train.values.ravel())

# display(cv)

#******GridSearchForSVM******
# parameters = {'C': [0.1, 1, 10, 100, 1000],  
#               'gamma': [1, 0.1, 0.01, 0.001, 0.0001], 
#               'kernel': ['rbf','linear']}  
# grid = GridSearchCV(SVC(), parameters, refit = True, verbose = 3) 
# grid.fit(X_train, y_train.values.ravel())
# display(grid)
  
clf = RandomForestClassifier(n_estimators = 5, max_depth = 2, criterion="entropy", verbose = True)  
clf.fit(X_train, y_train.values.ravel()) 

clf2 = SVC(kernel = 'rbf', C = 0.1, gamma = 1, verbose = True) 
clf2.fit(X_train, y_train.values.ravel())

logisticRegr = LogisticRegression()
logisticRegr.fit(X_train, y_train.values.ravel())

#*****ImportantFeatureSearch******
# importances = list(clf.feature_importances_)

# feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
# feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
# # [print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances]

# x_values = list(range(len(importances)))

# plt.bar(x_values, importances, orientation = 'vertical', color = 'r', edgecolor = 'k', linewidth = 1.2)
# plt.xticks(x_values, feature_list, rotation='vertical')
# plt.ylabel('Importance'); plt.xlabel('Variable'); plt.title('Variable Importances')
# plt.show()

y_pred = clf.predict(X_train) 
print("RF FIT OF THE MODEL: ", metrics.accuracy_score(y_train, y_pred)) 

y_pred = clf.predict(X_test) 
print("RF ACCURACY OF THE MODEL: ", metrics.accuracy_score(y_test, y_pred)) 

y_pred = clf2.predict(X_train) 
print("SVM FIT OF THE MODEL: ", metrics.accuracy_score(y_train, y_pred)) 

y_pred = clf2.predict(X_test) 
print("SVM ACCURACY OF THE MODEL: ", metrics.accuracy_score(y_test, y_pred)) 

score = logisticRegr.score(X_test, y_test)
print("Logistic Regression ACCURACY: ",score)

