from statistics import mean

"""
Tento modul poskytuje funkce pro zpracování signálu v oknech zadané délky a výpočet průměru každého okna.

Funkce:
- get_windows: Rozdělí signál do oken zadané délky
- counting_mean: Vypočítá průměr každého okna v seznamu oken


Příklad použití:
    signál = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    window_length = 3
    windows = get_windows(signál, window_length)  # Vrací [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    means = counting_mean(windows)  # Vrací [2.0, 5.0, 8.0, 10.0]
"""

def get_windows(signal, window_length):
    """
        Rozdělí signál do oken zadané délky.

        Args:
            signál: Seznam nebo 1D pole hodnot signálu.
            window_length: Délka každého okna.

        Vrácení:
            Seznam oken, kde každé okno je seznam nebo 1D pole hodnot signálu.
     """
    return [signal[i:i + window_length] for i in range(0, len(signal), window_length)]

def counting_mean(signal_into_windows):
    """
        Vypočítá průměr každého okna v seznamu oken.

        Args:
            okna: Seznam oken, kde každé okno je seznam nebo 1D pole hodnot signálu.

        Vrácení:
            Seznam středních hodnot, kde každá hodnota odpovídá průměru okna.
        """
    return [mean(window) for window in signal_into_windows]
