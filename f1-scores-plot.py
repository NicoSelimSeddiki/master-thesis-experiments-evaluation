# 1st Party Modules------------------------------------------------------------
...

# 3rd Party Modules------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Custom Packages/Modules/Classes/Functions etc.-------------------------------
from PlotHelper import PlotHelper

# Type Annotations-------------------------------------------------------------
from typing import List
from numpy.typing import ArrayLike


if __name__ == "__main__":

    # SI - F1 scores 
    f1_SD_Experiment_All_Feats: ArrayLike = np.array(
        [
            [0.78, 0.62, 0.72, 0.84],
            [0.84, 0.73, 0.68, 0.73],
            [0.81, 0.74, 0.76, 0.69],
            [0.79, 0.75, 0.69, 0.77],
            [0.74, 0.73, 0.69, 0.85],
            [0.88, 0.70, 0.70, 0.72],
            [0.84, 0.85, 0.84, 0.77],
            [0.85, 0.89, 0.79, 0.75]], 
            dtype=np.float64
    )

    f1_SD_Experiment_10_Feats: ArrayLike = np.array(
        [
            [0.80, 0.62, 0.67, 0.82],
            [0.76, 0.77, 0.72, 0.69],
            [0.83, 0.73, 0.58, 0.77],
            [0.79, 0.87, 0.61, 0.77],
            [0.78, 0.69, 0.61, 0.79],
            [0.84, 0.79, 0.72, 0.69],
            [0.80, 0.84, 0.82, 0.58],
            [0.83, 0.85, 0.83, 0.67]], 
            dtype=np.float64
    )
    
    # SI - F1 scores 
    f1_SI_Experiment_All_Feats: ArrayLike = np.array(
        [
            [0.42, 0.63, 0.66, 0.67],
            [0.58, 0.62, 0.59, 0.21],
            [0.35, 0.10, 0.54, 0.05],
            [0.54, 0.39, 0.18, 0.14],
            [0.62, 0.68, 0.31, 0.22],
            [0.65, 0.70, 0.54, 0.29],
            [0.71, 0.65, 0.39, 0.10],
            [0.55, 0.68, 0.23, 0.00]], 
            dtype=np.float64
    )
 
    f1_SI_Experiment_10_Feats: ArrayLike = np.array(
        [
            [0.63, 0.59, 0.65, 0.67],
            [0.61, 0.60, 0.65, 0.47],
            [0.52, 0.58, 0.49, 0.05],
            [0.62, 0.34, 0.44, 0.09],
            [0.69, 0.26, 0.15, 0.53],
            [0.76, 0.63, 0.57, 0.55],
            [0.77, 0.65, 0.31, 0.05],
            [0.48, 0.65, 0.38, 0.00]], 
            dtype=np.float64
    )

    # SI - F1 scores 
    f1_SIP_Experiment_All_Feats: ArrayLike = np.array(
        [
            [0.62, 0.74],
            [0.78, 0.68],
            [0.59, 0.79],
            [0.72, 0.68],
            [0.62, 0.75],
            [0.80, 0.63],
            [0.60, 0.68],
            [0.67, 0.75]], 
            dtype=np.float64
    )

    f1_SIP_Experiment_10_Feats: ArrayLike = np.array(
        [
            [0.61, 0.71],
            [0.70, 0.70],
            [0.57, 0.59],
            [0.70, 0.62],
            [0.68, 0.75],
            [0.74, 0.63],
            [0.61, 0.76],
            [0.70, 0.68]], 
            dtype=np.float64
    )


    #--------------------------------------------------------------------------
    # expr = sys.argv[1]
    # num_feat = sys.argv[2]

    speaker_names_ALL_SD_SI: List[str] = ['101M', '102M', '103M', '104M']
    speaker_names_SIP: List[str] = ['111Mrec1', '114Frec1']

    fig, ax = PlotHelper.lineplot(
        f1_SIP_Experiment_10_Feats[:, 0],
        f1_SIP_Experiment_10_Feats[:, 1],
        # f1_SI_Experiment_All_Feats[:, 2],
        # f1_SI_Experiment_All_Feats[:, 3],
        # name=f"F1-Score, {expr}-Experiments-{num_feat}-Features",
        description=speaker_names_SIP,
        xl='block 0_10 vs.',
        yl='f1-scores'
    )   

    plt.show()