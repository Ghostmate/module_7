team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
name1 = "Мастера кода"
name2 = "Волшебники данных"
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

def result():
    name = str()
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        name = name1
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        name = name2
    else:
        return 'Ничья!'
    return f"Результат битвы: победа команды {name}!"

print('В команде %(name)s участников: %(num)s ! ' % {'name':name1,'num':team1_num})
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))
print("Команда {name} решила задач: {score} !".format(name=name2,score=score_2))
print("{name} решили задачи за {time} с !".format(name = name2,time = team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(result())
print(f"Сегодня было решено {score_1 + score_2} задач, в среднем по {(team1_time+team2_time)/(score_1+score_2)} секунды на задачу!.")