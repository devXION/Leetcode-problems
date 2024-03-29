def is_power_of_two(number: int) -> bool:
    while number != 1:
        if number % 2:
            return False
        number /= 2
    return True
    
