#  Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  
#  Licensed under the Apache License, Version 2.0 (the "License").
#  You may not use this file except in compliance with the License.
#  A copy of the License is located at
#  
#      http://www.apache.org/licenses/LICENSE-2.0
#  
#  or in the "license" file accompanying this file. This file is distributed 
#  on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
#  express or implied. See the License for the specific language governing 
#  permissions and limitations under the License.

from __future__ import print_function

import argparse
import os
import pandas as pd

from sklearn import tree
from sklearn.externals import joblib


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Hyperparameters are described here. In this simple example we are just including one hyperparameter.
    parser.add_argument('--max_leaf_nodes', type=int, default=-1)

    ##TODO: READ IN OTHER HYPERPARAMETERS
    ##add --criterion with default 'gini'
    ##add --splitter with default 'random'
    parser.add_argument('--criterion', type=str, default='gini')
    parser.add_argument('--splitter', type=str, default='random')
    ##END TODO

    # Sagemaker specific arguments. Defaults are set in the environment variables.
    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])
    parser.add_argument('--test', type=str, default=os.environ['SM_CHANNEL_TEST'])
    

    args = parser.parse_args()
    
    print('done reading arguments')

    # Take the set of files and read them all into a single pandas dataframe
    input_files = [ os.path.join(args.train, file) for file in os.listdir(args.train) ]
    if len(input_files) == 0:
        raise ValueError(('There are no files in {}.\n' +
                          'This usually indicates that the channel ({}) was incorrectly specified,\n' +
                          'the data specification in S3 was incorrectly specified or the role specified\n' +
                          'does not have permission to access the data.').format(args.train, "train"))
    
    print("reading train data from " + ' '.join(input_files))
    raw_data = [ pd.read_csv(file, header=None, engine="python") for file in input_files ]
    train_data = pd.concat(raw_data)
    
    # Take the set of files and read them all into a single pandas dataframe
    input_files = [ os.path.join(args.test, file) for file in os.listdir(args.test) ]
    if len(input_files) == 0:
        raise ValueError(('There are no files in {}.\n' +
                          'This usually indicates that the channel ({}) was incorrectly specified,\n' +
                          'the data specification in S3 was incorrectly specified or the role specified\n' +
                          'does not have permission to access the data.').format(args.train, "train"))
    
    print("reading test data from " + ' '.join(input_files))
    raw_data_test = [ pd.read_csv(file, header=None, engine="python") for file in input_files ]
    test_data = pd.concat(raw_data_test)
    
    print("data read, first 5 rows:")
    print(train_data.head())

    print("pulling out label in first parameter in data")
    # labels are in the first column
    train_y = train_data.iloc[:,0]
    
    print("training dimensions are the other parameters in the data")
    train_X = train_data.iloc[:,1:]
    
    test_y = test_data.iloc[:,0]
    test_X = test_data.iloc[:,1:]

    # Here we support a single hyperparameter, 'max_leaf_nodes'. Note that you can add as many
    # as your training my require in the ArgumentParser above.
    max_leaf_nodes = args.max_leaf_nodes
    
    ##TODO: set parameters from new hyper parameter args
    criterion = args.criterion
    splitter = args.splitter
    #END TODO
    
    # Now use scikit-learn's decision tree classifier to train the model.
    clf = tree.DecisionTreeClassifier(max_leaf_nodes=max_leaf_nodes, criterion=criterion, splitter=splitter)
    
    clf = clf.fit(train_X, train_y)
    
    print('score:' + str(clf.score(test_X, test_y)))
    
    # Print the coefficients of the trained classifier, and save the coefficients
    joblib.dump(clf, os.path.join(args.model_dir, "model.joblib"))


def model_fn(model_dir):
    """Deserialized and return fitted model
    
    Note that this should have the same name as the serialized model in the main method
    """
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf
