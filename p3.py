temp = float(input("Enter temperature (°C): "))

if temp < 20:
    status = "Cold"
elif temp <= 30:
    status = "Normal"
else:
    status = "Hot"

print(f"Temperature: {temp}°C")
print(f"Status: {status}")


# temperature_alert.py

# Step 1: Accept temperature input
temperature_c = float(input("Enter temperature in °C: "))

# Step 2: Determine the temperature status
if temperature_c < 20:
    status = "Cold"
elif 20 <= temperature_c <= 30:
    status = "Normal"
else:
    status = "Hot"

# Step 3: Convert to Fahrenheit
temperature_f = (temperature_c * 9/5) + 32

# Step 4: Display results
print(f"Temperature: {temperature_c}°C")
print(f"Status: {status}")
print(f"Temperature in Fahrenheit: {temperature_f}°F")
