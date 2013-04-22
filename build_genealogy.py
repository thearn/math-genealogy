from pydot import graph_from_dot_file
from networkx import drawing, nx_agraph, compose,MultiDiGraph,nx_pydot,to_networkx_graph
import os,shutil
import unicodedata

def generate_dot(person):
    print "gathering data for:",person[0]
    fn=person[0]+'.dot'
    if not os.path.exists(fn) and not os.path.exists('dots/'+fn):
        os.system('ggrapher -f "'+fn+'" -a '+str(person[1]))
        shutil.move(fn,'dots/'+fn)

def make_graph(dotfile):
    gc = graph_from_dot_file('dots/'+dotfile+'.dot')
    gc.write_pdf('graphs/'+dotfile+'.pdf')
    gc.write_png('graphs/'+dotfile+'.png')

def sanitize_string(name):
    name= unicodedata.normalize('NFKD', name).encode('ascii','ignore')
    name = ', '.join(name.split(' \\n'))
    return name
    
def combine_dots(dotlist):
    g1=drawing.nx_agraph.read_dot('dots/'+dotlist[-1])
    g = MultiDiGraph()
    for i in xrange(len(dotlist)):
        g2=drawing.nx_agraph.read_dot('dots/'+dotlist[i])
        g1=compose(g1,g2)
    g.add_nodes_from(g1.nodes(data=True))
    g.add_edges_from(g1.edges(data=True))
    g.to_directed()
    g = nx_agraph.to_agraph(g)
    g.write('dots/combined.dot')

def graph_genealogy(name,math_id):
    generate_dot([name,math_id])
    make_graph(name)
    
def graph_combined_genealogy(name_id_pairs):
    for name, math_id in name_id_pairs:
        generate_dot([name,math_id])
        make_graph(name)
    names = [name+".dot" for name, math_id in name_id_pairs]
    combine_dots(names)
    make_graph("combined")

if __name__ == "__main__":
    #single person graph:
    graph_genealogy("Tristan A. Hearn",162833)
    
    #multiple person graph:
    graph_combined_genealogy([["Tristan A. Hearn", 162833],
                              ["Terry Tao", 43967],
                              ["David Alber", 110487]])

    
