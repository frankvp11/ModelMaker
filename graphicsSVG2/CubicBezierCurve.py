from math import comb

class CubicBezierCurve:
    def __init__(self, x0, y0, x1, y1, x2, y2, x3, y3, color='black', thickness=1):
        self.points = [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]
        self.color = color
        self.thickness = thickness

    def evaluate(self, t):
        x = sum(self._bezier_coeff(i, self.points[j][0], t) for i, j in enumerate(range(4)))
        y = sum(self._bezier_coeff(i, self.points[j][1], t) for i, j in enumerate(range(4)))
        return x, y

    def _bezier_coeff(self, i, p, t):
        n = 3
        return comb(n, i) * (1 - t) ** (n - i) * t ** i * p

    def to_svg(self, num_segments=100):
        step = 1 / num_segments
        path_data = 'M ' + ' '.join(map(str, self.points[0])) + ' C '
        for i in range(num_segments):
            t = (i + 1) * step
            x, y = self.evaluate(t)
            path_data += f'{x} {y} '
        return f'<path d="{path_data}" stroke="{self.color}" stroke-width="{self.thickness}" fill="none" />'
