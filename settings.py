# config.json will overwrite these settings,
# so these settings is not necessary.
# only config[args]==None will use below
from base.base_settings import *
from torch.optim.lr_scheduler import *
#----------------kwargs_optimizer-------------------
# kwargs_optimizer=sgd
kwargs_optimizer=adam
#---------------kwargs_lr_scheduler-----------------
# kwargs_lr_scheduler=cosinelr   #CosineAnnealingLR
kwargs_lr_scheduler=steplr     #StepLR
# kwargs_lr_scheduler=explr      #ExponentialLR
