# 1st Party Modules
from typing import List, Tuple

# 3rd Party Modules
import matplotlib.pyplot as plt
from matplotlib.legend import Legend

import matplotlib.patches as mpatches
from matplotlib.legend_handler import HandlerPatch


class HandlerElipse(HandlerPatch):
    """ Handler for an Elipse

    attributes
    ----------
        ...

    public methods and attributes
    -----------------------------
    (publicmethod) create_artist() 

    Resources
    ---------
    [1]: Official Docu. 'legend_handler'            (https://bit.ly/3nceIGB)
    [2]: Official Docu. 'matplotlib.patches'        (https://bit.ly/3h6fZec)
    [3]: 'Implementening a custom legend handler'   (https://bit.ly/3jMHoUj)
    [4]: 'using-mpatches-patch-for-a-custom-legend' (https://bit.ly/3h2LaXS)
    
    """
    
    def create_artists(self, 
        legend: Legend, 
        orig_handle: plt, 
        xdescent: float, 
        ydescent: float, 
        width: float, 
        height: float, 
        fontsize: int, 
        trans: float
        ) -> List[mpatches.Ellipse]:
        """ Class to create an eliptic artist object
        
        Parameters
        ----------
        legend : matplotlib.legend.Legend object
            Legend object itself
        
        orig_handle : matplotlib.pyplot Plot object
            Is the original plot
        
        xdescent : float 
            x-offset of the Elipse
        
        ydescent : float 
            y-offset of the Elipse
        
        width : float 
            Width of the artist
        
        height : float 
            Height of the artist

        fontsize : int
            Size of font in pixels
        
        trans : float
            Transormation 

        Returns
        -------
            p : List[mpatches.Ellipse]

        """

        center: Tuple[float, float] = (
            0.5 * width - 0.5 * xdescent, 
            0.5 * height - 0.5 * ydescent
            )
        
        p: mpatches.Ellipse = mpatches.Ellipse(xy=center, 
            width=height + xdescent, 
            height=height + ydescent
            )

        self.update_prop(p, orig_handle, legend)
        p.set_transform(trans)

        return [p]
