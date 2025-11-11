'''
the concrete implementations of strategy interface.
according to interface segration principle, each strategy class
implements only one algorithm.
'''

from interfaces import Strategy

class MaxStrategy(Strategy):
    ''' concrete strategy to find maximum in a list of numbers '''
    def execute(self, data):
        return max(data) if data else None
class MinStrategy(Strategy):
    ''' concrete strategy to find minimum in a list of numbers '''
    def execute(self, data):
        return min(data) if data else None
class SumStrategy(Strategy):
    ''' concrete strategy to calculate sum of a list of numbers '''
    def execute(self, data):
        return sum(data)
class MeanStrategy(Strategy):
    ''' concrete strategy to calculate mean of a list of numbers '''
    def execute(self, data):
        return sum(data) / len(data) if data else 0
class MedianStrategy(Strategy):
    ''' concrete strategy to calculate median of a list of numbers '''
    def execute(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 1:
            return sorted_data[n // 2]
        else:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
class ModeStrategy(Strategy):
    ''' concrete strategy to calculate mode of a list of numbers '''
    def execute(self, data):
        if not data:
            return None
        counts = {}
        for num in data:
            counts[num] = counts.get(num, 0) + 1
        max_count = max(counts.values())
        modes = [num for num, count in counts.items() if count == max_count]
        return modes[0] if len(modes) == 1 else modes
