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

### Onboarding

Work through the [Onboarding Page](/onboarding.md) to get what you need setup. 

###  Tutorials

Work through the [Tutorials page](/tutorials.md). If you are not familiar with Python or Git work through the [Python Tutorials](/tutorials.md#git-tutorials) and [Git sections](/tutorials.md#git-tutorials), work through the rest as needed.

### Summer Tasks

There are a number of projects that can be worked on which are broken down into `Code Quality`, `Workflow`, `Analysis`, and `Validation`. A detailed overview of the project can be found on the [projects page](https://github.com/orgs/GallagherSurfaceLab/projects/1/views/1) and a summary is in the table below. Clicking on a project link will take you to a detailed description of the project:

|Project | Type |
|--------|------|
[Fix the image area calculation bug][1] | Code Quality				
[Surpress the UserWarning in gray_process( )][2] | Code Quality				
[Vectorize the statistics( ) function][3] | Code Quality
[Create a `plot_voronoi()` helper function][13] | Code Quality
[Validate units and scale in img_file][14] | Validation
[Build a synthetic hexagonal lattice test][7] | Validation	
[Test sensitivity of results to the KDTree k parameter][6] | Validation		
[Move area filtering from find_nodes( ) to vornoi_tree( )][4] | Workflow				
[Investigate the Voronoi power weight parameter][5] | Workflow				
[Add analysis quantifying the distribution of degree and edge lengths][8] | Analysis				
[Plot and fit the MST edge length distribution][9] | Analysis				
[Compute the pair correlation function g(r)][10] | Analysis				
[Compute the hexatic order parameter ψ₆][11] | Analysis				
[Systematically Analyze a large number of images][12] | Analysis


**Use this checklist for every task on the Kanban board:**
```
[ ] Read the task card fully before writing any code
[ ] Pull the latest code from GitHub: git pull
[ ] Create a new branch: git checkout -b feature/task-XX-short-description
[ ] Read the relevant functions in stm_voronoi_mst.py before editing
[ ] Make your changes in small steps, testing as you go
[ ] Commit regularly (after each logical sub-step, not just at the end)
[ ] Write or update a docstring for any function you modify
[ ] Test your changes on the example notebook before considering the task done
[ ] Push your branch to GitHub: git push -u origin feature/task-XX-...
[ ] When the task is completely finished merge the task branch with the main branch
[ ] Move the card to "Done" on the Kanban board
```


[1]:https://github.com/GallagherSurfaceLab/summer_26/issues/1
[2]:https://github.com/GallagherSurfaceLab/summer_26/issues/2
[3]:https://github.com/GallagherSurfaceLab/summer_26/issues/3
[4]:https://github.com/GallagherSurfaceLab/summer_26/issues/4
[5]:https://github.com/GallagherSurfaceLab/summer_26/issues/5
[6]:https://github.com/GallagherSurfaceLab/summer_26/issues/6
[7]:https://github.com/GallagherSurfaceLab/summer_26/issues/7
[8]:https://github.com/GallagherSurfaceLab/summer_26/issues/8
[9]:https://github.com/GallagherSurfaceLab/summer_26/issues/9
[10]:https://github.com/GallagherSurfaceLab/summer_26/issues/10
[11]:https://github.com/GallagherSurfaceLab/summer_26/issues/11
[12]:https://github.com/GallagherSurfaceLab/summer_26/issues/12
[13]:https://github.com/GallagherSurfaceLab/summer_26/issues/13
[14]:https://github.com/GallagherSurfaceLab/summer_26/issues/14
