import math

ang = float(input('Digite o ângulo: '))
sin = math.sin(math.radians(ang))
print('O seno do ângulo {:.1f} é {:.2f}'.format(ang, sin))
cos = math.cos(math.radians(ang))
print('O cosseno do ângulo {:.1f} é {:.2f}'.format(ang, cos))
tang = math.tan(math.radians(ang))
print('A tangente do ângulo {:.1f} é {:.2f}'.format(ang, tang))
