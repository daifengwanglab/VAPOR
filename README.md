# Variational autoencoder with transport operators decouples co-occurring biological processes in development

Emerging single-cell and spatial transcriptomic data enable the investigation of gene expression dynamics of various biological processes, especially for development. To this end, existing computational methods typically infer trajectories that sequentially order cells for revealing gene expression changes in development, e.g., to assign a pseudotime to each cell indicating the ordering. However, these trajectories can aggregate different biological processes that cells undergo simultaneously such as maturation for specialized function and differentiation into specific cell types that do not occur on the same timescale. Therefore, a single pseudotime axis may not distinguish gene expression dynamics from co-occurring processes. 

We introduce a method, VAPOR (variational autoencoder with transport operators), to decouple dynamic patterns from developmental gene expression data. Particularly, VAPOR learns a latent space for gene expression dynamics and decomposes the space into multiple subspaces. The dynamics on each subspace are governed by an ordinary differential equation model, attempting to recapitulate specific biological processes. Furthermore, we can infer the process-specific pseudotimes, revealing multifaceted timescales of distinct processes in which cells may simultaneously be involved during development. 

VAPOR is open source for general use to parameterize and infer developmental gene expression dynamics. It can be further extended for other single-cell and spatial omics such as chromatin accessibility to reveal developmental epigenomic dynamics.

![fig1](https://github.com/JieShengm/VAPOR/blob/main/figures/fig1.png)

# Usage

## Installation

Clone and navigate to the repository. Create and activate VAPOR environment using python 3.9 with `conda`,

```
git clone https://github.com/JieShengm/VAPOR
cd VAPOR
conda env create -f environment.yml
conda activate VAPOR_env
```

## Training

VAPOR trains on `.h5ad` files (AnnData format). Basic usage:

```
python VAPOR/main.py --data_path /PATH/TO/FILE
```

Key hyperparameters:

 - --M: Number of psi matrices (default: 4)
 - --latent_dim: Dimensionality of latent space (default: 2)

Model outputs are saved to --output_dir (default: './out/').

## Inference

Example of using trained model:

```{python}
from utilities import *

# Paths
data_path = 'path/to/data.h5ad'
model_path = 'path/to/model.pth'

# Model configuration
adata_list = construct_VAPOR_adata(
    data_path,
    model_path,
    **params
)
```

Output format:

```
AnnData object with n_obs × n_vars = 4096 × 2
    obs: 't'
    obsm: 'X_mu', 'X_z'
    layers: 'mu1_psi0', 'v_psi0'
```
For downstream analysis examples, see [simulation_cyclic.ipynb](https://github.com/JieShengm/VAPOR/blob/main/demo/simulation-cyclic.ipynb).

