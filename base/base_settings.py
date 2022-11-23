adam={
    'lr':1e-3,
    "weight_decay": 0,
    # "weight_decay": 0.01,
    'betas':(0.9, 0.999),
    "amsgrad": True,
    'eps':1e-8
}
"""
Implements Adam algorithm.

For further details regarding the algorithm we refer to Adam: A Method for Stochastic Optimization_.

Args:
    params (iterable): iterable of parameters to optimize or dicts defining
        parameter groups
    lr (float, optional): learning rate (default: 1e-3)
    betas (Tuple[float, float], optional): coefficients used for computing
        running averages of gradient and its square (default: (0.9, 0.999))
    eps (float, optional): term added to the denominator to improve
        numerical stability (default: 1e-8)
    weight_decay (float, optional): weight decay (L2 penalty) (default: 0)
    amsgrad (boolean, optional): whether to use the AMSGrad variant of this
        algorithm from the paper On the Convergence of Adam and Beyond_
        (default: False)
    foreach (bool, optional): whether foreach implementation of optimizer
        is used (default: None)
    maximize (bool, optional): maximize the params based on the objective, instead of
        minimizing (default: False)
    capturable (bool, optional): whether this instance is safe to capture in a CUDA graph.
        Passing True can impair ungraphed performance, so if you don't intend to
        graph capture this instance, leave it False (default: False)
"""
sgd={
    'lr':1e-3,
    'momentum':0.9,
}
"""
params (iterable): iterable of parameters to optimize or dicts defining
Implements stochastic gradient descent (optionally with momentum).
Nesterov momentum is based on the formula from On the importance of initialization and momentum in deep learning__.

Args:
    params (iterable): iterable of parameters to optimize or dicts defining
        parameter groups
    lr (float): learning rate 
    momentum (float, optional): momentum factor (default: 0) 
    weight_decay (float, optional): weight decay (L2 penalty) (default: 0) 
    dampening (float, optional): dampening for momentum (default: 0) 
    nesterov (bool, optional): enables Nesterov momentum (default: False)
    maximize (bool, optional): maximize the params based on the objective, instead of
        minimizing (default: False)
    foreach (bool, optional): whether foreach implementation of optimizer
        is used (default: None)
"""
#-------------------------------lr_schedule-------------------------------
cosinelr={
    'T_max':20,
    'eta_min':1e-4,
}
"""
Args:
    T_max (int): Maximum number of iterations. 
    eta_min (float): Minimum learning rate. Default: 0. 
    last_epoch (int): The index of last epoch. Default: -1.
    verbose (bool): If True, prints a message to stdout for
        each update. Default: False.
"""
steplr={
    'step_size':50,
    'gamma':0.5,
}
"""
Args:
    optimizer (Optimizer): Wrapped optimizer.
    step_size (int): Period of learning rate decay.
    gamma (float): Multiplicative factor of learning rate decay.
"""
explr={
    'gamma':0.5,
}
"""
Args:
    optimizer (Optimizer): Wrapped optimizer.
    gamma (float): Multiplicative factor of learning rate decay. last_epoch (int): The index of last epoch. Default: -1.
    verbose (bool): If True, prints a message to stdout for each update. Default: False.
"""