def heating_cooling(actual_temp, desired_temp):
    if int(actual_temp) > 10 > int(desired_temp):
        print("Run A/C")
    elif int(actual_temp) < 25 < int(desired_temp):
        print("Run heat")
    else:
        print("Standby")
actual_temp = input("Please enter the current temperature:")
desired_temp = input("Please enter the desired temperature:")
heating_cooling(actual_temp,desired_temp)
def convert_temp(temp_celsius, target_unit):
    if target_unit == "K":
        temp_celsius = int(actual_temp) + 273.15
        print(f"The temperature is {temp_celsius} degrees {target_unit}")
    elif target_unit == "F":
        temp_celsius = 1.8 * int(actual_temp) +32
        print(f"The temperature is {temp_celsius} degrees {target_unit}")
    else:
        temp_celsius = actual_temp
        print(f"The temperature is {temp_celsius} degrees {target_unit}")
target_unit = input("Please enter temperature unit to convert to:")
temp_celsius = actual_temp
convert_temp(temp_celsius, target_unit)




