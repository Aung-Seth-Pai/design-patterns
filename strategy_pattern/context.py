from interfaces import Strategy

class Context:
    ''' Context class to use different strategies '''
    def __init__(self, strategy: Strategy = None):
        ''' constructor needs an initial strategy'''
        self._strategy: Strategy = strategy if strategy else None

    def set_strategy(self, strategy: Strategy):
        ''' by using this method, client can change strategy at runtime '''
        self._strategy = strategy

    def execute_strategy(self, data):
        ''' execute the current strategy's algorithm  '''
        if not self._strategy:
            raise ValueError("Strategy not set")
        return self._strategy.execute(data)
    