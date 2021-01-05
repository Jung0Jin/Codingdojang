# https://codingdojang.com/scode/645?answer_mode=hide

import datetime as dt

cur_time = dt.datetime.today()  # 현재시간
leave_time = cur_time.replace(hour=17, minute=30, second=0)  # 퇴근시간
# 남은 시간 계산 (퇴근 시간이 지난 경우 익일 퇴근까지의 시간)
diffsec = (leave_time - cur_time).total_seconds()
diffsec = diffsec + 60 * 60 * 24 if diffsec < 0 else diffsec

print(f"다음 퇴근시간까지는 {dt.timedelta(seconds=diffsec)}({diffsec:,.0f}초) 남았습니다.")
