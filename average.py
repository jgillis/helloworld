class Averager:
    """

    This class computes the average of all the samples that you add to it.

	Examples:
	  >>> avg = Averager()
	  >>> avg.add(12)
	  >>> avg.add(14)
	  >>> print avg()
	  13.0
	  
	  >>> avg = Averager()
	  >>> avg.add(2)
	  >>> avg.add(3)
	  >>> print avg()
	  2.5
	  
    """
    def __init__(self):
        """
        Initializer
        """
        self.mylist = []

    def add(self,n):
        """
        Add a single sample

        Args:
          n (number): the sample to add
        """
        self.mylist.append(n)

    def __call__(self):
        """
        Returns the average of all samples
        """
        return float(sum(self.mylist))/self.N

    @property
    def N(self):
        return len(self.mylist)-1

if __name__ == '__main__':
  # Demonstration
  avg = Averager()
  avg.add(12)
  avg.add(14)
  print avg()
