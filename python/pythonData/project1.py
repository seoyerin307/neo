import pandas as pd
import matplotlib.pyplot as plt

# 1. CSV 파일 경로 (두 번째 업로드된 파일)
file_path = '가구주_연령별_가구당_월평균_가계수지__전국_1인이상__20250414191217.csv'

# 2. 파일 읽기 (첫 2줄을 헤더로 사용)
df = pd.read_csv(file_path, header=None)

# 3. 첫 두 줄을 병합하여 컬럼명 만들기
new_columns = df.iloc[0].fillna(method='ffill') + "|" + df.iloc[1]
df.columns = ['가구주연령', '가계수지항목'] + new_columns[2:].tolist()

# 4. 데이터만 추출
df = df.iloc[2:].reset_index(drop=True)

# 5. Long 형식으로 변환
id_vars = ['가구주연령', '가계수지항목']
value_vars = df.columns[2:]
df_long = pd.melt(df, id_vars=id_vars, value_vars=value_vars,
                  var_name='연도_가구', value_name='값')

# 6. 연도 추출
df_long['연도'] = df_long['연도_가구'].str.extract(r'(\d{4})')

# 7. 숫자형으로 변환
df_long['값'] = pd.to_numeric(df_long['값'], errors='coerce')

# 8. 연도별 항목별 합계 계산
df_yearly = df_long.groupby(['연도', '가구주연령', '가계수지항목'], as_index=False)['값'].sum()

# 9. 컬럼명 정리
df_yearly.columns = ['연도', '연령대', '항목', '연간합계']

# 10. 한글 폰트 설정 (환경에 따라 수정 가능)
plt.rcParams['font.family'] = 'NanumBarunGothic'
plt.rcParams['axes.unicode_minus'] = False

# 11. '가계지출' 항목만 필터링
target = df_yearly[df_yearly['항목'] == '가계지출']

# 12. 시각화
plt.figure(figsize=(10, 6))
for name, group in target.groupby('연령대'):
    plt.plot(group['연도'], group['연간합계'], marker='o', label=name)

plt.title('연도별 가계지출 추이 (가구주 연령대별)')
plt.xlabel('연도')
plt.ylabel('연간 가계지출')
plt.legend(title='연령대')
plt.grid(True)
plt.tight_layout()

# 13. 파일로 저장
filename = '가계지출_연령대별_연도별.png'
plt.savefig(filename, dpi=300)
print(f'그래프가 "{filename}" 파일로 저장되었습니다.')

# 14. 그래프 출력
plt.show()