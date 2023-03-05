"""
Builds the record class.
"""

class Record:
    """
    Creates a class for each person.
    """

    def __init__(self, county, state, population, lfa_pop, income, \
        senior, vehicle_access):
        """
        Initialization method.
        """

        self.county = county
        self.state = state
        self.population = population
        self.lfa_pop = lfa_pop
        self.income = income
        self.senior = senior
        self.vehicle_access = vehicle_access

    def __str__(self):
        """
        Sets up the string return for the object.

        Parameters:
            none
        Returns:
            traits: (lst) list of traits
        """

        traits = [self.county, self.state, self.population, self.lfa_pop, \
            self.income, self.senior, self.vehicle_access]

        return str(traits)

    def get_county(self):
        """
        Gets the record's county.

        Parameters:
            none
        Returns:
            self.county: (str) county
        """

        return self.county

    def get_state(self):
        """
        Gets the record's state.

        Parameters:
            none
        Returns:
            self.state: (str) state
        """

        return self.state

    def get_population(self):
        """
        Gets the record's population.

        Parameters:
            none
        Returns:
            self.state: (int) population
        """

        return self.population

    def get_lfa_pop(self):
        """
        Gets the total number of people living more than 10 miles 
        from nearest supermarket.

        Parameters:
            none
        Returns:
            self.lfa_pop: (int) lfa_pop
        """

        return self.lfa_pop

    def get_income(self):
        """
        Gets the total number of low income people living more than
        10 miles from the nearest supermarket.

        Parameters:
            none
        Returns:
            self.income: (int) low income population
        """

        return self.income

    def get_senior(self):
        """
        Gets the total number of seniors living more than
        10 miles from the nearest supermarket.

        Parameters:
            none
        Returns:
            self.senior: (int) senior population
        """

        return self.senior

    def get_vehicle_access(self):
        """
        Gets the total number of households without vehicle access living 
        more than 10 miles from the nearest supermarket.

        Parameters:
            none
        Returns:
            self.vehicle_access: (int) vehicle_access
        """

        return self.vehicle_access

def main():
    """
    Main function for testing the class.

    For testing purposes.
    
    Parameters:
        none
    Returns:
        none
    """

    print("Testing")

if __name__ == "__main__": # For testing purposes
    main()