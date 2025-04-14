import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
from math import sqrt

# print([f.name for f in matplotlib.font_manager.fontManager.ttflist])
font_location = '/.virtualenvs/neo/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/NanumBarunGothic.ttf'
font_name = font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

