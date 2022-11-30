# config.json will overwrite these settings,
# so these settings is not necessary.
# only config[args]==None will use below

#----------------kwargs_optimizer-------------------
SGD_args={
    'lr':1e-3,
    'momentum':0.9,
}
Adam_args={
    'lr':1e-3,
    "weight_decay": 0,
    # "weight_decay": 0.01,
    'betas':(0.9, 0.999),
    # (Tuple[float, float], optional): coefficients used for computing
    # running averages of gradient and its square (default: (0.9, 0.999))
    "amsgrad": True,
    'eps':1e-8
    
}
#---------------kwargs_lr_scheduler-----------------
CosineAnnealingLR_args={
    'T_max':20,
    'eta_min':1e-4,
}   #CosineAnnealingLR
StepLR_args={
    'step_size':50,
    'gamma':0.5,
}     #StepLR
ExponentialLR_args={
    'gamma':0.5,
}     #ExponentialLR
