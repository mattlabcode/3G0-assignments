import numpy
import autograd

# import statement for autograd wrapped numpy
import autograd.numpy as np   
# import statment for gradient calculator
from autograd import grad  



# random search function
def random_search(g,alpha_choice,max_its,w,num_samples):
    # run random search
    w_history = []         # container for w history
    cost_history = []           # container for corresponding cost function history
    alpha = 0
    for k in range(1,max_its+1):
        # check if diminishing steplength rule used
        if alpha_choice == 'diminishing':
            alpha = 1/float(k)
        else:
            alpha = alpha_choice

    return (w_history,cost_history)

print(random_search(1,.5,10,22,199))