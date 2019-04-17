from abc import abstractmethod

from . import Shape, Point


class CompoundShapes(Shape):
    def __init__(self, *shapes):
        self._shapes = shapes

    def _get_postscript(self, center):
        return "\n".join(self._get_shapes_postscript(center))

    @abstractmethod
    def _get_shapes_postscript(self, center):
        pass
