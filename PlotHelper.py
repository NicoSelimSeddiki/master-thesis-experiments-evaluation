# 1st Party Modules
...

# 3rd Party Modules
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.offsetbox import AnchoredOffsetbox, VPacker, TextArea

# Custom Modules
from CustomHandler import HandlerElipse

# Style of plot
plt.style.use("./custom-mpl-style/plotly-0.mplstyle")

# Type annotations
from TypeAnnotations import Dict, List, Tuple, Union, DataFrame, DataSeries, ArrayLike


class PlotHelper:
    """Helper class for different Plot functions.

    This class is intended as a wrapper for different
    plot functions like line, bar, stem et. plots

    class attributes
    ----------------
    (private attribute) _answers    : Abbrevations for the answers.
    (private attribute) _borderpad  : Border between Axes object and legend object.
    (private attribute) _bbox_anchor: Anchor coordinates to place the legend.
    (private attribute) _colors     : Hexstrings, representing plotly colors.
    (private attribute) _labelpad   : Pad between axes object and the axes label.
    (private attribute) _legendh    : Handler for legends.
    (private attribute) _loc        : Legend location.
    (private attribute) _num_bins   : Number of bin for the histogram.
    (private attribute) _prop_cycle : cycler.Cycle object Composable cycles.
    (private attribute) _questions  : Abbrevations for the questions.
    (private attribute) _radius     : Radius of circle.
    (private attribute) _rotation   : Rotation of the y-axis labels.
    (private attribute) _title      : Legend title.
    (private attribute) _xy         : Coordinates of circle.
    (private attribute) _x_title    : x-coord Legend title.
    (private attribute) _y_title    : y-coord Legend title.

    public methods
    --------------
    (static method)  hgram()        : Histogram
    (static method)  qplot()        : Questionaire Scatter Plots
    (static method)  lineplot()     : Lineplot
    (static method)  scatterplot()  : Scatterplot

    private methods
    ---------------
    (classmethod)      _set_patches :

    """

    # General - Custom legend key entries for each plot function
    _prop_cycle = mpl.rcParams["axes.prop_cycle"]
    _colors: List[str] = _prop_cycle.by_key()["color"]
    _markers: List[str] = _prop_cycle.by_key()["marker"]

    _legendh: Dict = {mpatches.Circle: HandlerElipse()}

    # General - circle radius and coordinates
    _radius: float = 0.75
    _xy: Tuple[float, float] = (0.5, 0.5)

    # General - legend parameter
    _title: str = "Legend"
    _loc: str = "upper left"
    _borderpad: float = 0.0
    _bbox_anchor: Tuple[float, float] = (1.0125, 1)
    _legend_title_fontsize: float = 18
    _legen_labels_fontsize: float = 16

    # General - location of title
    _x_title: float = 0.5
    _y_title: float = 0.965

    _x_label_fontsize: float = 20
    _y_label_fontsize: float = 20

    # General - Text
    _rotation: float = 0.0
    _labelpad: float = 25.0
    _suptitle_fontsize: float = 25.0

    # General - Marker size
    _marker_size = float = 10

    # Histogram - Number of bins
    _num_bins: int = 250

    # Questions and Answers
    _answers: List[str] = ["A", "B", "C"]
    _questions: List[str] = ["Q1", "Q2", "Q3"]

    # Ticks for each block
    _x_ticks: List[str] = [
        "10_20",
        "20_30",
        "30_40",
        "40_50",
        "50_60",
        "60_70",
        "70_80",
        "80_90",
    ]

    # Static methods:------------------------------------------------------
    @staticmethod
    def clusters(
        cluster1: DataSeries, cluster2: DataSeries, feat1: str, feat2: str
    ) -> None:
        """Function to plot different scatterplots."""

        # Initialize plot
        fig, ax = plt.subplots(nrows=1, ncols=1)

        # Render onto the axes object
        ax.scatter(cluster1[feat1], cluster1[feat2], color=PlotHelper._colors[0])
        ax.scatter(cluster2[feat1], cluster2[feat2], color=PlotHelper._colors[1])

        # Set labels
        ax.set_xlabel(feat1)
        ax.set_ylabel(feat2)

        # Set figure name
        fig.suptitle(f"Scatterplot", x=PlotHelper._x_title, y=PlotHelper._y_title)

    @staticmethod
    def scatterplot(
        feature1: DataSeries, feature2: DataSeries, xl: str, yl: str
    ) -> None:
        """Simple Scatterplot

        Goal is to get more insight on how different pairwise comparisions
        between two features are related with each other

        Paramters
        ---------
        feature1 :  DataSeries
            First feature. In our case always F0

        feature2 :  DataSeries
            Second feature

        xl : str
            x-axis label

        yl : str
            y-axis label

        Returns
        -------
        None

        """

        # Initialize plot
        fig, ax = plt.subplots(nrows=1, ncols=1)

        alphas: ArrayLike = np.linspace(1, 0.2, len(feature1))
        sizes: ArrayLike = np.linspace(10, 1, len(feature1))

        # Render onto the axes object
        ax.scatter(feature1, feature2, s=sizes, alpha=alphas)

        # Set labels
        ax.set_xlabel(xl)
        ax.set_ylabel(yl)

        # Set figure name
        fig.suptitle(f"Scatterplot", x=PlotHelper._x_title, y=PlotHelper._y_title)

    @staticmethod
    def hgram(data: List[DataFrame], feature: str) -> None:
        """A Simple histogram plot

        Parameters
        ----------
        data :
            List of pandas Dataframe objects

        feature : str
            Name of the featurea

        Returns
        -------
            None

        """

        # Initialize plot
        fig, ax = plt.subplots(nrows=1, ncols=1)

        ax.hist(data[0], bins=PlotHelper._num_bins)
        ax.hist(data[1], bins=PlotHelper._num_bins, alpha=0.75)

        # Set axis labels, axis limits and legend
        ax.set_ylabel(f"Number of bins")
        ax.set_xlabel(f"Range of {feature}")

        # Set the number of legend patches
        len_data: int = len(data)
        labels: List[str] = [
            f"{i*10} minutes" for i in range(len(PlotHelper._x_ticks) + 1)
        ]
        patches: List[mpatches.Circle] = PlotHelper._set_patches(len_data)

        # Set legend
        ax.legend(
            labels=labels,
            handles=patches,
            loc=PlotHelper._loc,
            title=PlotHelper._title,
            handler_map=PlotHelper._legendh,
            borderaxespad=PlotHelper._borderpad,
            bbox_to_anchor=PlotHelper._bbox_anchor,
        )

        # Set figure name
        fig.suptitle(
            f"Histogram for {feature}", x=PlotHelper._x_title, y=PlotHelper._y_title
        )

    @staticmethod
    def lineplot(*args, description: List[str], xl: str, yl: str) -> None:

        if len(args) != len(description):
            raise ValueError("Num args != num provided labels!")

        # Initialize plot
        fig, ax = plt.subplots(nrows=1, ncols=1)
        plt.gca().set_prop_cycle(marker=PlotHelper._markers, color=PlotHelper._colors)

        for arg in args:
            ax.plot(
                PlotHelper._x_ticks,
                arg,
                markersize=PlotHelper._marker_size,
                linestyle="dashed",
            )

        # Set axis labels, axis limits
        ax.set_xticks(PlotHelper._x_ticks)
        ax.set_xticklabels(PlotHelper._x_ticks)
        ax.set_xlabel(xl, fontsize=PlotHelper._x_label_fontsize)

        ax.set_ylim(bottom=0.0, top=1.0)
        ax.set_ylabel(yl, fontsize=PlotHelper._y_label_fontsize)

        # Initialize patches for the handler
        patches = PlotHelper._set_patches(len(args))

        # Set legend
        ax.legend(
            title_fontsize=PlotHelper._legend_title_fontsize,
            fontsize=PlotHelper._legen_labels_fontsize,
            labels=description,
            handles=patches,
            loc=PlotHelper._loc,
            title=PlotHelper._title,
            handler_map=PlotHelper._legendh,
            borderaxespad=PlotHelper._borderpad,
            bbox_to_anchor=PlotHelper._bbox_anchor,
        )

        return fig, ax

    @staticmethod
    def qplot(
        data: Union[ArrayLike, DataFrame], answers: List[DataFrame], xl: str
    ) -> None:
        """Questioniare Plot - Plot relationship between a speech
        signal and the self rating assessment (short SRA).

        Notes
        -----
        The anchored box with the plot explanation is based of [1].

        Parameters
        ----------
        data : ArrayLike or Pandas.Series
            Array with data

        answers : List of pandas Dataframe object
            Questioniare answers

        xl : str
            Feature name respectively x-axis label

        Returns
        -------
        None

        Resources
        ---------
        [1] Anchored Box04 (08.10.2021), matplotlib documentation
            https://matplotlib.org/stable/gallery/userdemo/anchored_box04.html

        """

        # Initialize plot
        fig, ax = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True)

        # Alphas for scatterplot - Represents how the feature changed over time
        # See Transparency (alpha) can be set as an array in collections
        # https://bit.ly/39jGFns (18.09.2021)
        alphas: ArrayLike = np.linspace(1, 0.1, len(data))

        # Markersize for scatterplot - Represents how the self evaluated
        # speaking rate changed over time.
        # Small values suggest a slow speaking rate, high values a faster one.
        m_size: ArrayLike = answers[3].loc["A"]

        # Added a small offset of 2.0 for the marker size in case of
        # a speaking rate of 0
        for i in range(0, 3):
            for j in range(0, 3):
                ax[i, j].scatter(
                    data,
                    answers[j].iloc[i],
                    color=PlotHelper._colors[j],
                    alpha=alphas,
                    s=m_size + 2.0,
                )

            # set x-axis labels and position
            ax[0, i].xaxis.set_label_position("top")
            ax[0, i].set_xlabel(
                PlotHelper._questions[i], labelpad=PlotHelper._labelpad // 2
            )

            # set y-axis labels
            ax[i, 0].set_ylabel(
                PlotHelper._answers[i],
                labelpad=PlotHelper._labelpad,
                rotation=PlotHelper._rotation,
            )

        # Text Properties of the textboxes
        text_prop: Dict = {"color": mpl.rcParams["axes.labelcolor"]}

        # Questions Box - Elements---------------------------------------------
        text_Q: TextArea = TextArea("Questions", textprops={"size": 12})

        text_Q1 = TextArea(
            "Q1: Voice feel during the last 10 min.?", textprops=text_prop
        )

        text_Q2 = TextArea("Q2: Voice feel right now?", textprops=text_prop)

        text_Q3 = TextArea("Q3: Feeling in general?", textprops=text_prop)

        text: List[TextArea] = list(
            map(
                lambda txt: TextArea(txt, textprops=text_prop),
                [
                    "Q1: Voice feel during the last 10 min.?",
                    "Q2: Voice feel right now?",
                    "Q3: Feeling in general?",
                ],
            )
        )

        box_Q: VPacker = VPacker(
            children=[text_Q, text_Q1, text_Q2, text_Q3], align="left", pad=0, sep=20
        )

        anchored_box: AnchoredOffsetbox = AnchoredOffsetbox(
            bbox_to_anchor=PlotHelper._bbox_anchor,
            bbox_transform=ax[0, 2].transAxes,
            loc="upper left",
            frameon=False,
            child=box_Q,
        )

        # Add TextBox to the upper right axes object
        ax[0, 2].add_artist(anchored_box)

        # Answers Box - Elements-----------------------------------------------
        text_A: TextArea = TextArea("Answers", textprops={"size": 12})

        text_A1 = TextArea("A: not strained(0) - strained(10)", textprops=text_prop)

        text_A2 = TextArea("B: rested(0) - not rested(10)", textprops=text_prop)

        text_A3 = TextArea("C: smooth(0) - rough(10)", textprops=text_prop)

        box_A: VPacker = VPacker(
            children=[text_A, text_A1, text_A2, text_A3], align="left", pad=0, sep=20
        )

        anchored_box: AnchoredOffsetbox = AnchoredOffsetbox(
            bbox_to_anchor=PlotHelper._bbox_anchor,
            bbox_transform=ax[1, 2].transAxes,
            loc="upper left",
            frameon=False,
            child=box_A,
        )

        # Add TextBox to the upper right axes object
        ax[1, 2].add_artist(anchored_box)

        # Set figure name
        fig.suptitle(
            f"Relationship between SRA and {xl}",
            x=PlotHelper._x_title,
            y=PlotHelper._y_title,
        )

        # Set figure xlabel
        fig.supxlabel(xl)
        fig.supylabel("Self-Rating-Assessment Values")

        plt.tight_layout()


    @staticmethod
    def violinplot(data: List[DataFrame], labels: List[str], ID: str):

        # Plot  the results
        fig, ax = plt.subplots(nrows=1, ncols=1)
        fig.suptitle(
            f"",
            x=PlotHelper._x_title,
            y=PlotHelper._y_title,
            fontsize=PlotHelper._suptitle_fontsize,
        )

        PlotHelper._set_axis_style(ax=ax, labels=PlotHelper._x_ticks)

        inds = np.arange(1, 9)
        for i, elem in enumerate(data):
            ax.violinplot(elem, positions=inds + 0.18 * i, widths=0.12)

        patches = PlotHelper._set_patches(len(labels))

        # Set legend
        ax.legend(
            title_fontsize=PlotHelper._legend_title_fontsize,
            fontsize=PlotHelper._legen_labels_fontsize,
            labels=labels,
            handles=patches,
            loc=PlotHelper._loc,
            title=PlotHelper._title,
            handler_map=PlotHelper._legendh,
            borderaxespad=PlotHelper._borderpad,
            bbox_to_anchor=PlotHelper._bbox_anchor,
        )

        return fig, ax

    # ------------------------------------------------------------------------------
    @staticmethod
    def shapely(data: DataFrame, blocknames, features: List[str]):
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
        fig, ax = plt.subplots(nrows=1, ncols=1)
        plt.subplots_adjust(left=0.095, right=0.805)

        ax.set_xlim(0, np.sum(data, axis=0).max())
        ax.xaxis.set_major_formatter("{x:.2f}")
        ax.xaxis.set_visible(False)
        ax.invert_yaxis()
        #
        for i, colname in enumerate(features):
            widths = data.iloc[i, :]
            starts = data_cum.iloc[i, :] - widths

            rects = ax.barh(blocknames, widths, left=starts, height=0.5, label=colname)

            ax.bar_label(rects, label_type="center", fmt="%.2f")

        patches: List[mpatches.Circle] = PlotHelper._set_patches(data.shape[0])

        fig.suptitle(
            "",
            x=PlotHelper._x_title,
            y=PlotHelper._y_title,
            fontsize=PlotHelper._suptitle_fontsize,
        )

        ax.set_ylabel("Block '0_10' vs. ", fontsize=20)
        ax.legend(
            labels=features,
            handles=patches,
            loc="upper left",
            title_fontsize=20,
            fontsize=16,
            title="Legend",
            handler_map=PlotHelper._legendh,
            bbox_to_anchor=PlotHelper._bbox_anchor,
        )

        return fig, ax

    # Class methods:---------------------------------------------------------
    @classmethod
    def _set_patches(cls, len_data: int = 1) -> List[mpatches.Circle]:
        """Set legend keys for multiple entries in a figure

        Parameters
        ----------
        len_data : int
            Length of data array

        Return
        ------
        List[mpatches.Circle]
        List of mpatches.Circle objects with different facecolor

        """

        return [
            mpatches.Circle(xy=cls._xy, radius=cls._radius, facecolor=cls._colors[i])
            for i in range(len_data)
        ]

    # -------------------------------------------------------------------------
    @classmethod
    def _set_axis_style(cls, ax, labels):
        """Copied and adapted directly from

        https://matplotlib.org/stable/gallery/statistics/customized_violin.html

        """

        ax.xaxis.set_tick_params(direction="out")
        ax.xaxis.set_ticks_position("bottom")
        ax.set_xticks(np.arange(1, len(labels) + 1), labels=labels)

        ax.set_xlim(0.25, len(labels) + 0.75)
        ax.set_ylim(bottom=0.0, top=1.0)

        ax.set_xlabel("block 0_10 vs.", fontsize=PlotHelper._x_label_fontsize)
        ax.set_ylabel("f1-scores", fontsize=PlotHelper._y_label_fontsize)


# ----------------------------------------------------------------------------------
def showPlot():
    plt.show()


# ----------------------------------------------------------------------------------
def saveFig(path_to_save: str):
    plt.savefig(path_to_save)
