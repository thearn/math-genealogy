from tempfile import gettempdir
from pydot import graph_from_dot_file
from networkx import drawing, nx_agraph, compose,MultiDiGraph#,nx_pydot,to_networkx_graph
from subprocess import call

TMP = gettempdir() +'/'

def generate_dot(mathid):
    print("gathering data for MathID: {}".format(mathid))
    fn = TMP+'{}.dot'.format(mathid)
    call(['ggrapher','-f',fn,'-a',mathid])  # Geneagrapher

def make_graph(mathid,outfmt='pdf'):
    gc = graph_from_dot_file(TMP+'{}.dot'.format(mathid))
    gc.set_overlap(0)

    if 'png' in outfmt:
        gc.write_png('{}.png'.format(mathid), prog='dot')

    if 'pdf' in outfmt:
        gc.write_pdf('{}.pdf'.format(mathid), prog='dot') #fdp, dot,


def combine_dots(dotlist,mathid):
    g1=drawing.nx_agraph.read_dot(TMP+dotlist[-1])
    g = MultiDiGraph()
    for d in dotlist:
        g2=drawing.nx_agraph.read_dot(TMP + d)
        g1=compose(g1,g2)
    g.add_nodes_from(g1.nodes(data=True))
    g.add_edges_from(g1.edges(data=True))
    g.to_directed()
    g = nx_agraph.to_agraph(g)
    g.write(TMP+'-'.join(mathid)+'.dot')

def graph_genealogy(math_id,outformat='pdf'):
    try:
        make_graph(math_id,outformat)
    except Exception: #file wasn't found or is corrupt
        generate_dot(math_id)
        make_graph(math_id,outformat)

def graph_combined_genealogy(mathid,outfmt='pdf'):
    for i in mathid:
        graph_genealogy(i,outfmt)
#%% combined plot if more than one mathid specified
    if len(mathid)>1:
        names = [i+".dot" for i in mathid]
        combine_dots(names,mathid)
        make_graph('-'.join(mathid),outfmt)

if __name__ == "__main__":
    from argparse import ArgumentParser
    p = ArgumentParser(description='easy interface to Math Genealogy Project Plotter')
    p.add_argument('mathid',help='Math ID of person(s)',type=str,nargs='+')
    p.add_argument('-o','--output',help='output format [pdf png]',default=['pdf'],nargs='+')
    p = p.parse_args()

    graph_combined_genealogy(p.mathid,p.output)
