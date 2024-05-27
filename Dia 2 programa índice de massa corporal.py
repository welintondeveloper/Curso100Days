# meu código
# 1st input: enter height in meters e.g: 1.65
height = input("qual sua altura\n")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("qual seu peso\n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
ConverterAltura = float(height)
ConverterPeso = int(weight)
Indice = int(ConverterPeso/(ConverterAltura*ConverterAltura))
print(f"seu peso ideal é {Indice}")

# código do curso
height = input()
weight = input()
# Your code below this line 👇
weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
# bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)