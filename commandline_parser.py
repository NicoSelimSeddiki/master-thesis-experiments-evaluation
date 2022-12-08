# 1st Party Modules------------------------------------------------------------
import argparse

# ------------------------------------------------------------------------------
parser: argparse.ArgumentParser = argparse.ArgumentParser(
    usage="Provide up to 3 arguments to the commandline",
    description="A small commandline parser"
    + " to plot and save the results of the RandomForest experiments.",
)

# Specify which plot the user 
parser.add_argument(
    "--plot",
    "-p",
    help="Chose plotstyle",
    choices=["shapely", "violin"],
    default="violin",
    metavar=str,
)

# The first argument specifies the location, were all files are stored
parser.add_argument(
    "--filelocation",
    "-f",
    help="The location where the files can be loaded from.",
    default="reports",
    metavar=str,
)

# Both arguments are optional and set to a default value
parser.add_argument(
    "--experimentID",
    "-e",
    help="String which specifies the experiment. Defaults to Speaker-Dependent"
    + " (SD) experiment.",
    choices=["SD", "SI", "SIP"],
    default="SD",
    metavar=str,
)

# Both arguments are optional and set to a default value
parser.add_argument(
    "--numfeats",
    "-n",
    help="String which specifies the number of features used in the experiment."
    + 'Defaults to "10".',
    choices=["All", "10"],
    default="10",
    metavar=str,
)

# ------------------------------------------------------------------------------
args: argparse.Namespace = vars(parser.parse_args())
