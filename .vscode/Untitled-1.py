import numpy as np
import pandas as pd
import statsmodels as sm
from scipy import stats
import warnings
warnings.filterwarnings('ignore')
mean = 5
std = 1.5
grade = 7
z_score = (grade-mean)/std #z-оценка результата Васи
z_score
import numpy as np
norm_rv = stats.norm(loc=5, scale=1.5) # генерируем нормальное распределение
rate1 = norm_rv.cdf(grade)*100 # процент студентов написавших хуже Васи
rate1