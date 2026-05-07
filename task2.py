def longest_increasing_streak(nums: list[int]) -> dict:
    if len(nums) < 2:
        return {
            "length": 0,
            "streak": []
        }

    n = len(nums)

    # prefix[i] — длина возрастающей серии, заканчивающейся в nums[i]
    prefix = [1] * n

    best_length = 0
    best_end = -1

    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            prefix[i] = prefix[i - 1] + 1
        else:
            prefix[i] = 1

        # Обновляем только если строго больше,
        # чтобы при равных длинах оставить первую найденную серию
        if prefix[i] > best_length:
            best_length = prefix[i]
            best_end = i

    # Если максимальная серия длины 1,
    # значит нормальной возрастающей серии не найдено
    if best_length < 2:
        return {
            "length": 0,
            "streak": []
        }

    start = best_end - best_length + 1
    streak = nums[start:best_end + 1]

    return {
        "length": best_length,
        "streak": streak
    }

nums = [1, 0, 0, 3, 4 ,6, 5, 8, 4, 7]

result = longest_increasing_streak(nums)

print(result)