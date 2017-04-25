import numpy as np
import pandas
from sklearn.neighbors import KNeighborsClassifier
my_data = pandas.read_csv("https://ibm.box.com/shared/static/u8orgfc65zmoo3i0gpt9l27un4o0cuvn.csv", delimiter=",")
print( my_data )
