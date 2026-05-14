#Convert distant given in feet and inches into meter and centimeter.

feet = float(input('Enter the feet value:'))
inches = float(input('Enter the inches value:'))

total_inches = (feet * 12) + inches


centimeter = total_inches * 2.54
meter = centimeter / 100

print (f'The distance is {meter} meters and {centimeter} centimeters.')