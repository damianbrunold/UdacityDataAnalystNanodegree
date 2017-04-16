# Documentation

I used both for data exploration as well as for model building jupyter notebooks.
This allowed me to conveniently experiment and optimize my code, while at the same
time documenting my steps. Thus, dear evaluator, please refer to the provided
jupyter notebooks or alternatively the HTML-snapshots for any details.

In this document, I try to document and explain on a higher level what I tried
and accomplished in this project. I also try to answer the questions provided
by udacity.

For the data exploration and preparation part, refer to
[Enron+POI+Classifier+EDA.html](Enron POI Classifier EDA.pdf) and for the model building and tuning part, refer to [Enron+POI+Classifier+Model+Building.html](Enron POI Classifier Model Building.pdf).

One remark regarding featured that depend on POI: If we start with a fresh
dataset, then we cannot use these features, since they leak knowledge about
the labels. Here, I nonetheless use them, partly because they were used in the
course, and partly because I think they could be useful in an iterative
approach, where one tries to find POI in several rounds.

Lets move on to the answers to the questions:

## Question 1:

We were given financial data about enron officers and employees as well as
a large set of emails. These data were made public in court proceedings while
a range of enron officers were tried for fraud and other crimes. This case
was one of the largest corporate fraud cases in history.

Our job was to analyze the data and build a model that allows us to predict
whether a given person is a person of interest (POI) or not. Person of interests
are those persons, that were either convicted or indicted or otherwise involved
in the criminal proceedings.

In the financial data was an obvious outlier that corresponded not to a person
but instead to the TOTAL row in the data table. This outlier was discarded as it
clearly is an artifact. Another data point refered to a travel agency. It was
removed as well.

Checking the totals revealed two further data points with misaligned data.
I corrected these values by referring to the provided insider payment pdf file.

There were 145 data points divided in the two classes POI with 18 and non-POI
with 127 data points respectively.

The data comprised 21 features of whose one was the label 'poi'.

There were quite some missing values. I replaced them in general with 0, because
this was the most probable value (e.g. missing bonus value is most probably no
bonus).

I explored each feature using summary stats and histograms and I also listed any
outliers (more than 1.5 IQR off the median). Manual inspection of the outliers
led me to conclude that they were probably correct data.

## Question 2

Apart from the label 'poi', I used the following features:

- exercised_stock_options
- fraction_to_poi
- other
- shared_receipt_with_poi
- expenses

I selected these features by calculating the average importances of all
features using a 1000x StratifiedShuffleSplit for cross validation. I sorted
the features in descending importance order and chose the top 5 features.

In case of the second model that I looked at, namely logistic regression
with l1 penalty (Lasso), I used the LogisticRegressionCV class to perform
cross validation. From the resulting model I listed the features in descending
absolute coefficient value order and chose the top 9 features. (I also had to
use standardized features in this case.)

The feature 'fraction_to_poi' was newly created and it measures what fraction
of emails sent by a given person was sent to a poi. The assumption is, that
maybe poi were kind of a group within the company and therefore had a higher fraction_to_poi than non-poi.

The importances of the five chosen features are:

feature                   | importance   | cumulative
------------------------  | ------------ | ----------
exercised_stock_options   | 0.198        | 0.198
fraction_to_poi           | 0.149        | 0.348
other                     | 0.124        | 0.471
shared_receipt_with_poi   | 0.111        | 0.583
expenses                  | 0.107        | 0.690


## Question 3

I ended up using a simple decision tree model. It has the best performance
(regarding precision and recall) and it uses less features than the logistic
regression.

Best performance metrics from using tester.py were:

model                |  F1     | precision    |  recall  
---------------      | ------- | ------------ | --------
decision tree        |  0.51   |   0.61       |    0.44  
logistic regression  |  0.16   |   0.41       |    0.10

We cannot use accuracy since the two classes are highly unbalanced.

## Question 4

Most algorithms have various parameters. By tuning these parameters an
algorithm can be tailored to the given data set and thus provide much better performance. I used the GridSearchCV class of sklearn to search for best
parameter settings. I was careful to use F1 as scoring criteria (since the
default is the useless accuracy) and used stratified shuffled cross validation.

## Question 5

Validation is essential to prevent overfitting. If we use all our data to
train a model, we are likely to overfit the model. Thus, it performs excellent
on the training data, but performs much worse on new, unseen data. One way to
prevent this is to split of a test set which is not used for training the
model. When the model is trained, we use the test set to validate its
performance.

If we have not much data, then it is not possible to split of a large part of
it for testing purposes, because then not enough data remains for successful
training of the model. In such cases, one can use cross-validation, where
repeatedly split of one part of the data for training, validate with the rest
and do this over and over again. Then we average the validation performance
to get the final model performance. There are a variety of methods for
performing cross validation: e.g. Leave One Out, K-Fold Cross Validation.
In this project, I used stratified, shuffled K-Fold Cross Validation.

## Question 6

As mentioned before, the simple metric of accuracy does not work here, because
we have highly unbalanced classes. Thus we use precision and recall and the
combination of these two metrics known as F1 score.

Precision measures what part of positive results are really POI.

Recall measures what part of all POI we find with the model.

The average precision for the final model is 0.61

The average recall for the final model is 0.44

If our model says a person is a POI, then the chance that it really is a POI is 61%.

If we check a lot of persons using our model, we will get 44% of all POI.
