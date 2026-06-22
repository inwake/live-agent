from .bridge import AbletonLiveBridge


def create_instance(c_instance):
    return AbletonLiveBridge(c_instance)
