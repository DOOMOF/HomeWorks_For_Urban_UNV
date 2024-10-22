def champ(team1_num, team2_num, score_1, score_2, team1_time, team2_time, tasks_total, time_avg, challenge_result):
    print('В команде Мастера кода участников: %s' % team1_num)
    print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
    print('Команда Волшебники данных решили задач: {}!'.format(score_2))
    print('Волшебники данных решили задач за {}'.format(team1_time))
    print(f'Команды решили {score_1} и {score_2} задач')
    print(f'результат битвы: {challenge_result}')
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')


champ(5
,6
,40
,42
,1552.512
,2153.31451
,82
,45.2
,challenge_result = 'Победа команды Волшебники данных!')
