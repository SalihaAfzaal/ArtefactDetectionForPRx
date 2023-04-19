from plotting.comparing_prx import calculate_prx_for_comparison
from plotting.visualise_prx_comparison import plot_comparison
from data.generate_data import generate_data
import numpy as np

icp, abp = generate_data(3037511)

pr1, pr2, pr3 = calculate_prx_for_comparison(abp, icp, 100)
plot_comparison(pr1, pr2, pr3)

