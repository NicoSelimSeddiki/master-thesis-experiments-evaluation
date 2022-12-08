# 1st Party Modules------------------------------------------------------------
import os

# 3rd Party Modules------------------------------------------------------------
import pandas as pd

# Custom Packages/Modules/Classes/Functions etc.-------------------------------
from commandline_parser import args
from helperfunctions import get_files
from PlotHelper import PlotHelper, saveFig

from constants_experiments import labels, time_stemps


# ------------------------------------------------------------------------------
if __name__ == "__main__":
    experimentID: str = args["experimentID"]
    filelocation: str = args["filelocation"]
    numfeats: str = args["numfeats"]
    plotsyle: str = args["plot"]

    # Check if directory exists
    try:
        if not (os.path.exists(fullpath := os.path.join(os.getcwd(), filelocation))):
            os.makedir(fullpath)

    except FileExistsError:
        pass

    # Check if the user chose a violin or shapely plot
    search_pattern: str = None
    match plotsyle:
        case "violin":
            search_pattern: str = "_cross_val_"
        case "shapely":
            search_pattern: str = "_feat_importances"
        case _:
            pass

    # Load all of the data into the workspace
    files = list(get_files(fullpath, experimentID, search_pattern))
    base_names = list(map(lambda name: name.split("\\")[-3], files))
    data_frames = map(lambda path: pd.read_csv(path).iloc[:, 1:], files)


    # Make a violinplot
    if plotsyle == "violin":
        fig, ax = PlotHelper.violinplot(data_frames, base_names, experimentID)

        # Specify path where we save the pictures
        pictpath = os.path.join(
            os.getcwd(),
            "pictures",
            experimentID,
            f"{experimentID}_Experiment_f1_{numfeats}_Features_Violinplot",
        )

        # Save figure
        for f in ["png", "eps"]:
            saveFig(f"{pictpath}.{f}")

    # Make a shapelyplot
    if plotsyle == "shapely":
        for base_name, data_frame in zip(base_names, data_frames):
            fig, ax = PlotHelper.shapely(
                data_frame, time_stemps[1:], labels[experimentID]
            )

            # Specify path where we save the pictures
            pictpath = os.path.join(
                os.getcwd(),
                "pictures",
                experimentID,
                f"{experimentID}_Experiment_{base_name}_f1_{numfeats}_Features_Over_Time",
            )

            # Save figure
            for f in ["png", "eps"]:
                saveFig(f"{pictpath}.{f}")
