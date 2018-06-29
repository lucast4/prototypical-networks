import prototypical_networks.protonets.data

def load(opt, splits):
    if opt['data.dataset'] == 'omniglot':
        ds = prototypical_networks.protonets.data.omniglot.load(opt, splits)
    else:
        raise ValueError("Unknown dataset: {:s}".format(opt['data.dataset']))

    return ds
