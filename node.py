class Node:    
    def __init__(self, cpt, name, distribution='discrete'):
        self.__cpt = cpt
        self.__name = name
        self.__distribution = distribution

    def get_cpt(self):
        return self.__cpt
    
    def get_name(self):
        return self.__name
    
    def get_distribution(self):
        return self.__distribution

    def __str__(self):
        return self.__name
    
    def __repr__(self):
        return self.__name