"""
Calculate Data Coverage

Meteorological data provided by Meteostat (https://dev.meteostat.net)
under the terms of the Creative Commons Attribution-NonCommercial
4.0 International Public License.

The code is licensed under the MIT license.
"""

from copy import copy

def coverage(
    self,
    parameter: str = None
) -> float:
    """
    Calculate data coverage (overall or by parameter)
    """

    if parameter is None:
        return len(self.data.index) / self.expected_rows()

    return self.data[parameter].count() / self.expected_rows()
