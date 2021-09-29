from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """[summary]"""

    def __init__(self, args):
        """[summary]

        Args:
            args ([type]): [description]
        """
        self.bounds = np.array(args)

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [type]: [description]
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
        return len(self.bounds)

    def __contains__(self, args):
        if len(args) != len(self.bounds):
            return False
        else:
            for i in range(len(args)):
                if args[i] <= self.bounds[i][0] or args[i] >= self.bounds[i][1]:
                    return False
        return True

    def dimension(self):
        """[summary]"""
        return len(self)

    def volume(self):
        """[summary]"""
        res = self.bounds[0][1] - self.bounds[0][0]
        for i in range(1, len(self.bounds)):
            res = res * self.bounds[i][1] - self.bounds[i][0]
        return res

    def indicator_function(self, args):
        """[summary]

        Args:
            args ([type]): [description]
        """
        return

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        return


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        super(BoxWindow, self).__init__(args)
