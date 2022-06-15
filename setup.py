from unittest import result
from models.game import Game
import pygame
import sqlite3
import pygame_menu

from models.player import Player 

class Score() :
    def __init__(self, id, value, pseudo) :
        self.value = value
        self.pseudo = pseudo
        self.id = id
        
    def __str__(self):
        return str(self.pseudo) + "  :  " + str(self.value)  


class Setup(object):
    def __init__(self, *args):
        self.init_database()
        self.best_scores = []
    
    def start_game(self):
        pass
    
    def init_database(self):
        try:
            self.sqliteConnection = sqlite3.connect('./data/data.db')
            cursor = self.sqliteConnection.cursor()
            self.cursor = cursor

        except sqlite3.Error as error:
            print("Erreur lors de l'ouverture de la base de donnée : ", error)
        finally:
            if self.sqliteConnection:
                # sqliteConnection.close()
                print("La connexion SQLite et fermée")
    
    def launch_game(self) : 
        self.game = Game(self)
        self.game.running()
        
       
   
        
        
        
    def get_players_info(self) : 
        players = []
        sqlite_select_query = """SELECT * from player LIMIT 2"""
        self.cursor.execute(sqlite_select_query)
        result = self.cursor.fetchall()
        print("Total rows are:  ", len(result))
        print("Printing each row")
        for row in result:
            players.append(row)

        # self.cursor.close()
        return players
    
    def store_score(self, score, pseudo) : 
        sqlite_insert_query = """INSERT INTO score (pseudo, score_value) VALUES (?, ?);"""
        self.cursor.execute(sqlite_insert_query, (pseudo, round(score, 1)))
        self.sqliteConnection.commit()
        
    def get_best_score(self) :  
        scores = []
        sqlite_select_query = """SELECT * from score ORDER BY score_value DESC LIMIT 5;"""
        self.cursor.execute(sqlite_select_query)
        result = self.cursor.fetchall()
        for row in result : 
            scores.append(Score(*row))
            
        self.best_scores = scores
            


setup = Setup()
setup.launch_game()