# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:23:05 2020

@author: abm
"""
print("\n\t\tKNOW YOUR CHARACTER BASED ON BIRTH MONTH")
print("\t\t==== ==== ========= ===== == ===== =====")
next = True
while next == True:
    s = input(str("Enter your BIRTH month: ") )
    
    if s.lower() == 'january' or s.lower() == 'jan' :
        print("\n People born in JANUARY are BOLD and ALERT")
        print("\t                  ------------- ")
        print("\tYour Birth GEM is |' GARNET ' |")
        print("\t                  ------------- ")
        
    elif s.lower() == 'february' or s.lower() == 'feb' :
        print("\n People born in FEBRUARY are LUCKY and LOYAL")
        print("\t                  --------------")
        print("\tYour Birth GEM is |' AMETHYST '| ")
        print("\t                  --------------")
        
    elif s.lower() == 'march' or s.lower() == 'mar' :
        print("\n People born in MARCH are NAUGHTY and GENIUS")
        print("\t                  ----------------")
        print("\tYour Birth GEM is |' AQUAMARINE '| ")
        print("\t                  ----------------")
        
    elif s.lower() == 'april' or s.lower() == 'apr' :
        print("\n People born in APRIL are CARING and STRONG")
        print("\t                  -------------")
        print("\tYour Birth GEM is |' DIAMOND '| ")
        print("\t                  -------------")
        
    elif s.lower() == 'may' :
        print("\n People born in MAY are LOVING and PRACTICAL")
        print("\t                  ------------")
        print("\tYour Birth GEM is |'EMERALD '| ")
        print("\t                  ------------")
        
    elif s.lower() == 'june' or s.lower() == 'jun' :
        print("\n People born in JUNE are ROMANTIC and CURIOUS")
        print("\t                  -----------------")
        print("\tYour Birth GEM is |' ALEXANDRITE '| ")
        print("\t                  -----------------")
        
    elif s.lower() == 'july' or s.lower() == 'jul' :
        print("\n People born in JULY are ADVENTUROUS and HONEST")
        print("\t                  ----------")
        print("\tYour Birth GEM is |' RUBY '|")
        print("\t                  ----------")
        
    elif s.lower() == 'august' or s.lower() == 'aug' :
        print("\n People born in AUGUST are ACTIVE and HARDWORKING")
        print("\t                  -------------")
        print("\tYour Birth GEM is |' PERIDOT '| ")
        print("\t                  -------------")
        
    elif s.lower() == 'september' or s.lower() == 'sep' :
        print("\n People born in SEPTEMBER are SENSITIVE and PRETTY")
        print("\t                  --------------")
        print("\tYour Birth GEM is |' SAPPHIRE '| ")
        print("\t                  --------------")
        
    elif s.lower() == 'october' or s.lower() == 'oct' :
        print("\n People born in OCTOBER are STYLISH and FRIENDLY")
        print("\t                  ----------------  ")
        print("\tYour Birth GEM is |' TOURMALINE '| ")
        print("\t                  ----------------  ")
        
    elif s.lower() == 'november' or s.lower() == 'nov' :
        print("\n People born in NOVEMBER are NICE and CREATIVE")
        print("\t                  -------------")
        print("\tYour Birth GEM is |' CITRINE '| ")
        print("\t                  -------------")
        
    elif s.lower() == 'december' or s.lower() == 'dec' :
        print("\n People born in DECEMBER are CONFIDENT and LOVING")
        print("\t                  ------------")
        print("\tYour Birth GEM is |' ZIRCON '| ")
        print("\t                  ------------")
        
    else:
        print("\n Please check the Entered data.")
        
    next = True if input("Shall we do it again (y/n)").lower() =='y' else False