from statistics import mean


class Correlations:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _sum_of_squares(self, arr):
        average = mean(arr)
        return sum(pow(i - average, 2) for i in arr)

    def _cov(self):
        mean_x = mean(self.x)
        mean_y = mean(self.y)
        return sum((self.x[i] - mean_x) * (self.y[i] - mean_y) for i in range(len(self.x)))

    def t_student(self):
        len_x = len(self.x)
        len_y = len(self.y)
        sum_sqr_x = self._sum_of_squares(self.x)
        sum_sqr_y = self._sum_of_squares(self.y)
        if len_x != len_y:
            S = pow((len_x + len_y) / len_y * len_x, 0.5) * pow(
                (sum_sqr_x + sum_sqr_y) / (len_x + len_y - 2), 0.5)
        else:
            S = pow((sum_sqr_x + sum_sqr_y) / (len_x - 1) / len_x, 0.5)

        return abs(mean(self.x) - mean(self.y)) / S

    def r_pearson(self):
        if len(self.x) == len(self.y):
            sum_sqr_x = self._sum_of_squares(self.x)
            sum_sqr_y = self._sum_of_squares(self.y)
            return self._cov() / pow(sum_sqr_x * sum_sqr_y, 0.5)


if __name__ == "__main__":
    pass
