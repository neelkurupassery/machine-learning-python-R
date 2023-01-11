#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install stockfish
pip install lichess
pip install python-lichess
pip install python-chess


# In[3]:


import os
import json
from stockfish import Stockfish
import stockfish
import lichess.format 
import lichess.api
from lichess.format import PYCHESS
from lichess.format import PGN
import chess
import chess.svg


# In[4]:


pathSf = "C:/Users/neelk/Desktop/Python/stockfish_15_win_x64_avx2"
os.listdir(pathSf)


# In[38]:


pathSf = "C:/Users/neelk/Desktop/Python/stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe"
stockfish = Stockfish(pathSf)


# In[10]:


stockfish.get_top_moves()


# In[32]:


stockfish.set_fen_position("r3kb1r/1b1q1ppp/p1nppn2/P1p5/Qp2P3/2PP1NP1/1P1N1PBP/R1B2RK1 b kq - 3 11")
                           
x = stockfish.get_top_moves()
if x[1]['Centipawn'] - x[2]['Centipawn'] > 500: 
    print("One good move in this position")


# In[51]:


LICHESS_CLIENT_ID="lichess-oauth-flask"
SECRET_KEY= #retrieve from file

game = lichess.api.game('TBFISNd2')
#print(game.end().board())
print(game)


# In[120]:


from lichess.format import PYCHESS
game2 = lichess.api.game('TBFISNd2', format=PYCHESS)
board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
#for move in game2.mainline_moves():
#    board.push(move)
#    chess.svg.board(board, coordinates=False, size=350)
print(game2.mainline_moves())
print(game2.end().board())

chess.svg.board(game2.board(), coordinates=False, size=200)


# In[9]:




#fen1 = "8/8/8/8/4N3/8/8/8 w - - 0 1"
#board=chess.Board(fen1)

#chess.svg.board(board, coordinates=False, size=350)


# In[128]:


print(game2.mainline_moves())
stockfish.set_position(game2.mainline_moves())
#stockfish.set_fen_position("r3kb1r/1b1q1ppp/p1nppn2/P1p5/Qp2P3/2PP1NP1/1P1N1PBP/R1B2RK1 b kq - 3 11")
stockfish.get_top_moves()


# In[136]:


import requests
response = requests.get('https://lichess.org/api/puzzle/daily')
print(response.json())
#https://lichess.org/api/puzzle/activity


# In[139]:


response = requests.get('https://lichess.org/training/Rapport-Jobava_System')
print(response.text())


# In[ ]:


import pandas as pd 
for chunk in pd.read_csv("C:/Users/neelk/Desktop/Chess/lichess_db_puzzle.csv", chunksize=1): 
    print(chunk)


# In[214]:


import dask.dataframe as dd
filename = "C:/Users/neelk/Desktop/Chess/lichess_db_puzzle.csv"
df = dd.read_csv(filename, dtype='str')
List = ['PuzzleId','FEN','Moves','Rating','RatingDeviation','Popularity','NbPlays','Themes','GameUrl']
df.columns = List
data = df.Themes.head(2)[0].split()
data2 = df.Themes.head(1000)
print(data2)


#df = df.rename(columns=List)
#num = -1
#for c in df.columns:
#    num+=1
#    print(List[num])
    
               
    
    #'PuzzleId,FEN,Moves,Rating,RatingDeviation,Popularity,NbPlays,Themes,GameUrl')


# In[179]:


def search_item(list, product):
    for i in range(len(list)):
        if list[i] == product:
            return True
    return False

search_item(data, 'short')


# In[207]:


df.PuzzleId.head(1)[0]
chess.svg.board(chess.Board(df.FEN.head(1)[0]), coordinates=False, size=200)


# In[191]:


search_item(data2[0].split(), 'short')


# In[226]:


n = 10
data2 = df.Themes.head(n)
for i in range(n):
    if search_item(data2[i].split(), 'short'): 
        print(df.FEN.head(n)[i])                  


# In[ ]:


#n = 240845
n = 10
data2 = df.Themes.head(n)
for i in range(n):
    if search_item(data2[i].split(), 'short'): 
        print(df.FEN.head(n)[i])
    if i == (n-1): 
        print("done")


# In[213]:





# In[239]:


df.PuzzleId.head(1)[0]
chess.svg.board(chess.Board(df.FEN.head(1)[0]), coordinates=False, size=200)

chess.Board(df.FEN.head(1)[0]).pieces(piece_type=chess.PAWN, color=chess.WHITE)


# In[241]:


chess.Board(df.FEN.head(1)[0]).pieces(piece_type=1, color=True)


# In[249]:


len([n for n in chess.Board(df.FEN.head(1)[0]).pieces(piece_type=1, color=True)])


# In[261]:


material=[0,0]
v=[1,3,3,5,9]
for a in range(5):
    material[0] += len([n for n in chess.Board(df.FEN.head(1)[0]).pieces(piece_type=(a+1), color=True)])*v[a]
    material[1] += len([n for n in chess.Board(df.FEN.head(1)[0]).pieces(piece_type=(a+1), color=False)])*v[a]
mdiff = material[1] - material[0]
print(mdiff)


# In[278]:


f = '5rk1/1p3ppp/pq3b2/8/8/1P1Q1N2/P4PPP/3R2K1 w - - 2 27'
stockfish.set_fen_position(f)
x = stockfish.get_evaluation()
v=[1,3,3,5,9]
p=['p','n','b','r','q']
mdiff=0
for a in range(5):
    mdiff += f.count(p[a])*v[a]
    mdiff -= f.count(p[a].capitalize())*v[a]
print([mdiff,x['value']])


# In[269]:


stockfish.get_fen_position()


# In[5]:


pip install requests


# In[14]:


import requests
res = requests.get('http://tablebase.lichess.ovh/standard?fen=5k2/4pP2/4K3/8/8/8/8/8_w_-_-_0_9')
res2 = requests.get('http://tablebase.lichess.ovh/standard?fen=5k2/4pP2/4K3/8/8/8/8/8_b_-_-_0_9')


# In[64]:


print(res.json()["category"])
print(res2.json()["category"])
#print(res.text)
#print(res2.text)


# In[2]:


chess.svg.board(chess.Board("4k3/6KP/8/8/8/8/7p/8_w_-_-_0_1".replace("_"," ")), coordinates=False, size=350)


# In[4]:


chess.svg.board(chess.Board("5k2/5P2/4K3/8/8/8/8/8_w_-_-_0_1".replace("_"," ")), coordinates=False, size=350)


# In[5]:


testPos1 = "5k2/3p1P2/4K3/8/8/8/8/8_b_-_-_0_1".replace("_"," ")
testPos2 = "3p1k2/5P2/4K3/8/8/8/8/8_b_-_-_0_1".replace("_"," ")
testPos3 = "5k2/5P2/4K3/8/8/8/8/8_w_-_-_0_9".replace("_"," ")
chess.svg.board(chess.Board(testPos3), coordinates=False, size=350)


# In[51]:


chess.Board(testPos2).is_valid()


# In[55]:


def allPoss(fen, piece):
  tail = fen.replace("1","a").replace("2","aa").replace("3","aaa").replace("4","aaaa").replace("5","aaaaa").replace("6","aaaaaa").replace("7","aaaaaaa").replace("8","aaaaaaaa")
  for x in range(len(tail)-1):
      tail2 = tail
      if tail[x]=="a": 
        tail2=tail[0:x]+piece+tail[(x+1):]
        tail3=tail2.replace("aaaaaaaa","8").replace("aaaaaaa","7").replace("aaaaaa","6").replace("aaaaa","5").replace("aaaa", "4").replace("aaa","3").replace("aa","2").replace("a","1")
        if chess.Board(tail3).is_valid(): 
            print(tail3)
        #print(tail2)
        
allPoss(testPos3,"p")    


# In[42]:


l = "task"
l[0:2]+l[2:]


# In[79]:


def interp(out1, out2):
    if (out1=="draw") & (out2=="draw"): 
        return("drawn")
    if (out1=="win") & (out2=="loss"):
        return("won(w)")
    if (out1=="loss") & (out2=="win"): 
        return("won(b)")
    if (out1=="loss") & (out2=="loss"): 
        return("mzug(f)")
    if (out1=="draw") & (out2=="loss"): 
        return("mzug(hw)")
    if (out1=="loss") & (out2=="draw"): 
        return("mzug(hb)")
    if (out1=="won") & (out2=="won"): 
        return("stmw")
    if (out1=="won") & (out2=="draw"): 
        return("btmd")
    if (out1=="draw") & (out2=="win"): 
        return("wtmd")


# In[80]:


def allPoss2(fen, piece):
  tail = fen.replace("1","a").replace("2","aa").replace("3","aaa").replace("4","aaaa").replace("5","aaaaa").replace("6","aaaaaa").replace("7","aaaaaaa").replace("8","aaaaaaaa")
  for x in range(len(tail)-1):
      tail2 = tail
      if tail[x]=="a": 
        tail2=tail[0:x]+piece+tail[(x+1):]
        tail3=tail2.replace("aaaaaaaa","8").replace("aaaaaaa","7").replace("aaaaaa","6").replace("aaaaa","5").replace("aaaa", "4").replace("aaa","3").replace("aa","2").replace("a","1")
        if chess.Board(tail3).is_valid() & chess.Board(tail3.replace("w","b")).is_valid(): 
            tail4 = requests.get("http://tablebase.lichess.ovh/standard?fen=" + tail3.replace(" ","_")).json()["category"]
            tail5 = requests.get("http://tablebase.lichess.ovh/standard?fen=" + tail3.replace("w","b").replace(" ","_")).json()["category"]
            tail6 = interp(tail4, tail5)
            print(tail3, " ", tail4, " ", tail5, " ", tail6)
            #print(tail3)


# In[6]:


chess.svg.board(chess.Board("5k2/5P2/4K3/p7/8/8/8/8 w - - 0 9"), coordinates=False, size=350)


# In[ ]:


requests.get('http://tablebase.lichess.ovh/standard?fen=4k3/6KP/8/8/8/8/7p/8_w_-_-_0_1').json()["category"]


# In[81]:


allPoss2(testPos3,"p")


# In[78]:


a = "draw"
b = "draw"
def test(aa,bb): 
    if (aa=="draw") & (bb=="draw"): 
        return("drawn")
test(a,b)


# In[82]:


allPoss2(testPos3,"n")


# In[83]:


allPoss2(testPos3,"b")


# In[85]:


allPoss2(testPos3,"r")


# In[86]:


allPoss2(testPos3,"q")


# In[90]:


def countPossInit(fen, piece,piece2):
  count=0
  tail = fen.replace("1","a").replace("2","aa").replace("3","aaa").replace("4","aaaa").replace("5","aaaaa").replace("6","aaaaaa").replace("7","aaaaaaa").replace("8","aaaaaaaa")
  for x in range(len(tail)-1):
      tail2 = tail
      if tail[x]=="a": 
        tail2=tail[0:x]+piece+tail[(x+1):]
        tail3=tail2.replace("aaaaaaaa","8").replace("aaaaaaa","7").replace("aaaaaa","6").replace("aaaaa","5").replace("aaaa", "4").replace("aaa","3").replace("aa","2").replace("a","1") 
        count += countPoss(tail3,piece2)   
  print(count)

def countPoss(fen, piece):
  count=0
  tail = fen.replace("1","a").replace("2","aa").replace("3","aaa").replace("4","aaaa").replace("5","aaaaa").replace("6","aaaaaa").replace("7","aaaaaaa").replace("8","aaaaaaaa")
  for x in range(len(tail)-1):
      tail2 = tail
      if tail[x]=="a": 
        tail2=tail[0:x]+piece+tail[(x+1):]
        tail3=tail2.replace("aaaaaaaa","8").replace("aaaaaaa","7").replace("aaaaaa","6").replace("aaaaa","5").replace("aaaa", "4").replace("aaa","3").replace("aa","2").replace("a","1")
        if chess.Board(tail3).is_valid(): 
            count += 1   
  return(count)
        
countPossInit("8/8/8/8/8/8/8/8 w - - 0 9","K","k")    


# In[92]:


def countPossInit3m(fen, piece,piece2,piece3):
  count=0
  tail = fen.replace("1","a").replace("2","aa").replace("3","aaa").replace("4","aaaa").replace("5","aaaaa").replace("6","aaaaaa").replace("7","aaaaaaa").replace("8","aaaaaaaa")
  for x in range(len(tail)-1):
      tail2 = tail
      if tail[x]=="a": 
        tail2=tail[0:x]+piece+tail[(x+1):]
        tail3=tail2.replace("aaaaaaaa","8").replace("aaaaaaa","7").replace("aaaaaa","6").replace("aaaaa","5").replace("aaaa", "4").replace("aaa","3").replace("aa","2").replace("a","1") 
        count += countPoss3m2(tail3,piece2,piece3)   
  print(count)

def countPoss3m2(fen, piece,piece2):
  count=0
  tail = fen.replace("1","a").replace("2","aa").replace("3","aaa").replace("4","aaaa").replace("5","aaaaa").replace("6","aaaaaa").replace("7","aaaaaaa").replace("8","aaaaaaaa")
  for x in range(len(tail)-1):
      tail2 = tail
      if tail[x]=="a": 
        tail2=tail[0:x]+piece+tail[(x+1):]
        tail3=tail2.replace("aaaaaaaa","8").replace("aaaaaaa","7").replace("aaaaaa","6").replace("aaaaa","5").replace("aaaa", "4").replace("aaa","3").replace("aa","2").replace("a","1")
        if chess.Board(tail3).is_valid(): 
            count += countPoss3m(tail3,piece2)  
  return(count)

def countPoss3m(fen, piece):
  count=0
  tail = fen.replace("1","a").replace("2","aa").replace("3","aaa").replace("4","aaaa").replace("5","aaaaa").replace("6","aaaaaa").replace("7","aaaaaaa").replace("8","aaaaaaaa")
  for x in range(len(tail)-1):
      tail2 = tail
      if tail[x]=="a": 
        tail2=tail[0:x]+piece+tail[(x+1):]
        tail3=tail2.replace("aaaaaaaa","8").replace("aaaaaaa","7").replace("aaaaaa","6").replace("aaaaa","5").replace("aaaa", "4").replace("aaa","3").replace("aa","2").replace("a","1")
        if chess.Board(tail3).is_valid(): 
            count += 1   
  return(count)
        
countPossInit3m("8/8/8/8/8/8/8/8 w - - 0 9","K","k","p")  


# In[ ]:


def countPossInit3m(fen, piece,piece2,piece3):
  count=0
  tail = fen.replace("1","a").replace("2","aa").replace("3","aaa").replace("4","aaaa").replace("5","aaaaa").replace("6","aaaaaa").replace("7","aaaaaaa").replace("8","aaaaaaaa")
  for x in range(len(tail)-1):
      tail2 = tail
      if tail[x]=="a": 
        tail2=tail[0:x]+piece+tail[(x+1):]
        tail3=tail2.replace("aaaaaaaa","8").replace("aaaaaaa","7").replace("aaaaaa","6").replace("aaaaa","5").replace("aaaa", "4").replace("aaa","3").replace("aa","2").replace("a","1") 
        count += countPoss3m2(tail3,piece2,piece3)   
  print(count)

def countPoss3m2(fen, piece,piece2):
  count=0
  tail = fen.replace("1","a").replace("2","aa").replace("3","aaa").replace("4","aaaa").replace("5","aaaaa").replace("6","aaaaaa").replace("7","aaaaaaa").replace("8","aaaaaaaa")
  for x in range(len(tail)-1):
      tail2 = tail
      if tail[x]=="a": 
        tail2=tail[0:x]+piece+tail[(x+1):]
        tail3=tail2.replace("aaaaaaaa","8").replace("aaaaaaa","7").replace("aaaaaa","6").replace("aaaaa","5").replace("aaaa", "4").replace("aaa","3").replace("aa","2").replace("a","1")
        if chess.Board(tail3).is_valid(): 
            count += countPoss3m(tail3,piece2)  
  return(count)

def countPoss3m(fen, piece):
  count=0
  tail = fen.replace("1","a").replace("2","aa").replace("3","aaa").replace("4","aaaa").replace("5","aaaaa").replace("6","aaaaaa").replace("7","aaaaaaa").replace("8","aaaaaaaa")
  for x in range(len(tail)-1):
      tail2 = tail
      if tail[x]=="a": 
        tail2=tail[0:x]+piece+tail[(x+1):]
        tail3=tail2.replace("aaaaaaaa","8").replace("aaaaaaa","7").replace("aaaaaa","6").replace("aaaaa","5").replace("aaaa", "4").replace("aaa","3").replace("aa","2").replace("a","1")
        if chess.Board(tail3).is_valid(): 
            count += 1   
  return(count)
        
countPossInit3m("8/8/8/8/8/8/8/8 w - - 0 9","K","k","p")  


# In[95]:


def countPossInit4m(fen, piece,piece2,piece3,piece4):
  count=0
  tail = fen.replace("1","a").replace("2","aa").replace("3","aaa").replace("4","aaaa").replace("5","aaaaa").replace("6","aaaaaa").replace("7","aaaaaaa").replace("8","aaaaaaaa")
  for x in range(len(tail)-1):
      tail2 = tail
      if tail[x]=="a": 
        tail2=tail[0:x]+piece+tail[(x+1):]
        tail3=tail2.replace("aaaaaaaa","8").replace("aaaaaaa","7").replace("aaaaaa","6").replace("aaaaa","5").replace("aaaa", "4").replace("aaa","3").replace("aa","2").replace("a","1") 
        count += countPoss4m2(tail3,piece2,piece3,piece4)   
  print(count)

def countPoss4m2(fen, piece,piece2,piece3):
  count=0
  tail = fen.replace("1","a").replace("2","aa").replace("3","aaa").replace("4","aaaa").replace("5","aaaaa").replace("6","aaaaaa").replace("7","aaaaaaa").replace("8","aaaaaaaa")
  for x in range(len(tail)-1):
      tail2 = tail
      if tail[x]=="a": 
        tail2=tail[0:x]+piece+tail[(x+1):]
        tail3=tail2.replace("aaaaaaaa","8").replace("aaaaaaa","7").replace("aaaaaa","6").replace("aaaaa","5").replace("aaaa", "4").replace("aaa","3").replace("aa","2").replace("a","1")
        if chess.Board(tail3).is_valid(): 
            count += countPoss4m3(tail3,piece2,piece3)  
  return(count)

def countPoss4m3(fen, piece,piece2):
  count=0
  tail = fen.replace("1","a").replace("2","aa").replace("3","aaa").replace("4","aaaa").replace("5","aaaaa").replace("6","aaaaaa").replace("7","aaaaaaa").replace("8","aaaaaaaa")
  for x in range(len(tail)-1):
      tail2 = tail
      if tail[x]=="a": 
        tail2=tail[0:x]+piece+tail[(x+1):]
        tail3=tail2.replace("aaaaaaaa","8").replace("aaaaaaa","7").replace("aaaaaa","6").replace("aaaaa","5").replace("aaaa", "4").replace("aaa","3").replace("aa","2").replace("a","1")
        if chess.Board(tail3).is_valid(): 
            count += countPoss4m(tail3,piece2)  
  return(count)

def countPoss4m(fen, piece):
  count=0
  tail = fen.replace("1","a").replace("2","aa").replace("3","aaa").replace("4","aaaa").replace("5","aaaaa").replace("6","aaaaaa").replace("7","aaaaaaa").replace("8","aaaaaaaa")
  for x in range(len(tail)-1):
      tail2 = tail
      if tail[x]=="a": 
        tail2=tail[0:x]+piece+tail[(x+1):]
        tail3=tail2.replace("aaaaaaaa","8").replace("aaaaaaa","7").replace("aaaaaa","6").replace("aaaaa","5").replace("aaaa", "4").replace("aaa","3").replace("aa","2").replace("a","1")
        if chess.Board(tail3).is_valid(): 
            count += 1   
  return(count)
        
countPossInit4m("8/8/8/8/8/8/8/8 w - - 0 9","K","k","p","P")  


# In[ ]:




