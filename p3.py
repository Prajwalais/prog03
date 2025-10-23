temp = float(input("Enter temperature (°C): "))

if temp < 20:
    status = "Cold"
elif temp <= 30:
    status = "Normal"
else:
    status = "Hot"

print(f"Temperature: {temp}°C")
print(f"Status: {status}")




temperature_c = float(input("Enter temperature in °C: "))

if temperature_c < 20:
    status = "Cold"
elif 20 <= temperature_c <= 30:
    status = "Normal"
else:
    status = "Hot"


temperature_f = (temperature_c * 9/5) + 32


print(f"Temperature: {temperature_c}°C")
print(f"Status: {status}")
print(f"Temperature in Fahrenheit: {temperature_f}°F")
