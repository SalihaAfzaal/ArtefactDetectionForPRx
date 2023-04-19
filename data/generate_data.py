import numpy as np

def generate_data(size=3037511):
    """
    Generujte simulovaná data pro arteriální krevní tlak (ABP) a intrakraniální tlak (ICP).

    Args:
    size (int, volitelné): Počet datových bodů, které se mají vygenerovat. Výchozí hodnota je 3037511.

    Vrácení:
    Nice dvou polí NumPy:
    abp (ndarray): Simulovaná data ABP.
    icp (ndarray): Simulovaná data ICP.

    Vygenerovaná data jsou simulována pomocí normálních rozdělení se střední hodnotou a standardní odchylkou.
    Vygenerovaná pole také obsahují některé uměle vložené chybějící hodnoty (-9999) pro simulaci chybějících dat.
    """

    abp = np.random.normal(loc=100, scale=20, size=size)
    icp = np.random.normal(loc=10, scale=5, size=size)

    abp[np.random.choice(abp.size, size=500, replace=False)] = -9999
    icp[np.random.choice(icp.size, size=1000, replace=False)] = -9999

    return abp, icp
