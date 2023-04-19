import time
import numpy as np
import pandas as pd
from prx.prx_calculation import calculate_pearsonr
from chunking_signal.windows_and_mean import get_windows, counting_mean

def vypocet_prx_doplnene_casti_poly_interpolace_2_rad(art, icp, fs):
    """
        Modul pro výpočet Pearsonova korelačního koeficientu pomocí lineární interpolace mezi polemi arteriálního tlaku (ART) a intrakraniálního tlaku (ICP), která jsou převzorkována.

        Funkce:
        - vypocet_prx_doplnene_casti_poly_interpolace_2_rad(art, icp, meaned_window_size, fss): Vypočítá Pearsonův korelační koeficient pomocí lineární interpolace nad průměrem oken délky 'meaned_window_size' pro signály ART a ICP po odstranění NaN hodnot a odlehlých hodnot. Frekvence vzorkování signálů je 'fss'. Vrátí pole korelačních koeficientů.

        Parametry:
        - art (array-like): Pole dat arteriálního tlaku.
        - icp (array-like): Pole dat intrakraniálního tlaku.
        - meaned_window_size (int): Velikost okna pro výpočet průměru převzorkovaných dat.
        - fss (int): Frekvence vzorkování dat.

        Návratová hodnota:
        - pr (array-like): Pole Pearsonových korelačních koeficientů.
        """
    start_time = time.time()
    df_art = pd.DataFrame({'ART': art})
    df_icp = pd.DataFrame({'ICP': icp})

    # Apply NaN values to out-of-range values
    df_art.loc[(df_art['ART'] < 0) | (df_art['ART'] > 250), 'ART'] = np.nan
    df_icp.loc[(df_icp['ICP'] < -10) | (df_icp['ICP'] > 150), 'ICP'] = np.nan

    art = df_art['ART']
    icp = df_icp['ICP']

    art_series = pd.Series(art)
    icp_series = pd.Series(icp)

    art = art_series.interpolate(method="polynomial", order=2)
    icp = icp_series.interpolate(method="polynomial", order=2)

    downelimi_art = get_windows(art, fs)
    downelimi_icp = get_windows(icp, fs)

    meaned_art = counting_mean(downelimi_art)
    meaned_icp = counting_mean(downelimi_icp)

    seq_art = meaned_art[1:fs*10]
    seq_icp = meaned_icp[1:fs*10]

    seq_art_for_prx = ([seq_art[i: i + 30] for i in range(0, len(seq_art), 6)])
    seq_icp_for_prx = ([seq_icp[i: i + 30] for i in range(0, len(seq_icp), 6)])

    ar = [[np.round(float(i), 2) for i in nested]
          for nested in np.asarray(seq_art_for_prx, dtype='object')]
    ic = [[np.round(float(i), 2) for i in nested]
          for nested in np.asarray(seq_icp_for_prx, dtype='object')]

    pr = calculate_pearsonr(ar, ic)

    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time polynom 2 stupne:", execution_time, "seconds")

    return pr