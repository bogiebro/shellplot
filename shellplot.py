import visdom
import sys
import numpy as np

vis = visdom.Visdom(env=sys.argv[1])
y = np.array(list(map(np.float, sys.stdin.readline().split())))
xmin = 1
x = np.arange(xmin, xmin + len(y))
win = vis.line(X=x, Y=y, opts={'markers': True, 'title': sys.argv[2]})
for ystr in sys.stdin:
  xmin += len(y)
  y = np.array(list(map(np.float, ystr.split())))
  x = np.arange(xmin, xmin + len(y))
  vis.line(win=win, X=x, Y=y, update='append')


