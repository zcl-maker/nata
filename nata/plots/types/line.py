# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import Union

import numpy as np

from nata.plots.types import BasePlot


@dataclass
class LinePlot(BasePlot):
    ls: Optional[str] = None
    lw: Optional[Union[float, int]] = 1
    c: Optional[str] = None
    alpha: Optional[Union[float, int]] = None
    marker: Optional[str] = None
    ms: Optional[Union[float, int]] = None
    antialiased: Optional[bool] = True

    def _default_xlim(self):
        return (self.data.axes[0].min, self.data.axes[0].max)

    def _default_ylim(self):
        return (np.min(self.data.data), np.max(self.data.data))

    def _default_xlabel(self, units=True):
        return self.data.axes[0].get_label(units)

    def _default_ylabel(self, units=True):
        return self.data.get_label(units)

    def _default_title(self):
        return self.data.get_time_label()

    def _default_label(self):
        return self.data.get_label(units=False)

    def _xunits(self):
        return f"${self.data.axes[0].units}$"

    def _yunits(self):
        return f"${self.data.units}$"

    def build_canvas(self):
        # get plot axes and data
        x = self.data.axes[0].data
        y = self.data.data

        # build plot
        self.h = self.axes.ax.plot(
            x,
            y,
            ls=self.ls,
            lw=self.lw,
            c=self.c,
            alpha=self.alpha,
            marker=self.marker,
            ms=self.ms,
            label=self.label,
            antialiased=self.antialiased,
        )

    @classmethod
    def style_attrs(cls) -> List[str]:
        return [
            "ls",
            "lw",
            "c",
            "alpha",
            "marker",
            "ms",
            "antialiased",
        ] + BasePlot.style_attrs()