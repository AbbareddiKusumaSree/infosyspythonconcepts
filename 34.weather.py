#Write a function with the name get weather_report that takes the temperature as an argument. If the temperature is less than 22, it should return "Cold". -If the temperature is greater than or equal to 22 and less than 35, it should return "Warm". - If the temperature is greater than or equal to 35, it should return "Hot".
def get_weather_report(temperature):
    if temperature < 22:
        return "Cold"
    elif 22 <= temperature < 35:
        return "Warm"
    else:  
        return "Hot"
print(get_weather_report(18))  
print(get_weather_report(28))  
print(get_weather_report(37))  