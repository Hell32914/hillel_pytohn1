def format_time(seconds):
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)
    
    if days % 10 == 1 and days != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and not (12 <= days <= 14):
        day_word = "дні"
    else:
        day_word = "днів"
    
    return f"{days} {day_word}, {hours_str}:{minutes_str}:{seconds_str}"

user_input = int(input("Введіть кількість секунд (0 - 8639999): "))

formatted_time = format_time(user_input)
print(formatted_time)