import pandas as pd
import numpy as np
from scipy import stats

def correlation(x,y,method:{'normal','ordinal'}='normal', alpha=0.05):
    try:
        if method=='ordinal':
            spearman_corr, spearman_p = stats.spearmanr(x, y)
            if spearman_p<=alpha:
                return {'spearman_corr': spearman_corr, 'spearman_p': spearman_p, 'crux': "There is statistically significant correlation between x & y"}
            else:
                return {'spearman_corr': spearman_corr, 'spearman_p': spearman_p, 'crux': "There's not enough statistically significant correlation between x & y"}
        else:
            pearson_corr, pearson_p = stats.pearsonr(x, y)
            if pearson_p<=alpha:
                return {'pearson_corr': pearson_corr, 'pearson_p': pearson_p, 'crux': "There is statistically significant linear correlation between x & y"}
            else:
                return {'pearson_corr': pearson_corr, 'pearson_p': pearson_p, 'crux': "There's not enough statistically significant linear correlation between x & y"}
    except Exception as e:
        raise(e)

