import yaml
import mysql.connector

from mysql_connect import parrams


class MySQL():

    def __init__(self, params):
        self.params = params

    def input_games(self):
        """Создаёт поделючение к базе данных и вносит данные из файла games.yaml"""
        with open('games.yaml') as file:
            games = yaml.load(file)
        with mysql.connector.connect(**self.params) as conn:
            with conn.cursor() as curs:
                for game in games['games']:
                        curs.execute('INSERT INTO games VALUES (NULL, {}, "{}", "{}");'.format(
                            game['id'], game['name'], game['date'])
                        )
                conn.commit()

                curs.execute('select {} from games;'.format('*'))
                data = curs.fetchall()
                print(data)


syberry = MySQL(parrams)
syberry.input_games()