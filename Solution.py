from Marriage import Marriage

import itertools


class Solution:

    def __init__(self, number, women, men):
        """
        The constructor exists only to initialize variables. You do not need to change it.
        :param number: The number of members
        :param men: The preference list of men, as a dictionary.
        :param women: The preference list of the women, as a dictionary.
        """
        self.num = number
        self.men = men
        self.women = women
        self.count = 0
        self.stable_matchings = []

    def output_stable_matchings(self):

        #marriage = Marriage(3,)

        #a = itertools.permutations()

        print(self.women)

        all_perfect_matching = []

        #Creates all permutations of perfect matchings
        for i in list(itertools.permutations(range(1,self.num+1),self.num)):
            perfect_matching = []
            numm = 1
            for j in i:
                if(numm < self.num+1):
                    perfect_matching.append((numm,j))
                    numm += 1        
            for match in perfect_matching:
                #prefference is the index of the matched man in the woman prefference list
                #if not zero it means there are men the woman preffers
                #Basically checks if any more preffered men exist in her list
                prefference = (self.woman[match[0]]).index(match[1])
                while(prefference != 0):
                    #looks for the match where the man is
                    for man_match in perfect_matching:
                        #if the match is equal to the prefference then
                        if(man_match[1] == prefference):
                            #Check the index of both women (original match and man's own match)
                            #If original match is higher, then relation is unstable.f
                            if((self.man[man_match[1]]).index(man_match[0]) > (self.man[man_match[1]]).index(match[1])):

                #Checks index of the woman looking for better match in men prefference list
                #We want to check if it's index is higher or lower than the one from the man's matched woman



        #all_perfect_matching.append(perfect_matching)
                

        #print(all_perfect_matching)

        
        
        #print(list(itertools.permutations("ABC",2)))

        #print(list(itertools.permutations(range(value),3))))


        #for key, value in self.women.items():
            #for key, value in self.men.items():
            #perfect_matching.append(list(itertools.permutations(range(1,4),2)))

        #print(perfect_matching)


        """
        This method both computes and returns the stable matchings
        :return: the list of stable matchings   
        """

        return self.stable_matchings
