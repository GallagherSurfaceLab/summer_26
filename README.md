# STM Minimum Spanning Tree Analysis Summer 2026

This project builds off of analysis presented in two papers which analyzed STM images ([Galeotti et al. 2019](https://doi.org/10.1039/C8SC05267K) and [Galeottie et al. 2020](https://doi.org/10.1038/s41563-020-0682-z)).

The overall goal of this summer project is to analyze a number of STM images and qauntify the structure of two-dimensional polymers. The code here is a modified version of the orginal code which fixes a number of errors, improves the image segmentation, vornoi algoritm, graph analysis, and plotting. 

The basic workflow of the code is: 
1. Image loading
2. Image Filtering
3. Image Segmentation
4. Image Labeling
5. Node identification
6. Voronoi tesselation
7. Voronoi graph analysis
8. Mimimum spanning tree (MST) analysis
9. Statistical analysis of the MST

A Jupyter notebook working through an example of this workflow can be opened by clicking on the badge below. 

<a href="https://colab.research.google.com/github/GallagherSurfaceLab/summer_26/blob/main/STM_voronoi.ipynb" target="_blank" rel="noopener noreferrer"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

There are a number of projects that can be worked on which are broken down into :

<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: var(--font-sans); }

.board { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; padding: 1rem 0; align-items: start; }

.column-header {
  font-size: 13px;
  font-weight: 500;
  color: var(--color-text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0 0 10px 0;
  border-bottom: 2px solid var(--color-border-tertiary);
  margin-bottom: 10px;
}

.col-backlog .column-header { border-color: #B4B2A9; }
.col-todo .column-header { border-color: #85B7EB; }
.col-progress .column-header { border-color: #EF9F27; }
.col-stretch .column-header { border-color: #5DCAA5; }

.card {
  background: var(--color-background-primary);
  border: 0.5px solid var(--color-border-tertiary);
  border-radius: var(--border-radius-lg);
  padding: 12px;
  margin-bottom: 8px;
  cursor: pointer;
  transition: border-color 0.15s;
}
.card:hover { border-color: var(--color-border-secondary); }

.card-tag {
  display: inline-block;
  font-size: 11px;
  font-weight: 500;
  padding: 2px 8px;
  border-radius: 99px;
  margin-bottom: 6px;
}
.tag-refactor { background: #D3D1C7; color: #444441; }
.tag-workflow { background: #B5D4F4; color: #0C447C; }
.tag-analysis { background: #C0DD97; color: #27500A; }
.tag-validation { background: #FAC775; color: #633806; }

.card-title {
  font-size: 13px;
  font-weight: 500;
  color: var(--color-text-primary);
  line-height: 1.4;
  margin-bottom: 4px;
}

.card-meta {
  font-size: 11px;
  color: var(--color-text-tertiary);
}

.modal-backdrop {
  display: none;
  position: fixed; top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.35);
  z-index: 100;
  align-items: center;
  justify-content: center;
}
.modal-backdrop.open { display: flex; }

.modal {
  background: var(--color-background-primary);
  border: 0.5px solid var(--color-border-secondary);
  border-radius: var(--border-radius-lg);
  padding: 24px;
  max-width: 480px;
  width: 90%;
  max-height: 80vh;
  overflow-y: auto;
  position: relative;
}

.modal-tag { display: inline-block; font-size: 11px; font-weight: 500; padding: 2px 8px; border-radius: 99px; margin-bottom: 10px; }
.modal-title { font-size: 16px; font-weight: 500; color: var(--color-text-primary); margin-bottom: 12px; line-height: 1.4; }
.modal-section { font-size: 12px; font-weight: 500; color: var(--color-text-secondary); text-transform: uppercase; letter-spacing: 0.05em; margin: 14px 0 6px; }
.modal-body { font-size: 13px; color: var(--color-text-secondary); line-height: 1.7; }
.modal-body ul { padding-left: 16px; }
.modal-body li { margin-bottom: 4px; }
.modal-close {
  position: absolute; top: 14px; right: 14px;
  background: none; border: none; cursor: pointer;
  font-size: 18px; color: var(--color-text-secondary); line-height: 1;
  padding: 4px 8px;
}
.modal-close:hover { color: var(--color-text-primary); }

.difficulty-pip { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 3px; }
.diff-1 { background: #1D9E75; }
.diff-2 { background: #EF9F27; }
.diff-3 { background: #E24B4A; }

.legend { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 14px; }
.legend-item { display: flex; align-items: center; gap: 6px; font-size: 12px; color: var(--color-text-secondary); }
.legend-dot { width: 8px; height: 8px; border-radius: 50%; }

.filter-bar { display: flex; gap: 8px; margin-bottom: 14px; flex-wrap: wrap; }
.filter-btn {
  font-size: 12px; padding: 4px 12px;
  border: 0.5px solid var(--color-border-secondary);
  border-radius: 99px;
  background: none;
  color: var(--color-text-secondary);
  cursor: pointer;
}
.filter-btn.active, .filter-btn:hover {
  background: var(--color-background-secondary);
  color: var(--color-text-primary);
}
</style>

<span class="modal-tag tag-workflow">Workflow</span>

<button class="filter-btn" onclick="setFilter('analysis', this)">Analysis</button>
