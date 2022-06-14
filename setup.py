from models.game import Game
import pygame
import sqlite3

from models.player import Player 

class Setup(object):
    def __init__(self, *args):
        self.init_database()
    
    def start_game(self):
        pass
    
    def init_database(self):
        try:
            sqliteConnection = sqlite3.connect('./data/data.db')
            cursor = sqliteConnection.cursor()
            self.cursor = cursor

        except sqlite3.Error as error:
            print("Erreur lors de l'ouverture de la base de donnée : ", error)
        finally:
            if sqliteConnection:
                # sqliteConnection.close()
                print("La connexion SQLite et fermée")
    
    def launch_game(self) : 
        game = Game(self.get_players_info())
        game.start()
       
    
    def get_players_info(self) : 
        players = []
        sqlite_select_query = """SELECT * from player LIMIT 2"""
        self.cursor.execute(sqlite_select_query)
        records = self.cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            players.append(row)

        # self.cursor.close()
        return players
    



setup = Setup()
setup.launch_game()