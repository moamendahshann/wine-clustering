# Wine Clustering

Explore chemical measurements of wines with standardisation, KMeans and a two-dimensional PCA view. The number of clusters is selected without consulting the reference classes.

[![CI](https://github.com/moamendahshann/wine-clustering/actions/workflows/ci.yml/badge.svg)](https://github.com/moamendahshann/wine-clustering/actions/workflows/ci.yml)

![PCA view of the exploratory clusters](results/clusters.png)

## Results

| Measure | Recorded result |
| --- | ---: |
| Samples | 178 |
| Selected cluster count | **3** |
| Silhouette score at k=3 | 0.2849 |
| Adjusted Rand index against reference classes | 0.8975 |

[Full recorded metrics, including k=2 through k=6](results/metrics.json)

## Method

Standardise all features, fit KMeans for k=2…6 with 20 initialisations and seed 42, select the highest silhouette score, then use PCA for plotting. The reference class labels are used only afterwards for descriptive comparison via adjusted Rand index.

## Run locally

Python 3.11 or newer is recommended.

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS / Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python train.py
```

The dataset is bundled with scikit-learn; no dataset download or API key is required. Results and plots are written to `results/`. Random seed: 42. Dependency and platform differences can affect results.

## Interpretation and limitations

This is full-dataset exploratory analysis, not held-out predictive evaluation. The PCA plot is a projection of higher-dimensional features; apparent separation in two dimensions is not a complete measure of cluster quality. The clusters do not establish causal or business categories.

## Development notes

This is an educational portfolio project developed with AI assistance. The recorded results describe the included experiment, not a production system or a previous employment achievement.

## Automated checks

GitHub Actions reruns the experiment and checks the generated metrics and plots. You can run the same check locally with `python scripts/verify_results.py` after training. The status badge reflects the latest workflow result; it is not a real-world quality guarantee.

## Source

[scikit-learn wine dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html)
