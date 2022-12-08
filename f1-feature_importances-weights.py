# 1st Party Modules------------------------------------------------------------
import os
import sys
from typing import List

# 3rd Party Modules------------------------------------------------------------
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# Custom Packages/Modules/Classes/Functions etc.-------------------------------
from constants_experiments import labels
from PlotHelper import PlotHelper, showPlot
plt.style.use('./custom-mpl-style/plotly-0.mplstyle')


#------------------------------------------------------------------------------
if __name__ == '__main__':
    trainSpeaker: str = sys.argv[1] if sys.argv[1] else '101M'
    testsSpeaker: str = sys.argv[2] if sys.argv[2] else '101M'
    experiment: str = sys.argv[3] if sys.argv[3] else 'SD'

    speakerData: str = os.path.join(os.getcwd(), 'reports', trainSpeaker, 'data-csv',
        f"{experiment}-train-{trainSpeaker}_test-{testsSpeaker}"+
        f"_feat_importances.csv")

    # Open csv
    df = pd.read_csv(speakerData).iloc[:, 1:]
    blocknames = df.columns
    
    # Get feature names
    feats: List[str] = labels[sys.argv[3]]
    
    # Function to make a Barplot
    fig, ax = PlotHelper.shapely(data=df, blocknames=blocknames, features=feats)
    showPlot()