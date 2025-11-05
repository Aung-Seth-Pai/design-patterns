from interfaces import Strategy

class Context:
    def __init__(self, strategy: Strategy = None):
        ''' constructor takes an initial Strategy to use '''
        self._strategy: Strategy = strategy if strategy else None

    def set_strategy(self, strategy: Strategy):
        ''' allows changing to a different strategy at runtime '''
        self._strategy = strategy

    def execute_strategy(self, data):
        ''' execute the selected strategy's algorithm '''
        if not self._strategy:
            raise ValueError("Strategy not set")
        return self._strategy.execute(data)
    