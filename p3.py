temp = float(input("Enter temperature (°C): "))

if temp < 20:
    status = "Cold"
elif temp <= 30:
    status = "Normal"
else:
    status = "Hot"

print(f"Temperature: {temp}°C")
print(f"Status: {status}")
