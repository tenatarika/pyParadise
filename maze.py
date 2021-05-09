# -*- coding: utf-8 -*-
"""
Created on Sat May  8 20:19:41 2021

@author: Furcas
"""



from random import  randint
from PIL import Image, ImageDraw
from random import shuffle, randrange
 
def make_maze(w = 16, h = 8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
 
    def walk(x, y):
        vis[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)
 
    walk(randrange(w), randrange(h))
 
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s
 
if __name__ == '__main__':
    print(make_maze()) 
 
def board(num, size):
    new_color = (255, 255, 255)
    new_image = Image.new("RGB", (num * size, num * size), new_color)
    x = size * num
    y = x
    draw = ImageDraw.Draw(new_image)
    for i in range(0, x, size):
        if i % (size * 2) == 0:
            for j in range(0, y, size):
                if j % (size * 2) == 0:
                    draw.rectangle(
                        [i, j, i + size - 1, j + size - 1], fill='black')
        else:
            for j in range(size, y, size):
                if j % (size * 2) != 0:
                    draw.rectangle(
                        [i, j, i + size - 1, j + size - 1], fill='black')
    new_image.save('res.png', "PNG")

def make_matrix(n, m):
    matrix = []
    for _ in range(n):
        temp_arr = []
        for i in range(m):
            temp_arr.append(1)
        matrix.append(temp_arr)
        
    return matrix
stack = [] 
def generate_labirint(matrix, i, j):
    
    
    if i != 0 and j != 0 and (i, j) not in stack:
        rw = randint()
        if rw == 0:
            matrix[i+1][j]=0
            stack.append((i, j))
            return generate_labirint(matrix, i+1, j)
        else:
            matrix[i][j+1]=0
            stack.append((i, j))
            return generate_labirint(matrix, i, j+1)
    elif (i,j) in stack and j != len(matrix[1]):
        return generate_labirint(matrix, i, j+1)
    elif (i,j) in stack and j == len(matrix[1]):
       return generate_labirint(matrix, i+1, 1)
        
        
        
    else:
        return matrix
            
def genMaze(matrix ):
    matrix[1][1] = 0    
    for i in range(1,len(matrix)-2):
        for j in range(1,len(matrix[1])-2):
            if (i+1, j) not in stack and (i, j+1) not in stack and i!=1  and j !=len(matrix[1])-2  and i!= len(matrix)-2:
                stack.append((i,j))
                
                rw = randint(0,1)
                if rw == 0:
                    
                    matrix[i][j+1]=0
                    stack.append((i, j+1))
                    
                     
                if rw == 1:
                    
                    matrix[i-1][j]=0
                    stack.append((i-1, j))
            
            '''
                if (i-1, j) in stack and i==1 and (i,j+1) not in stack:
                    
                    matrix[i][j+1]=8
                    stack.append((i, j+1))
                
                elif (i,j) == (len(matrix)-1,len(matrix[1])-1):
                    continue
                elif (i-1, j) in stack  and (i,j+1) not in stack :
                    
                    matrix[i][j+1]=8                 
                    stack.append((i, j+1))
                    
                elif (i, j+1) in stack and (i-1,j) not in stack and i!=1:
                    matrix[i-1][j]=0
                    
                    stack.append((i-1, j))
                   
                elif (i, j+1) not in stack and (i-1, j) not in stack:
                    rw = randint(0,1)
                    if rw == 0:
                        
                        matrix[i][j+1]=0
                        stack.append((i, j+1))
                        
                         
                    if rw == 1:
                        
                        matrix[i-1][j]=0
                        stack.append((i-1, j))
                        
            '''
                
                
                
                
                
    return matrix 
                
    """
    y_up = cell[0]+1
    y_down = cell[0]-1
    
    x_right = cell[0][1]+1
    x_left = cell[0][1]-1
    """
        
       
        
     
        
if __name__ == '__main__':
    #board(8, 50)
    m1 = genMaze(make_matrix(7, 7))
    print(m1)
    print(stack)
    print(make_maze())