import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform

# 한글 폰트 설정 (운영체제에 따라 다름)
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')  # 윈도우용
elif platform.system() == 'Darwin':  # macOS
    plt.rc('font', family='AppleGothic')
else:  # Linux
    plt.rc('font', family='NanumGothic')  # 설치되어 있어야 함

# 마이너스 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# 데이터 정의
years = [
    2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
    2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
]
amounts = [
    149160, 186124, 196079, 212029, 236872, 259479, 263884, 296527, 328294,
    320945, 325697, 337696, 372139, 368225, 370778, 383168, 396897, 450534,
    487180, 487202, 492997
]

# 그래프 생성
plt.figure(figsize=(12, 6))
plt.plot(years, amounts, marker='o', linestyle='-', color='blue', linewidth=2)

# 그래프 설정
plt.title('연도별 1인당 국민연금 수령액 변화', fontsize=16)
plt.xlabel('연도', fontsize=12)
plt.ylabel('1인당 연금 수령액 (원)', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# 그래프 표시
plt.show()
plt.savefig('pension_graphsyr.png')
