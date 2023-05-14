Matrix = [[1 for j in range(5)] for j in range(5)]
set_neighbors = [[(-1,-1),(-1,0),(-1,1)]
                ,[(0,-1),(0,0),(0,1)]
                ,[(1,-1),(1,0),(1,1)]]

for x in range(len(Matrix)):
    for y in range(len(Matrix[x])):
        print(x,y, Matrix[x][y])
        neighbors = [[None for j in range(3)] for j in range(3)]

        for i in range(len(neighbors)):
            for j in range(len(neighbors[i])):
                #print("=====================Neighbors Editting Starts Here==========================")
                ## Any elements has 9 neighbors inckuding itself. We are looping through all neighbors for every element.
                cord_one = x+set_neighbors[i][j][0]
                cord_two = y+set_neighbors[i][j][1]

                if cord_one >= 0 and cord_one < len(Matrix) and cord_two >=0 and cord_two < len(Matrix[x]):
                    neighbors[i][j] = Matrix[x+set_neighbors[i][j][0]][y+set_neighbors[i][j][1]]
                #print(i,j,neighbors[i][j])
                #print("======================Neighbors Editting Ends Here===========================")
        print(neighbors)
