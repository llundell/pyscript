from . import CompoundShapes


class LayeredShapes(CompoundShapes):

    def _get_shapes_postscript(self, center):
        return (shape._get_postscript(center) for shape in self._shapes)

    def _get_width(self):
        return max((shape._get_width() for shape in self._shapes), default=0)

    def _get_height(self):
        return max((shape._get_height() for shape in self._shapes), default=0)
