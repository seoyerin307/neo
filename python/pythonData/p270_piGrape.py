import pandas as pd
import metplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

slice = [1, 2, 3, 4]
hobbies = ['잠자기', '외식', '여행', '운동']
mycolors = ['blue', '#6AFF00', 'green', '#ff003c']

plt.pie(x=slice, labels=hobbies, colors=mycolors, shadow=mycolors, ecplode=[0, 0.1, 0, 0],
    autopct='%1.2f%%', startangle=90, counterclockwise=False)

plt.legend(loc=4)

filename = 'p270_poGrape01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
plt.show()