# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

# We now have training data in the X_train and Y_train for preparing models,
# and a X_validation and Y_validation sets that we can use later.
#
# Notice that we used a python slice to select the columns in the NumPy array
# X = matrix with all rows/observations, and all columns EXCEPT the last column = the class of the observation.
# y = matrix with all rows/observations, and ONLY column 4 = the class of the observation.
# X_train = matrix with training data. Shape: (120, 4)
# y_train = matrix with training data. Shape: (120,)
# X_validation = matrix for validation. Shape: (30, 4)
# Y_validation = matrix for validation. Shape: (30, )