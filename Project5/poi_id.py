#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi', 'exercised_stock_options', 'fraction_to_poi', 'other', 'shared_receipt_with_poi', 'expenses']

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers

del data_dict['TOTAL']
del data_dict['THE TRAVEL AGENCY IN THE PARK']

belfer = data_dict['BELFER ROBERT']
belfer['deferred_income'] = -102500
belfer['deferral_payments'] = 'NaN'
belfer['expenses'] = 3285
belfer['exercised_stock_options'] = 'NaN'
belfer['director_fees'] = 102500
belfer['restricted_stock'] = 44093
belfer['restricted_stock_deferred'] = -44093
belfer['total_payments'] = 3285
belfer['total_stock_value'] = 'NaN'

bhatnagar = data_dict['BHATNAGAR SANJAY']
bhatnagar['expenses'] = 137864
bhatnagar['director_fees'] = 'NaN'
bhatnagar['other'] = 'NaN'
bhatnagar['total_payments'] = 137864
bhatnagar['exercised_stock_options'] = 15456290
bhatnagar['restricted_stock'] = 2604490
bhatnagar['restricted_stock_deferred'] = -2604490
bhatnagar['total_stock_value'] = 15456290

### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.

def fraction(subset, all):
    fraction = 0.0
    if all != 'NaN' and subset != 'NaN':
        fraction = float(subset) / float(all)
    return fraction

for data in data_dict.values():
    data['fraction_to_poi'] = fraction(data['from_this_person_to_poi'], data['from_messages'])
    data['fraction_from_poi'] = fraction(data['from_poi_to_this_person'], data['to_messages'])
    
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth=4, max_features=None, max_leaf_nodes=None, min_samples_leaf=4, min_samples_split=3, criterion='entropy')

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html


# The model is already tuned, see the accompanying juypter notebooks.
    

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)