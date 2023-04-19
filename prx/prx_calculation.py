from scipy.stats import pearsonr
def calculate_pearsonr(ar, ic):
    """
    Vypočítá Pearsonovy korelační koeficienty mezi dvěma poli 'ar' a 'ic'
    pomocí funkce 'pearsonr' z modulu 'scipy.stats'.

    Parametry:
    - ar (jako pole): Pole dat ART.
    - ic (jako pole): Pole ICP dat.

    Vrácení:
    - pr (seznam): Seznam Pearsonových korelačních koeficientů mezi dvěma poli.
    """
    pr = [pearsonr(f, b)[0] for f, b in zip(ar, ic)]
    return pr
