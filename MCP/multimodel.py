"""
simple multimodel ai agent

->weather(city)
->calculator(a,b)
->currency_converter(amount,rate)

"""

import re

#accesss the numbers and city name in the i/p

#weather
def weather(city):
    weather_data={
        "hyderabad":{"condition":"cloudy","temp":30},
        "bangalore":{"condition":"overcast","temp":20},
        "chennai":{"condition":"humidity","temp":35},
        "mumbai":{"condition":"clear","temp":24},
        "delhi":{"condition":"sunny","temp":39},
        "kerela":{"condition":"rainy","temp":27},
        "New york":{"condition":"snowy","temp":20},
    }
    key=city.strip().lower()
    if key in weather_data:
        data=weather_data[key]
        return f"weather in {city.title()}:{data['condition']},{data['temp']}c"
    return f"weather not found for:'{city}'."
def calculator(a,b):
    result={
        "sum":a+b,
        "sub":a-b,
        "mul":a*b,
        "div":a/b,
    }
    return result

def currency_converter(amount,rate):
    converted=amount*rate
    return round(converted,2)

def handle_req(user_input):
    text=user_input.lower()

    if "weather" in text:
        match=re.search(r"weather (?:in|for|at)\s*([a=zA-Z\s]+)",text)
        if match:
            city=match.group(1).strip()
        else:
            city="your city"
        return weather(city)
    
    if any(word in text for word in["calculator","add","sub","mul","div"]):
        numbers=re.findall(r"[-+]?\d*\.?\d+",text)
        if len(numbers)>=2:
            a,b=int(numbers[0]),int(numbers[1])
            return calculator(a,b)
        return "provide correctly e.g calculate 10 and 40"
    
    if "convert" in text or "exchange" in text:
        numbers=re.findall(r"[-+]?\d*\.?\d+",text)
        if len(numbers)>=2:
            amount,rate=float(numbers[0],float(numbers[1]))
            return currency_converter(amount,rate)
        return "provide eg convert 100 at rate 95.5"
    if __name__=="__main__":
        sample_req=[
            "What is the weather in mumbai?",
            "calculate 25 and 69",
            "convert 100 at rate 95.5"
            ]
        for req in sample_req:
            print(f"request:{req}")
            print(f"response:{handle_req[req]}")
            while True:
                user_input=input("ask something or exit:")
                if user_input.lower()=="exit":
                    break
                print(handle_req(user_input))








