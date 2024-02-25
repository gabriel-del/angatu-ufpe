import arff
import numpy as np
import pandas as pd

for row in  arff.load('TermografiaMama_frontais.arff'):
  print(row)
