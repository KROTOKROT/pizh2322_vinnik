# Lambda-Функции

## Задание 1

Напишите два вызова функции say_to_all(), Чтобы:
- При первом вызове для каждого имени из списка people напечатано Привет, "имя"! (итого шесть строчек вывода).
- При втором вызове для каждого имени из списка people было напечатано До завтра, "имя"! (Ещё шесть строчек вывода).

Решите задачу, используя лямбда-функцию.

```PYTHON
people = ["Антон", "Соня", "Коля"]

say_to_all = lambda greeting: [
    print(f"{greeting}, {name}!") for name in people]

say_to_all("Привет")
say_to_all("До завтра")
```

