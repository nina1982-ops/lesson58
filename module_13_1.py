import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    for i in range(1, 6):  # Поднимаем 5 шаров
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональная силе
        print(f'Силач {name} поднял {i} шар')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    # Параметры для 3 силачей
    strongmen = [
        ("Pasha", 3),
        ("Denis", 4),
        ("Apollon", 5)
    ]

    # Создаем задачи для каждого силача
    tasks = [start_strongman(name, power) for name, power in strongmen]

    # Ждем выполнение всех задач
    await asyncio.gather(*tasks)


# Запуск турнира
if __name__ == '__main__':
    asyncio.run(start_tournament())



