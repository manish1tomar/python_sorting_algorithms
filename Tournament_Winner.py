# Space Complexity = O[K], Time Complexity = O[N]
def tournamentWinner(competitions, results):
    dict = {}
    for i,j in enumerate(competitions):
        if results[i] == 0:
            if competitions[i][1] not in dict.keys():
                dict[competitions[i][1]] = 3
            else:
                dict[competitions[i][1]] += 3
        else:
            if competitions[i][0] not in dict.keys():
                dict[competitions[i][0]] = 3
            else:
                dict[competitions[i][0]] += 3
    return max(dict, key=dict.get)
