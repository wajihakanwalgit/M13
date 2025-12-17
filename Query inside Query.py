from google.colab import files
uplaoded = files.upload()


import pandas as pd
import numpy as np

import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT *
                    FROM sqlite_master
                    WHERE type='table';""", conn)
tables


team = pd.read_sql("""SELECT * FROM Team""", conn)

team

season = pd.read_sql("""SELECT * FROM Season""", conn)

season


csk_matche_2015 = pd.read_sql("""SELECT Match_Id, Team_2 as Away_Team, Toss_Winner, Match_Winner
                            FROM Match
                            WHERE Team_1 =
                            (SELECT Team_1
                            FROM Match
                            WHERE Team_1 == 3 AND Season_Id == 8)""", conn)

print("Matche Played By Chennai Super Kings in Year 2015")
csk_matche_2015

csk_win = pd.read_sql("""SELECT *
                          FROM Match
                          WHERE Match_Winner == 3 AND Season_Id == 8""", conn)
print("Matche won by CSK as Home Team in Year 2015")
csk_win


match_run = pd.read_sql("""SELECT Match_Id, Runs_Scored as Total_Runs, Innings_No
                            FROM Batsman_Scored
                            WHERE Total_Runs > 5 AND Match_Id IN
                            (SELECT Match_Id
                            FROM Match
                            WHERE Season_Id == 8)""", conn)

print("Matche with Scored Run GreaterThan 5 in Year 2015")
match_run


avg_run = pd.read_sql("""SELECT Match_Id, Runs_Scored as Total_Runs, Innings_No
                            FROM Batsman_Scored
                            WHERE Innings_No == 1 AND Runs_Scored >
                            (SELECT AVG(Runs_Scored)
                            FROM Batsman_Scored)""", conn)

print("Matches with Scor Run GreaterThan Average Scored Run")
avg_run

