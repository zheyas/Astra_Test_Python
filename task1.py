def process_grades(records: list[str]) -> dict:
    valid_count = 0
    total_grade = 0
    passed = []
    skipped = 0

    for record in records:
        try:
            # Проверяем наличие двоеточия
            if ':' not in record:
                skipped += 1
                continue

            # Разделяем по двоеточию
            parts = record.split(':')

            # Должно быть ровно 2 части (фамилия и оценка)
            if len(parts) != 2:
                skipped += 1
                continue

            surname = parts[0].strip()
            grade_str = parts[1].strip()

            # Проверяем, что фамилия не пустая
            if not surname:
                skipped += 1
                continue

            # Пытаемся преобразовать оценку в целое число
            grade = int(grade_str)

            # Проверяем диапазон оценки (0-100)
            if grade < 0 or grade > 100:
                skipped += 1
                continue

            # Успешно распарсили
            valid_count += 1
            total_grade += grade

            if grade >= 60:
                passed.append(surname)

        except (ValueError, AttributeError):
            # Строка битая (оценка не число, или другие ошибки)
            skipped += 1
            continue

    # Вычисляем среднее
    if valid_count == 0:
        average = 0.0
        passed = []
    else:
        average = round(total_grade / valid_count, 1)
        passed.sort()  # Сортируем по алфавиту

    return {
        "valid_count": valid_count,
        "average": average,
        "passed": passed,
        "skipped": skipped
    }


if __name__ == "__main__":
    data1 = [
        "Иванов: 85",
        "Петров: 42",
        "Сидоров: abc",
        "Козлов: 90",
        ": 55",
        "Иванов: 70"
    ]
    print("Тест 1:", process_grades(data1))

    data2 = [
        "А: 0",
        "Б: 59",
        "В: 60",
        "Г: 100",
        "Д: 101",
        "Е: -5",
    ]
    print("Тест 2:", process_grades(data2))

    data3 = []
    print("Тест 3:", process_grades(data3))

    data4 = ["abc", "no colon", ": 50", ""]
    print("Тест 4:", process_grades(data4))

    data5 = ["А: 60", "Б: 70", "В: 80"]
    print("Тест 5:", process_grades(data5))

    data6 = ["А: 0", "Б: 30", "В: 59"]
    print("Тест 6:", process_grades(data6))