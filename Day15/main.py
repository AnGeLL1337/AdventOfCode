import heapq

fileObj = open("15.in", "r") 
lines = fileObj.read().splitlines() 
fileObj.close()

risk = [list(map(int, line)) for line in lines]

paths = [(0, 0, 0)]

help_list = [[0] * len(row) for row in risk]

while True:
    rf, x, y = heapq.heappop(paths)
    if help_list[x][y]: continue
    if (x, y) == (len(risk) - 1, len(risk[x]) - 1):
        print(rf)
        exit(0)
    help_list[x][y] = 1
    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if not len(risk) > nx >= 0 <= ny < len(risk[0]): continue
        if help_list[nx][ny]: continue
        heapq.heappush(paths, (rf + risk[nx][ny], nx, ny))