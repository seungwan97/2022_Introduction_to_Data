first_p=int(input("최초 계약시 연봉:"))
grow=int(input("연봉인상률:"))


tra=120
eat=120
notax=eat+tra #비과세항목
bonus=800

#올해 총 세전
print(first_p+bonus)
#올해 총 세후
print(((first_p-notax)*0.85)+240+(bonus*0.85))
#매달 기본급(세전)
print((first_p+bonus)/12)
#매달 기본급(세후)
print((((first_p-notax)*0.85)+240+(bonus*0.85)/12))

#인상 후 세전 총 금액
next_p=(first_p*(grow/100+1))
print((first_p*(grow/100+1)))
#인상 후 세후 총 금액
print(((next_p-notax)*0.85)+240+(bonus*0.85))
#매달 기본급(세전)
print((next_p+bonus)/12)
#매달 기본급(세후)
print((((next_p-notax)*0.85)+240+(bonus*0.85)/12))
