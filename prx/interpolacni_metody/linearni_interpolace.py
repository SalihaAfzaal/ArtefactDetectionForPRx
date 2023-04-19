import time
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from prx.prx_calculation import calculate_pearsonr
from chunking_signal.windows_and_mean import get_windows, counting_mean

def spocitat_prx_doplnene_casti_interpolaci_linearni(art,icp,fs):
        """
        Vypočítejte Pearsonův korelační koeficient mezi dvěma poli převzorkovaného a interpolovaného arteriálního tlaku
        (ART) a data intrakraniálního tlaku (ICP) pomocí lineární interpolace.

        Args:
        - art (array-like): Pole dat arteriálního tlaku.
        - icp (jako pole): Pole údajů o intrakraniálním tlaku.
        - meaned_window_size (int): Velikost okna pro výpočet průměru převzorkovaných dat.
        - fss (int): Frekvence vzorkování dat.

        Vrácení:
        - pr1 (pole): Pole Pearsonových korelačních koeficientů.

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

        art = art_series.interpolate()
        icp = icp_series.interpolate()

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
        print("Execution time linearni interpolace:", execution_time, "seconds")
        return pr