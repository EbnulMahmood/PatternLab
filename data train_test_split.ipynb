import pandas as pd
#dataset: https://vincentarelbundock.github.io/Rdatasets/datasets.html (flchain.csv)
data = pd.read_csv('flchain.csv', delimiter=',')
len(data)

#age = age in years, 
#sex = F=female, M=male, 
#sample.yr = the calendar year in which a blood sample was obtained,
#kappa = serum free light chain, kappa portion,
#lambda = serum free light chain, lambda portion,
#flc.grp = the FLC group for the subject, as used in the original analysis,
#creatinine = serum creatinine,
#mgus = 1 if the subject had been diagnosed with monoclonal gammapothy (MGUS),
#futime = days from enrollment until death. Note that there are 3 subjects whose sample was obtained on their death date,
#death = 0=alive at last contact date, 1=dead,
#chapter = for those who died, a grouping of their primary cause of death by chapter headings of the International Code of Diseases ICD-9.

data.head()
column_target = ['death']
columns_train = ['age', 'sex', 'kappa', 'lambda', 'flc.grp', 'creatinine', 'mgus', 'futime'] #, 'chapter']

X = data[columns_train]
Y = data[column_target]

#NaN value present in data
X['creatinine'].isnull().sum()
#X['chapter'].isnull().sum()

#fill NaN value with Mean or Mediam value
X['creatinine'] = X['creatinine'].fillna(X['creatinine'].median())

#Let F = 1, M = 0
d = {'F':0, 'M':1}
X['sex'] = X['sex'].apply(lambda x:d[x])
X.head()

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .33, random_state = 10)
