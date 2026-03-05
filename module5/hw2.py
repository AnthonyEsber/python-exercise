def number_stats(numbers:list[int]) -> tuple[int, int, float, int] | str:

    if len(numbers) == 0:
        return "Empty list!"

    smallest_number:int = min(numbers)
    largest_number:int = max(numbers)
    average_number:float = sum(numbers) / len(numbers)
    odd_count:int = 0 
    for num in numbers:
        if num % 2: odd_count += 1
    
    return smallest_number, largest_number, average_number, odd_count

result = number_stats([1, 2, 3, 9, 0])

print(result)

result = number_stats([])

print(result)