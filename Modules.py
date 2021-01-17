from math import fsum , ceil

print(fsum([1,2,3,4,5,6]))
print(ceil(2.8))

from math import fsum as Sexy_Sum #as를 붙여주면 자신이 원하는 이름으로 설정가능

print(Sexy_Sum([1,2,3,4,5,6]))

from Calculater import plus,minus #Calculater에서 plus와 minus 함수를 받아와 사용

print(plus(2,3),minus(3,5))