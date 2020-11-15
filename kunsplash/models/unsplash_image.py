# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# Local
from .image_urls import ImageUrls

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------------- class: UnsplashImage --------------------------------------------------------- #

class UnsplashImage:

    # ------------------------------------------------------------- Init ------------------------------------------------------------- #

    def __init__(
        self,
        d: dict
    ):
        self.id = d['id']
        self.orgW = d['width']
        self.orgH = d['height']
        self.ratio = self.orgW / self.orgH
        self.color = d['color']
        self.description = d['description']
        self.alt_description = d['alt_description']
        self.urls = ImageUrls(['urls'])


# ---------------------------------------------------------------------------------------------------------------------------------------- #