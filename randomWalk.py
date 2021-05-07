from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

import os
os.environ["BOKEH_LOG_LEVEL"] = "trace"
os.environ["BOKEH_PY_LOG_LEVEL"] = "trace"

from bokeh.plotting import figure, show
from bokeh.palettes import Dark2_5 as palette
import itertools
COLORS = itertools.cycle(palette)

def visual_results(steps):
    graph = figure(title="randomWalk")
    for s in steps:
        graph.line(steps[s]["y"],steps[s]["x"],legend_label=f"borracho - {s}", color=next(COLORS))
        graph.line(steps[s]["y_a"],steps[s]["x_a"],legend_label=f"borracho Anormal - {s}", color=next(COLORS))
    show(graph)

def sim_walk(step, reps, typeDrunk):
    drunkGuy = typeDrunk("Pablo")
    drunkANormalGuy = typeDrunk("Luis")
    origin = Coordenada(0,0)
    res = 0
    dists=[None for i in range(reps)]
    coords={"x":(), "y":(), "x_a":(), "y_a":()}
    for i in range(reps):
        coords_x, coords_y = [0 for i in range(step)],[0 for i in range(step)]
        coords_x_a, coords_y_a = [0 for i in range(step)],[0 for i in range(step)]
        camp = Campo()
        camp.add_drunk(drunkGuy, origin)
        camp.add_drunk(drunkANormalGuy, origin)
        for s in range(step):
            camp.move_drunk(drunkGuy)
            coords_x[s], coords_y[s]=camp.other_coord(drunkGuy).x,camp.other_coord(drunkGuy).y
            camp.move_funDrunk(drunkANormalGuy)
            coords_x_a[s], coords_y_a[s]=camp.other_coord(drunkANormalGuy).x,camp.other_coord(drunkANormalGuy).y
        dists[i] = origin.dist(camp.other_coord(drunkGuy))
        res += dists[i]
        # Solo dame la ultima simulacion
        coords["x"]= tuple(coords_x)
        coords["y"]= tuple(coords_y)
        coords["x_a"]= tuple(coords_x_a)
        coords["y_a"]= tuple(coords_y_a)
    return res/reps, coords

def main(steps, reps, typeDrunk):
    coords_steps={s : {} for s in steps}
    for step in steps:
        res, coords = sim_walk(step,reps,typeDrunk)
        coords_steps[step]=coords
        print(f"Para step = {step}, se obtiene una dist prom  = {res}")
    visual_results(coords_steps)

if __name__ == "__main__":
    steps = [500, 1000, 1500]
    reps = 100
    main(steps, reps, BorrachoTradicional)