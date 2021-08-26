import math
import pyvoronoi

pv = pyvoronoi.Pyvoronoi(100)
pv.AddSegment([[0.1,0.8],[0.3,0.6]])
pv.AddSegment([[0.3,0.6],[0.4,0.6]])
pv.AddSegment([[0.4,0.6],[0.4,0.5]])
pv.AddSegment([[0.4,0.6],[0.4,0.7]])
pv.AddSegment([[0.4,0.7],[0.5,0.8]])
pv.AddSegment([[0.4,0.7],[0.5,0.6]])
pv.AddSegment([[0.5,0.6],[0.7,0.7]])

pv.Construct()
edges = pv.GetEdges()
vertices = pv.GetVertices()
cells = pv.GetCells()

for cIndex in range(len(cells)):
        cell = cells[cIndex]
        if cell.is_open == False:
                for i in range(len(cell.edges)):
                        e = edges[cell.edges[i]]
                        startVertex = vertices[e.start]
                        endVertex = vertices[e.end]

                        max_distance  = math.dist([startVertex.X, startVertex.Y], [endVertex.X, endVertex.Y]) / 10
                        if startVertex != -1 and endVertex != -1:
                                if(e.is_linear == True):
                                        array = [[startVertex.X, startVertex.Y],[endVertex.X, endVertex.Y]]
                                else:
                                        points = pv.DiscretizeCurvedEdge(cell.edges[i], max_distance)
                                        for p in points:
                                                print ("{0},{1}".format(p[0], p[1]))