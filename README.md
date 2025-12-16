# Cell Maps for AI (CM4AI) Immunofluorescence (IF) Embedding Tutorial

## Overview
This tutorial will work with the IF data that are available in the [CM4AI March 2025 Data Release](https://dataverse.lib.virginia.edu/dataset.xhtml?persistentId=doi:10.18130/V3/B35XWX). This release contains IF images for 4 channels in untreated, [paclitaxel-treated](https://www.cancer.gov/about-cancer/treatment/drugs/paclitaxel), and [vorinostat-treated](https://www.cancer.gov/about-cancer/treatment/drugs/vorinostat) [MDA-MB-468 breast cancer cells](https://www.cellosaurus.org/CVCL_0419).

With the Python notebooks and scripts in the src directory, you will be able to:
1. Download and extract the raw IF data from Dataverse
2. Run an exploratory data analysis (EDA) for the images
3. Generate embeddings for the images using the [CM4AI cell maps pipeline](https://github.com/idekerlab/cellmaps_pipeline)
4. Create a similarity graph that represents each gene/protein in the data set
5. Explore the effects of each treatment on protein similarity based on the embeddings

## Background Information
For a quick background on CM4AI data and tools, the following short videos provide a quick introduction:

| **Introduction to CM4AI** | **Introduction to the Cell Map Pipeline** | **CM4AI Data Generation: Immunofluorescence** |
|:-------------------------:|:----------------------------------------:|:--------------------------------------------:|
| [![Introduction to CM4AI](https://img.youtube.com/vi/wiGgof7gY3w/hqdefault.jpg)](https://www.youtube.com/watch?v=wiGgof7gY3w) | [![Cell Map Pipeline](https://img.youtube.com/vi/AK2eQbOys2I/hqdefault.jpg)](https://www.youtube.com/watch?v=AK2eQbOys2I) | [![CM4AI Immunofluorescence](https://img.youtube.com/vi/Ys5rFvMMtE4/hqdefault.jpg)](https://www.youtube.com/watch?v=Ys5rFvMMtE4) |

## Working with the Tutorial
1. Create a conda environment
```
conda env create -f environment.yml
```
2. Activate the environment
```
conda activate cm4ai-tutorial-if
```
3. Review and run the tutorial scripts
   1. Download the CM4AI data release: [View Script](src/download.py)
   ```
   python src/download.py
   ```
   2. Explore the data set: [View Notebook](src/eda.ipynb)
   3. Generate embeddings with cellmaps_image_embedder: [View Script](src/generate_embeddings.py)
   ```
   python src/generate_embeddings.py
   ```
   4. Generate a protein similarity graph based on the embedding and visualize results: [View Notebook](src/generate_graph.ipynb)

## Links and References
* CM4AI Website: https://cm4ai.org
* YouTube Channel: https://youtube.com/@cm4ai
* CM4AI Pre-Print: https://www.biorxiv.org/content/10.1101/2024.05.21.589311v1