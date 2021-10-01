from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """BoxWindow is an object of N dimension. In 1D, it can be represented by a range, in 2D a rectangle and in 3D a box"""

    def __init__(self, bounds):
        """This method initializes the box, thanks to the ranges of the box in parameter.

        bounds:
            bounds (list): list of ranges of the box in all the directions of the space.
        """
        self.bounds = np.array(bounds)

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [string]: Writing expression of the box with its bounds.
        """
        res = "BoxWindow: "
        for i in range(len(self.bounds) - 1):
            res = res + "["
            n = len(self.bounds[i])
            for j in range(n - 1):
                res = res + str(self.bounds[i][j]) + ", "
            res = res + str(self.bounds[i][n - 1]) + "] x "
        res = res + "["
        n = len(self.bounds[len(self.bounds) - 1])
        for j in range(n - 1):
            res = res + str(self.bounds[len(self.bounds) - 1][j]) + ", "
        res = res + str(self.bounds[len(self.bounds) - 1][n - 1]) + "]"
        return res

    def __len__(self):
        """Returns the number of dimension of the box"""
        return len(self.bounds)

    def __contains__(self, args):
        """Returns true if a point is contained in the box. The coordinates of the point are given in parameter.

        args:
            args (array): list of coordinates of the point
        """
        if len(args) != len(self.bounds):
            return False
        else:
            for i in range(len(args)):
                if args[i] <= self.bounds[i][0] or args[i] >= self.bounds[i][1]:
                    return False
        return True

    def dimension(self):
        """Returns the number of dimension of the box"""
        return len(self)

    def volume(self):
        """Returns the volume of the box"""
        res = self.bounds[0][1] - self.bounds[0][0]
        for i in range(1, len(self.bounds)):
            res = res * self.bounds[i][1] - self.bounds[i][0]
        return res

    def indicator_function(self, args):
        """[summary]

        Args:
            args ([type]): [description]
        """
        if self.__contains__(args):
            return 1
        else:
            return 0

    def rand(self, n, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): Number of points. Defaults to 1.
            rng ([type], optional): generator of a random number. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        liste_pts = []
        for j in range(n):
            l = []
            for i in range(len(self.bounds)):
                l.append(rng.uniform(self.bounds[i][0], self.bounds[i])[1])
            liste_pts.append(l)
        return np.array(liste_pts)

    def center(self):
        """Returns the coordinates of the center of the box"""
        l = []
        for i in range(len(self.bounds)):
            l.append(round((self.bounds[i][0] + self.bounds[i][1]) / 2, 2))
        return l


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        super(BoxWindow, self).__init__(args)
