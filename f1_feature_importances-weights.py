# 1st Party Modules------------------------------------------------------------
import os
import sys
from typing import List

# 3rd Party Modules------------------------------------------------------------
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Custom Packages/Modules/Classes/Functions etc.-------------------------------
import PlotHelper
import constants_experiments
plt.style.use('./custom-mpl-style/plotly.mplstyle')


#------------------------------------------------------------------------------
def survey(data: pd.DataFrame, blocknames: pd.Index, features: List[str]):
    """
    Parameters
    ----------
    results : dict
        A mapping from question blocknames to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    
    category_names : list of str
        The category blocknames.
    """

    # Cumulative sum
    data_cum = data.cumsum(axis=0)

    fig, ax = plt.subplots(figsize=(19.2, 10.8))
    plt.subplots_adjust(left=0.095, right=0.805)

    ax.set_xlim(0, np.sum(data, axis=0).max())
    ax.xaxis.set_major_formatter("{x:.2f}")
    ax.xaxis.set_visible(False)
    ax.invert_yaxis()
# 
    for i, colname in enumerate(features):
        widths = data.iloc[i, :]
        starts = data_cum.iloc[i, :] - widths

        rects = ax.barh(blocknames, widths, left=starts, height=0.5,
            label=colname)
    
        ax.bar_label(rects, label_type='center', fmt="%.2f")

    patches: List[mpatches.Circle] = (
        PlotHelper.PlotHelper._set_patches(data.shape[0]))

    ax.set_ylabel("Block '0_10' vs. ")

    ax.legend(
        labels=features,
        handles=patches, 
        loc="upper left",
        fontsize='small',
        title="Legend",
        handler_map=PlotHelper.PlotHelper._legendh,
        bbox_to_anchor=PlotHelper.PlotHelper._bbox_anchor)


    return fig, ax
    

#------------------------------------------------------------------------------
if __name__ == '__main__':
    trainSpeaker: str = sys.argv[1] if sys.argv[1] else '101M'
    testsSpeaker: str = sys.argv[2] if sys.argv[2] else '101M'
    experiment: str = sys.argv[3] if sys.argv[3] else 'SD'
    
    speakerData: str = os.path.join(os.getcwd(), 'reports', '110M', 
        f"{experiment}-train-{trainSpeaker}_test-{testsSpeaker}"+
        f"_feat_importances.csv")

    # Open csv
    df: pd.DataFrame = pd.read_csv(speakerData).iloc[:, 1:]
    blocknames: pd.Index= df.columns
    
    # Get feature names
    feats: List[str] = constants_experiments.SIP_labels[1:-1]
    
    # Function to make a Barplot
    fig, ax = survey(data=df, blocknames=blocknames, features=feats)
    fig.suptitle(
        f"Feature-Importances-Over-Time, {experiment}-Experiment, Speaker {testsSpeaker}", 
        x=PlotHelper.PlotHelper._x_title, 
        y=PlotHelper.PlotHelper._y_title,
        fontsize=PlotHelper.PlotHelper._suptitle_fontsize
    )
    plt.show()
    
