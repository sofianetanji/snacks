BEST_VALUES = {}

N_SAMPLES = {}

BEST_VALUES["a9a"] = [800, 0.01, 1e-5, int(8e6)]
N_SAMPLES["a9a"] = 32561

BEST_VALUES["ijcnn1"] = [5000, 2., 1e-8, int(8e7)]
N_SAMPLES["ijcnn1"] = 49990

BEST_VALUES["SUSY"] = [500, 1e-2, 1e-7, int(8e7)]
N_SAMPLES["SUSY"] = 5e6

BEST_VALUES["HIGGS"] = [5000, 0.02,  1e-8, 1050000]
N_SAMPLES["HIGGS"] = 11e6

BEST_VALUES["mnist"] = [1000, 0.002, 1/(100*60000), int(5e6)]
N_SAMPLES["mnist"] = 60000

BEST_VALUES["SVHN"] = [10000, 5.45, 1e-8, int(8e6)]
N_SAMPLES["SVHN"] = 73257

BEST_VALUES["epsilon"] = [3000, 7e-6, 1e-8, 1050000]
N_SAMPLES["epsilon"] = 400000

BEST_VALUES["url"] = [1500, 5e-4, 3e-6, 1050000]
N_SAMPLES["url"] = 2396130

# not considered anymore
BEST_VALUES["real-sim"] = [6000, 5e-1, 1e-7, 1050000]
N_SAMPLES["real-sim"] = 72309

BEST_VALUES["news20.binary"] = [5500, 5e-1, 1e-8, 245000]
N_SAMPLES["news20.binary"] = 19996

BEST_VALUES["covtype.binary"] = [3000, 1/(100*581012),  1e-8, 1050000]
N_SAMPLES["covtype.binary"] = 581012

BEST_VALUES["rcv1.binary_test"] = [1000, 5e-3, 1e-8, 90000]
N_SAMPLES["rcv1.binary_test"] = 677399
