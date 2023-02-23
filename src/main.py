from pyamaze import maze, agent
m = maze(30, 40)
m.CreateMaze()
a = agent(m, filled=True, footprints=True)
m.tracePath({a:m.path})
m.run()
