math-genealogy
=====================
A python script to collect data from the mathematics genealogy project and
generate genealogy graphs, combine graphs, etc.

## Usage:

    python build_genealogy <mathID>
    
    
## One-time Setup:

    pip install -r requirements.txt
    
Due to Geneagrapher 0.2.1, requires Python 2.


--------------------------------------------------------------
## Script Usage:
Method `graph_genealogy(name, mathid)` from `build_genealogy.py` builds a math genealogy graph for a single individual.
Input arguments are the indiviudal's name (as a string), and their Mathematics Genealogy Project id number (available at
the end of the url for their page).

### Script Example:
```python
graph_genealogy(162833) #name, mathid
```
This generates:
![Graph](http://i.imgur.com/G9UtDYv.jpg)
as well as a pdf version.

Method `graph_combined_genealogy(name_mathid_pairs)` from `build_genealogy.py` builds a math genealogy graph for a list
of individuals, then generates their combined genealogy graph.
Input argument is a list of indiviudal's name-id number pairs.

Example:
```python
graph_combined_genealogy([162833, 43967, 110487])
```
This generates:
![Graph](http://i.imgur.com/zelQDx9.jpg)
as well as a pdf version.

##TODO:
- Clean up some of the dependancies (there may be some redundancy)
- Methods that will graph just the minimum path between groups individuals, by finding their most recent common grand-advisor
