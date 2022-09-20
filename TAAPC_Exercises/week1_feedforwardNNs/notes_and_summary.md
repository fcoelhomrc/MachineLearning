# Week 1, Feed-forward Neural Networks

I have tried to tackle a dataset of 32 x 32 images containing 10 different categories, using the following network:

```python
model = keras.models.Sequential()
model.add(keras.layers.Dense(128, activation="relu", input_shape=(3*width*height, )))
model.add(keras.layers.Dropout(0.1))
model.add(keras.layers.Dense(256, activation="relu"))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(256, activation="relu"))
model.add(keras.layers.Dropout(0.1))
model.add(keras.layers.Dense(128, activation="relu"))
model.add(keras.layers.Dense(10, activation="softmax"))
```

Dropout layers serve as a form of regularization.

The optimizer used as SGD, and the idea was to train for 80 epochs with a learning rate of 0.01, and after that train for 20 more but with a smaller rate of 0.001

The result is interesting because it clearly shows overfitting in the training set. See how the accuracy keeps decreasing for the train set, while it remains stuck in a plateau for the validation set. 

![](.\example_overfitting.png)

Indeed, the accuracy for the test set is only around 0.50