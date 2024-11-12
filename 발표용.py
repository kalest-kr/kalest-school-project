MOL = 6.02 * (10 ** 23)


print("계산을 시작합니다")
print("질량, 입자 수, 기체의 부피중 한개를 골라주세요")
x = input()


# 본격적인 분류
if x == '질량':
    print("질량을 선택하셨습니다. 몰을 구할지 질량을 구할지 정해주세요")
    y = input()
    if y == '몰':
        print("질량값과 몰 질량을 입력해주세요.")
        print("질량값을 입력해주세요.")
        mass = input()
        print("몰 질량값을 입력해주세요.")
        mol_mass = input()
        print(int(mass) / int(mol_mass), 'mol')
    if y == '질량':
        print("물질의 양과 몰의 질량값을 정해주세요.")
        print("물질의 양을 정해주세요")
        quantity = input()
        print("몰 질량값을 입력해주세요.")
        mol_mass = input()
        print(int(quantity) * int(mol_mass), 'mol')
if x == '입자 수':
    print("입자수를 선택하셨습니다. 몰을 구할지 입자 수를 구할지 정해주세요")
    y = input()
    if y == '몰':
        print("입자 수를 정해주세요")
        num = input()
        print(float(num) * MOL)
    if y == '입자 수':
        print("물질의 양을 정해주세요.")
        quantity = input()
        print(float(quantity) * MOL)
if x == '기체의 부피':
    print("기체의 부피를 선택하셨습니다. 몰을 구할지 기체의 부피를 구할지 정해주세요.")
    y = input()
    if y == '몰':
        print('부피를 정해주세요')
        t = input()
        print(22.4 * float(t))
    if y == '기체의 부피':
        print("물질의 양을 구해주세요")
        quantity = input()
        print(22.4 * float(quantity))
