pi = 22 / 7
radian = float(input('Radius of cylinder: '))
volume = pi * radian * radian * height
sur_area = 2 * pi * radian * height + pi * radian ** 2 * 2
print('Volume is: ', volume)
print('Surface Area is: ', sur_area)