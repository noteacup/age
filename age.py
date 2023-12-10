driving = input('你有開過車嗎?')
if driving != '有' and driving != '沒有':
    print('只能輸入 有/沒有')
    raise SystemExit

age = input('請問你的年齡是?')
age = int(age)
if driving == '有':
    if age >= 18:
        print('通過檢測!')
    else:
        print('需要做個調查歐')
