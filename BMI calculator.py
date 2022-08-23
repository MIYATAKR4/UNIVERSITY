height = float(input('Insert your height:'))
gender = input('Insert your gender:')

if gender == 'male':
    print('your ideal weight is:', (float((72.7 * height) - 58)))
if gender == 'female':
    print('your ideal weight is:', (float((62.1 * height) - 44.7)))

