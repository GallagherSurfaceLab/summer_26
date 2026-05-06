"""This code analyzes STM images using voronoi diagrams and graphs
to quantify various properties of the image.

It builds off of the orginal code by Lucas V. Besteiro, lvbesteiro@protonmail.com
which was used in Refs. [1,2] and can be found at [3]. Additional information about its 
output and methodology, as well as references to previous related work, can be found 
either in Ref. [1] or in the supplementary information of Ref. [2].

The modified code here vectorized and simplified the voronoi diagram and simplified
some of the plotting. The new code is signifcantly faster and take up less memory.

The original segmentation and labelling of an STM image was also removed as this was a
difficult process to automate and was better done in steps.

1. G. Galeotti, F. De Marchi, T. Taerum, L.V. Besteiro, M. El Garah, J. Lipton-Duffin, 
   M. Ebrahimi, D.F. Perepichka, F. Rosei. Surface-mediated assembly, polymerization and
   degradation of thiophene-based monomers. Chem. Sci. 10 (19), 5167-5175 (2019).
   https://doi.org/10.1039/C8SC05267K

2. G. Galeotti, F. De Marchi, E. Hamzehpoor, O. MacLean, M. Rajeswara Rao, Y. Chen, 
   L.V. Besteiro, D. Dettmann, L. Ferrari, F. Frezza,P.M. Sheverdyaeva, R. Liu, 
   A.K. Kundu, P. Moras, M. Ebrahimi, M.C. Gallagher, F. Rosei, D.F. Perepichka & 
   G. Contini. Synthesis of mesoscale ordered two-dimensional π-conjugated polymers with 
   semiconducting properties. Nat. Mater. (2020). https://doi.org/10.1038/s41563-020-0682-z

3. https://github.com/lvbesteiro/STM-Minimum_Spanning_Tree/tree/master


modified code by Kyle Murphy, murphy.kyle.r@gmail.com
"""


#
# STM-Minimum_Spanning_Tree
# This Python script analyzes the degree of order in two-dimensional (2D) polymers from STM experimental images.
#
# It was used in the preparation of Refs. [1,2]. Additional information about its output and methodology, as well
# as references to previous related work, can be found either in Ref. [1] or in the supplementary information of Ref. [2].
# Both documents can be freely downloaded from the publishers' websites indicated below.
#
# If you use this code to analyze your data, please consider citing Refs. [1,2].
#
# 1. G. Galeotti, F. De Marchi, T. Taerum, L.V. Besteiro, M. El Garah, J. Lipton-Duffin, M. Ebrahimi, D.F. Perepichka, F. Rosei.
#    Surface-mediated assembly, polymerization and degradation of thiophene-based monomers. Chem. Sci. 10 (19), 5167-5175 (2019).
#    https://doi.org/10.1039/C8SC05267K
#
# 2. G. Galeotti, F. De Marchi, E. Hamzehpoor, O. MacLean, M. Rajeswara Rao, Y. Chen, L.V. Besteiro, D. Dettmann, L. Ferrari, F. Frezza,
#    P.M. Sheverdyaeva, R. Liu, A.K. Kundu, P. Moras, M. Ebrahimi, M.C. Gallagher, F. Rosei, D.F. Perepichka & G. Contini.
#    Synthesis of mesoscale ordered two-dimensional π-conjugated polymers with semiconducting properties. Nat. Mater. (2020).
#    https://doi.org/10.1038/s41563-020-0682-z
#
# Written by Lucas V. Besteiro, lvbesteiro@protonmail.com.
# Shared under GPL 3.0 license
#

# Modified 2026-04-02 by K. Murphy
# - Add docstrings and comments
# - Update function calls as needed
# - Vectorize Voronoi algorithm
# - Add nearest neighbour to Voronoi (cKDTree)
    

import numpy as np
from skimage import io, filters, morphology
from skimage.util import img_as_float, img_as_ubyte

from skimage import exposure, draw
from scipy.spatial import cKDTree
from scipy.ndimage import binary_dilation

import networkx as nx

# Reads image files and scale information. Expected name format: "TEXTscale_XXX.extension"
class img_file:
  """
  Represents an STM image with embedded scale metadata.

  Expected filename format:
      <anything>scale_<value>.<ext>

  Example: 
      sample_scale_500.png

  Attributes
  ----------
  name : str
      Filename
  nm_size : float
      Physical image size in nanometers (from filename)
  px_sizex : int
      Image width in pixels
  px_sizey : int
      Image height in pixels
  scale : float
      Pixel-to-nanometer ratio (px/nm)
  area : float
      Physical area of the image (nm²)
  """
  def __init__(self,name):
    """Parse filename and extract physical size."""
    self.name = name
    try:
        self.nm_size = float(name.split('scale_')[1].split('.')[0])
    except:
        self.nm_size = None
  def load(self):
    """
    Load image and compute spatial scaling.

    Returns
    -------
    img : ndarray
        Image as float array
    """
    self.img = img_as_float(io.imread(self.name))
    self.px_sizex = self.img.shape[1]
    self.px_sizey = self.img.shape[0]
    if self.nm_size is None:
        self.area = 1
        self.scale = 1
        self.nm_size = 1
        self.physical = False
    else:
        self.area = self.nm_size**2 * self.px_sizey/self.px_sizex # px_sizex/px_sizex is 1. Corrected from px_sizex/px_sizex for area calculation
        #Changed from px_sizex/px_sizex to px_sizey/px_sizex for scale calculation
        self.scale = self.px_sizex/self.nm_size
        self.physical = True

# Converts image to grayscale, equalize and enhance contrast
def gray_process(img,dsize=25,cutoff=0.5,gain=10):
    """
    Convert image to enhanced grayscale.

    Steps:
        1. Convert RGB → grayscale
        2. Apply local histogram equalization
        3. Apply sigmoid contrast enhancement

    Parameters
    ----------
    img : ndarray
        Input RGB image
    dsize : int
        Structuring element size for local equalization
    cutoff : float
        Sigmoid midpoint
    gain : float
        Sigmoid steepness

    Returns
    -------
    img_gr : ndarray
        Processed grayscale image
    """
    img_gr = np.zeros_like(img[:,:,0])
    img_gr = (img[:,:,0]+img[:,:,1]+img[:,:,2])/3
    selem = morphology.disk(dsize)
    img_gr = img_as_ubyte(img_gr)
    img_gr = filters.rank.equalize(img_gr, footprint=selem) #change for update skiimage
    img_gr = img_as_float(img_gr)
    img_gr = exposure.adjust_sigmoid(img_gr,cutoff=cutoff,gain=gain)
    return img_gr

# Populates the network with nodes
def find_nodes(mask,N,px_a_th,scale):
    """
    Convert segmented regions into graph nodes.

    Filters out small/noisy regions.

    Parameters
    ----------
    mask : ndarray
        Labeled segmentation mask
    N : int
        Number of labels
    px_a_th : float
        Area threshold (pixels)
    scale : float
        Pixel-to-nm conversion

    Returns
    -------
    G : networkx.Graph
        Graph with nodes representing regions
    """
    G = nx.Graph()
    for ii in range (1,N+1):
        # Gets the points for each label
        region = np.column_stack(np.where(mask==ii))
        # Gets the region center of mass, in pixel coordinates
        pcoord = np.floor(sum(region)/len(region))
        area = len(region)
        # Keep all nodes without area filtering
        G.add_node(ii, pixel_pos=pcoord, area=area/scale**2)
    return G


def voronoi_tree(img, G, k=8):
    """
    Hybrid Voronoi (Power Diagram) using KDTree preselection.

    Strategy:
    - Use KDTree to find k nearest candidate nodes per pixel
    - Compute exact power distance only for those k nodes
    - Assign pixel to best candidate

    This gives:
        - Near-exact results
        - Much lower memory usage
        - Significant speedup

    Parameters
    ----------
    img : img_file
        Image object with metadata
    G : networkx.Graph
        Graph with node positions and areas
    k : int
        Number of nearest nodes to consider (default=8)

    Returns
    -------
    img_vor : voronoi diagram (random colors) ndarray
    img_vor_deg : voronoi diagram (cells colored by degree) ndarray
    img_vor_boarder : vornoi boarders (voronoi cell boarders in black) ndarray
    G : Graph (original graph)
    G_inner : Graph (cells boardering to image removed, graph edges calculated)
    """

    psx = img.px_sizex
    psy = img.px_sizey
    scale = img.scale

    # --- Extract node data ---
    nodelist = np.array(list(G.nodes()))
    coords = np.array([G.nodes[n]['pixel_pos'] for n in nodelist], dtype=np.float32)
    narea = np.array([G.nodes[n]['area'] * scale**2 for n in nodelist], dtype=np.float32)

    # --- Power diagram weights ---
    power = 0.3
    weights = np.power(narea, power).astype(np.float32)

    # --- Build KDTree ---
    tree = cKDTree(coords)

    # --- Pixel grid ---
    yy, xx = np.indices((psy, psx))
    pts = np.c_[yy.ravel(), xx.ravel()].astype(np.float32)

    # --- KDTree preselection ---
    _, nn = tree.query(pts, k=k)  # (num_pixels, k)

    # --- Gather candidate nodes ---
    cand_coords = coords[nn]       # (P, k, 2)
    cand_weights = weights[nn]     # (P, k)

    # --- Compute exact power distance ---
    diff = pts[:, None, :] - cand_coords
    dist2 = np.sum(diff**2, axis=2)

    power_dist = dist2 - cand_weights

    # --- Select best node ---
    best_local = np.argmin(power_dist, axis=1)
    idx = nn[np.arange(len(pts)), best_local]

    mask = nodelist[idx].reshape(psy, psx)

    # ==========================================================
    # AREA COMPUTATION
    # ==========================================================

    counts = np.bincount(idx, minlength=len(nodelist))
    S = counts / scale**2

    for i, node in enumerate(nodelist):
        G.nodes[node]['area_vor'] = S[i]

    # ==========================================================
    # REMOVE EDGE NODES
    # ==========================================================

    edge_labels = np.unique(
        np.concatenate([
            mask[0, :], mask[-1, :],
            mask[:, 0], mask[:, -1]
        ])
    )

    G_inner = G.copy()
    G_inner.remove_nodes_from(edge_labels)

    # ==========================================================
    # BUILD ADJACENCY (VECTOR SHIFT METHOD)
    # ==========================================================

    shifts = [(-1,0),(1,0),(0,-1),(0,1)]
    adjacency = {}

    for dx, dy in shifts:
        shifted = np.roll(mask, shift=(dx, dy), axis=(0,1))
        diff = mask != shifted

        pairs = np.stack((mask[diff], shifted[diff]), axis=1)

        for a, b in pairs:
            if a == b:
                continue
            adjacency.setdefault(a, set()).add(b)

    # ==========================================================
    # BUILD GRAPH EDGES
    # ==========================================================

    for node in G_inner.nodes():
        nbrs = adjacency.get(node, [])

        G_inner.nodes[node]['degree'] = len(nbrs)

        for nbr in nbrs:
            if nbr in G_inner.nodes():
                p1 = G_inner.nodes[node]['pixel_pos']
                p2 = G_inner.nodes[nbr]['pixel_pos']

                dist = np.linalg.norm(p1 - p2) / scale
                G_inner.add_edge(node, nbr, dis=dist)

    # ==========================================================
    # VISUALIZATION
    # ==========================================================

    img_vor = np.zeros((psy, psx, 3), dtype=np.uint8)
    img_vor_deg = np.ones((psy, psx, 3), dtype=np.uint8) * 127

    rng = np.random.default_rng()
    colors = rng.integers(0, 256, size=(len(nodelist), 3))

    node_to_idx = {node: i for i, node in enumerate(nodelist)}

    for node, i in node_to_idx.items():
        region = (mask == node)

        img_vor[region] = colors[i]

        if node in G_inner.nodes():
            deg = G_inner.nodes[node]['degree']
            img_vor_deg[region] = color_by_degree(deg)

    # ----------------------------------
    # Detect boundaries between regions
    # ----------------------------------
    boarder = np.zeros((psy, psx), dtype=bool)

    # Compare with right neighbor
    boarder[:, :-1] |= mask[:, :-1] != mask[:, 1:]

    # Compare with bottom neighbor
    boarder[:-1, :] |= mask[:-1, :] != mask[1:, :]
    boarder = binary_dilation(boarder, iterations=1)

    # Paint edges black
    img_vor_boarder = np.zeros((psy, psx), dtype=np.float16)
    img_vor_boarder[boarder] = [0]
    img_vor_boarder[~boarder] = [np.nan]
    


    return img_vor, img_vor_deg, img_vor_boarder, G, G_inner


# Computes network metrics values
def statistics(G,G_inner,G_MSF):
    """
    Compute structural metrics from graph and MST.

    Metrics:
        - Mean edge length
        - Std deviation of edge lengths
        - Average node degree
        - Defect ratio (non-hexagonal nodes)
        - Average Voronoi cell area

    Returns
    -------
    deg_list : list
    deg_avg : float
    m : float
        Mean edge length (normalized)
    sig : float
        Std deviation (normalized)
    S : float
        Mean cell area
    defect_ratio : float
    """
    Ne = G_MSF.number_of_edges()
    N = G_MSF.number_of_nodes()
    m = 0 # average edge length
    sig = 0 # standard deviation edge length
    deg_list = []
    deg_list = [G_inner.nodes[n]['degree'] for n, tmp in G_inner.nodes(data=True)]
    deg = sum(deg_list) / N # average degree
    #we can replace lines 408-9 with a single line "deg = np.mean"
    defect_ratio = [1 for n in deg_list if n!=6]
    defect_ratio = sum(defect_ratio)/N
    lengths = np.array([G_MSF[u][v]['dis'] for u, v, in G_MSF.edges()])
    m = np.mean(lengths)
    sig = np.std(lengths, ddof=1)
    S = sum([G_inner.nodes[n]['area_vor'] for n, tmp in G_inner.nodes(data=True)])/N
    m = m / np.sqrt(S) * (N-1)/N
    sig = sig / np.sqrt(S) * (N-1)/N
    return deg_list, deg, m, sig, S, defect_ratio

# Color coding the cells by their coordination number
def color_by_degree(deg):
    """
    Map node degree to RGB color.

    Ideal hexagonal structure (degree=6) is green.

    Returns
    -------
    list : [R, G, B]
    """
    if deg == 6:
        return [0, 255, 0]
    elif deg > 6:
        diff = int(255*min(np.sqrt(deg-6)/2,1))
        return [diff,255-diff,0]
    elif deg < 6:
        diff = int(255*min(np.sqrt(6-deg)/2,1))
        return [0,255-diff,diff]

