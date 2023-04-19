from prx.interpolacni_metody.linearni_interpolace import spocitat_prx_doplnene_casti_interpolaci_linearni
from prx.interpolacni_metody.icm_pristup import spocitat_prx_odstranene_casti_ICM_pristup
from prx.interpolacni_metody.poly_interpolace_druheho_radu import vypocet_prx_doplnene_casti_poly_interpolace_2_rad

def calculate_prx_for_comparison(abp, icp, fs):
    pr1 = spocitat_prx_odstranene_casti_ICM_pristup(abp, icp, fs)
    pr2 = spocitat_prx_doplnene_casti_interpolaci_linearni(abp, icp, fs)
    pr3 = vypocet_prx_doplnene_casti_poly_interpolace_2_rad(abp, icp,fs)
    return pr1, pr2, pr3

