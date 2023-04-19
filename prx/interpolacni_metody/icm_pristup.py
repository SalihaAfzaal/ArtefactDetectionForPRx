import time
import numpy as np
import pandas as pd
from prx.prx_calculation import calculate_pearsonr
from chunking_signal.windows_and_mean import get_windows, counting_mean

def spocitat_prx_odstranene_casti_ICM_pristup(art, icp, fs):
    """
    #     Spočítá korelační koeficient mezi signály ICP a ART po odstranění artefaktů pomocí metody ICM+.
    #
    #     Parametry:
    #     -----------
    #     art: list nebo ndarray
    #         Signál ART
    #     icp: list nebo ndarray
    #         Signál ICP
    #     meaned_window_size: int
    #         Počet vzorků pro výpočet průměru signálu
    #     fss: int
    #         Frekvence vzorkování signálu v Hz
    #
    #     Návratová hodnota:
    #     -------------------
    #     pr1: list
    #         Korelační koeficient mezi signály ICP a ART
    #
    #     """
    start_time = time.time()

    df_art = pd.DataFrame({'ART': art})
    df_icp = pd.DataFrame({'ICP': icp})

    # Apply NaN values to out-of-range values
    df_art.loc[(df_art['ART'] < 0) | (df_art['ART'] > 250), 'ART'] = np.nan
    df_icp.loc[(df_icp['ICP'] < -10) | (df_icp['ICP'] > 150), 'ICP'] = np.nan

    downelimi_art = get_windows(art, fs)
    downelimi_icp = get_windows(icp, fs)

    meaned_art = counting_mean(downelimi_art)
    meaned_icp = counting_mean(downelimi_icp)

    print('Length of meaned signals should be:', len(meaned_art))

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
    print("Execution time icm+:", execution_time, "seconds")

    return pr
