import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
​
#For plotting graphs
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_regression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score,confusion_matrix,roc_auc_score, r2_score
​
# all different models used here
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
​
#to ignore warning
import warnings
warnings.filterwarnings('ignore')
heart=pd.read_csv("Heart.csv")
heart.head()
