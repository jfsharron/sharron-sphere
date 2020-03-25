""" test_rational.py """

from rational import Rational

num = input("Please enter numerator: ")
den = input("Please enter the denominator: ")

num2 = input("Please enter numerator: ")
den2 = input("Please enter the denominator: ")

r1 = Rational(int(num), int(den))
r2 = Rational(int(num2), int(den2))
print(r1)
print(r2)

#r3 = Rational(r1 + r2)
print(r1 + r2)


