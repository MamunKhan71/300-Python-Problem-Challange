# Problem 105
# Write A Python Program To Get Temperature In Fahrenheit, To Convert Into Centigrade And Kelvin

temperF = float(input("Temp(f): "))
centigrade = (5/9 * (temperF-32))
kelvin = ((temperF + 459.67) * 5/9)
print(f"Centigrade : {centigrade}\nKelvin: {kelvin}")