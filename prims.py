

def prims(source ,graph):
    current_index = source
    weights = []
    visited = []
    for node,weight in graph(source):
        weights.append([node,weight])
        
    visited.append(source)
    if not  visited:
        mini = min(weights,(weight))
        


