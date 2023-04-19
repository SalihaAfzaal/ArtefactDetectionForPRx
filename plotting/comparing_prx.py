from prx.interpolacni_metody.linearni_interpolace import spocitat_prx_doplnene_casti_interpolaci_linearni
from prx.interpolacni_metody.icm_pristup import spocitat_prx_odstranene_casti_ICM_pristup
from prx.interpolacni_metody.poly_interpolace_druheho_radu import vypocet_prx_doplnene_casti_poly_interpolace_2_rad

def calculate_prx_for_comparison(abp, icp, fs):
    """
    Vypočítá tři různé metody indexu periferního odporu (PRx) pro srovnání.

    Args:
    abp (numpy.ndarray): Pole hodnot arteriálního krevního tlaku (ABP).
    icp (numpy.ndarray): Pole hodnot intrakraniálního tlaku (ICP).
    fs (float): Vzorkovací frekvence signálů ABP a ICP v Hz.

    Vrácení:
    Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]: N-tice obsahující tři pole hodnot PRx
    vypočítané pomocí různých metod: PRx s odstraněnými pomalými oscilacemi (PRx_ICM),
    PRx s lineární interpolací chybějících dat (PRx_Linear) a PRx s polynomickou interpolací druhého řádu chybějících dat (PRx_Poly).

    Error:
    TypeError: Pokud abp a icp nejsou numpy ndarrays nebo pokud fs není float.
    ValueError: Pokud abp a icp mají různé délky nebo pokud fs není větší než nula.
    """
    pr1 = spocitat_prx_odstranene_casti_ICM_pristup(abp, icp, fs)
    pr2 = spocitat_prx_doplnene_casti_interpolaci_linearni(abp, icp, fs)
    pr3 = vypocet_prx_doplnene_casti_poly_interpolace_2_rad(abp, icp,fs)
    return pr1, pr2, pr3

