import arff
import numpy as np
import pandas as pd

array = []
for row in  arff.load('TermografiaMama_frontais.arff'):
  array.append(row)

print(array[:1])
