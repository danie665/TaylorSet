class DescriptiveStats():

    """ a simple descriptive statistics model """

    def __init__(self, data_1=[], data_2=[], data_3=[], data_4=[], data_5=[]):
        """ initialize data """
        self.data_1 = data_1
        self.data_1 = [float(x) for x in self.data_1]
        self.data_2 = data_2
        self.data_2 = [float(x) for x in self.data_2]
        self.data_3 = data_3
        self.data_3 = [float(x) for x in self.data_3]
        self.data_4 = data_4
        self.data_4 = [float(x) for x in self.data_4]
        self.data_5 = data_5
        self.data_5 = [float(x) for x in self.data_5]

    def _lists_uniform(self):
        """ ensures that input lists are the same length """
        length = len(self.data_1)
        if (
                (len(self.data_2) == length or len(self.data_2) == 0) and
                (len(self.data_3) == length or len(self.data_3) == 0) and
                (len(self.data_4) == length or len(self.data_4) == 0) and
                (len(self.data_5) == length or len(self.data_5) == 0)
            ):
            return True
        return False

    def mean(self, data=[]):
        """ returns the arithmetic mean of an array """
        if len(data) == 0:
            return sum(data) / len(data)
        else:
            return sum(data) / len(data)

    def median(self, data=[]):
        """ returns the median of an array """
        sorted_array = sorted(data)
        if len(sorted_array) % 2 == 0:
            lower = int( ( len(sorted_array) / 2 ) )
            upper = int( ( len(sorted_array) / 2 ) + 1 )
            return ( sorted_array[lower-1] + sorted_array[upper-1] ) / 2
        else:
            place = int( ( len(sorted_array) + 1 ) / 2 )
            return sorted_array[place-1]

    def mode(self, data=[]):
        """ return the mode of the data """
        tally_dict = {}
        i = 0
        while i < len(data):
            if data[i] in tally_dict:
                tally_dict[data[i]] += 1
            else:
                tally_dict[data[i]] = 1
            i += 1
        max_occ = 0
        for key, value in tally_dict.items():
            if value > max_occ:
                max_occ = value
        modes = []
        for key, value in tally_dict.items():
            if value == max_occ:
                modes.append(key)
        if len(modes) == 1:
            return modes[0]
        else:
            return modes

    def range(self, data=[]):
        """ return the range of the data """
        return max(data) - min(data)

    def weighted_mean(self):
        """ returns weighted mean from an array of arrays """
        if not _lists_uniform():
            raise ValueError
        return 0

    def geometric_mean(self, data=[]):
        """ returns geometic mean of an array """
        my_product = 1
        i = 0
        while i < len(data):
            my_product *= data[i]
            i += 1
        return my_product ** ( 1 / len(data) )

    def percentile(self, percentile, data=[]):
        """ returns the percentile location of an array """
        sorted_array = sorted(data)
        location = ( len(sorted_array) + 1 ) * percentile
        lower = int(location) - 1
        upper = int(location)
        mid_distance = location - int(location)
        return ( sorted_array[lower] +
                (( sorted_array[upper] - sorted_array[lower] ) * mid_distance ) )

    def interquartile_range(self, data=[]):
        """ returns the interquartile range of an array """
        return self.percentile(.75, data=data) - self.percentile(.25, data=data)

    def population_variance(self, data=[]):
        """ returns population variance of an array """
        my_mean = self.mean(data=data)
        my_sum = 0
        i = 0
        while i < len(data):
            my_sum += ( data[i] - my_mean ) ** 2
            i += 1
        return my_sum / len(data)

    def sample_variance(self, data=[]):
        """ returns sample variance of an array """
        my_mean = self.mean(data=data)
        my_sum = 0
        i = 0
        while i < len(data):
            my_sum += ( data[i] - my_mean ) ** 2
            i += 1
        return my_sum / ( len(data) - 1 )

    def population_skewness(self, data=[]):
        """ returns population skewness of an array """
        my_mean = self.mean(data=data)
        my_std = self.population_standard_deviation(data=data)
        my_sum = 0
        i = 0
        while i < len(data):
            my_sum += ( data[i] - my_mean ) ** 3
            i += 1
        return my_sum / (len(data) * my_std ** 3)

    def sample_skewness(self, data=[]):
        """ returns sample skewness of an array """
        my_mean = self.mean(data=data)
        my_std = self.sample_standard_deviation(data=data)
        my_sum = 0
        i = 0
        while i < len(data):
            my_sum += ( ( data[i] - my_mean ) / my_std ) ** 3
            i += 1
        return ( len(data) / ( (len(data) - 1) * (len(data) - 2) ) ) * my_sum

    def population_kurtosis(self, data=[]):
        """ returns population kurtosis of an array """
        my_mean = self.mean(data=data)
        my_sum = 0
        my_sum_two = 0
        i = 0
        while i < len(data):
            my_sum += (data[i] - my_mean) ** 4
            my_sum_two += (data[i] - my_mean) ** 2
            i += 1
        return my_sum / my_sum_two ** 2

    def sample_kurtosis(self, data=[]):
        """ returns sample kurtosis of an array """
        my_mean = self.mean(data=data)
        my_std = self.sample_standard_deviation(data=data)
        my_sum = 0
        i = 0
        while i < len(data):
            my_sum += ( (data[i] - my_mean) / my_std ) ** 4
            i += 1
        my_coef = (len(data)*(len(data)+1)) / (
            (len(data)-1)*(len(data)-2)*(len(data)-3)
        )
        return my_coef * my_sum

    def sample_excess_kurtosis(self, data=[]):
        """ returns sample kurtosis of an array """
        my_mean = self.mean(data=data)
        my_std = self.sample_standard_deviation(data=data)
        my_sum = 0
        i = 0
        while i < len(data):
            my_sum += ( (data[i] - my_mean) / my_std ) ** 4
            i += 1
        my_coef = (len(data)*(len(data)+1)) / (
            (len(data)-1)*(len(data)-2)*(len(data)-3)
        )
        my_standardizer = (3*(len(data)-1)**2) / ((len(data)-2)*(len(data)-3))
        return my_coef * my_sum - my_standardizer

    def population_standard_deviation(self, data=[]):
        """ returns the population standard deviation of an array """
        return self.population_variance(data=data) ** 0.5

    def sample_standard_deviation(self, data=[]):
        """ returns the sample standard deviation of an array """
        return self.sample_variance(data=data) ** 0.5

    def population_coefficient_of_variation(self, data=[]):
        """ returns the population coefficient of variation of an array """
        return self.population_standard_deviation(data=data) / self.mean(data=data)

    def sample_coefficient_of_variation(self, data=[]):
        """ returns the sample coefficient of variation of an array """
        return self.sample_standard_deviation(data=data) / self.mean(data=data)

    def population_z_score(self, position, data=[]):
        """ returns the population z-score of an element in an array """
        return ( ( data[position] - self.mean(data=data) ) / 
                    self.population_standard_deviation(data=data) )

    def sample_z_score(self, position, data=[]):
        """ returns the sample z-score or an element in a list """
        return ( ( data[position] - self.mean(data=data) ) / 
                    self.sample_standard_deviation(data=data) )

    def sample_covariance(self, data_1=[], data_2=[]):
        """ returns the sample covariance of an array """
        if not self._lists_uniform():
            raise ValueError
        mean_1 = self.mean(data=data_1)
        mean_2 = self.mean(data=data_2)
        covariance = 0
        i = 0
        while (i < len(data_1)):
            covariance += ( data_1[i] - mean_1 ) * ( data_2[i] - mean_2 )
            i += 1
        return covariance / ( len(data_1) - 1)

    def population_covariance(self, data_1=[], data_2=[]):
        """ returns the population covariance of an array """
        if not self._lists_uniform():
            raise ValueError
        mean_1 = self.mean(data=data_1)
        mean_2 = self.mean(data=data_2)
        covariance = 0
        i = 0
        while (i < len(data_1)):
            covariance += ( data_1[i] - mean_1 ) * ( data_2[i] - mean_2 )
            i += 1
        return covariance / len(data_1)

    def simple_linear_regression(self, data_1=[], data_2=[]):
        """ returns linear regression of the first array regressed on the second array """
        """ TODO: Expand to multiple linear regression """
        mean_1 = self.mean(data=data_1)
        mean_2 = self.mean(data=data_2)
        i = 0
        beta = self.population_covariance(data_1, data_2) / self.population_variance(data_2)
        alpha = mean_1 - beta * mean_2
        return [alpha, beta]

