
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    leap_year1 = 366
    common_year1 = 365
    leap_year2 = 366
    common_year2 = 365
    years_old = 0
    month1_days = 0
    month2_days = 0
    jan = 31
    feb1 = 0
    feb2 = 0
    mar = 31
    apr = 30
    may = 31
    jun = 30
    jul = 31
    aug = 31
    sep = 30
    oct = 31
    nov = 30
    dec = 31
#calculates months
#calculates years old
    if month2 > month1:
        years_old = year2 - year1
    if month2 < month1:
            years_old = year2 - year1 - 1
    if month2 == month1:
        if year2 == year1:
            years_old = 0
        else:
            if day1 >= day2:
                years_old = year2 - year1
            else:
                years_old = year2 - year1 - 1
#calculates number of common years and leap years based on difference between date and birthday year
    
    if year1 % 4 != 0:
        if year1 % 400 != 0:
            year1 = common_year1
    else:
        if year1 % 100 != 0:
            year1 = leap_year1
        else:
            year1 = leap_year1
    if year2 % 4 != 0:
        if year2 % 400 != 0:
            year2 = common_year2
    else:
        if year2 % 100 != 0:
            year2 = leap_year2
        else:
            year2 = leap_year2
    
    num_leap_years = 0     
    extra_day = 0
    
    if year1 == 366:
        if year2 == year1 + 365:    
            if month1 > 2:
                num_leap_years = years_old / 4
            if month1 == 2:
                if day1 >= 29:
                    num_leap_years = years_old / 4 
                else:
                    if day1 < 29:
                        num_leap_years = years_old / 4
                        extra_day = 1
            if month1 < 2:
                num_leap_years = years_old / 4
                extra_day = extra_day + 1
    if year1 == 366:
        if year2 + 365 > year1:
            num_leap_years = years_old / 4
    if year1 == 365:
        num_leap_years = years_old / 4
    if year2 == 366:
        if month1 > 2:
            num_leap_years = years_old / 4
            extra_day = extra_day + 1
        if month1 == 2:
            if day1 >= 29:
                num_leap_years = years_old / 4
                extra_day = extra_day + 1
    if year1 == year2 == 366:
        extra_day = 0
                
    num_common_years = years_old - num_leap_years
    
    if years_old == 0:
        num_common_years = 0
        num_leap_years = 0
    
#sets february number of days for date year 
    if year2 == 366:
        feb2 = 29
    else:
        feb2 = 28
    if year1 == 366:
        feb1 = 29
    else:
        feb1 = 28
    month1var = 0
    month2var = 0
    if month1 == 1:
        month1var = jan
    if month1 == 2:
        month1var = feb1
    if month1 == 3:
        month1var = mar
    if month1 == 4:
        month1var = apr
    if month1 == 5:
        month1var = may
    if month1 == 6:
        month1var = jun
    if month1 == 7:
        month1var = jul
    if month1 == 8:
        month1var = aug
    if month1 == 9:
        month1var = sep
    if month1 == 10:
        month1var = oct
    if month1 == 11:
        month1var = nov
    if month1 == 12:
        month1var = dec
    if month2 == 1:
        month2var = jan
    if month2 == 2:
        month2var = feb2
    if month2 == 3:
        month2var = mar
    if month2 == 4:
        month2var = apr
    if month2 == 5:
        month2var = may
    if month2 == 6:
        month2var = jun
    if month2 == 7:
        month2var = jul
    if month2 == 8:
        month2var = aug
    if month2 == 9:
        month2var = sep
    if month2 == 10:
        month2var = oct
    if month2 == 11:
        month2var = nov
    if month2 == 12:
        month2var = dec
#calculates the days between months not accounted for by the years calculation            
    month_gap_days = 0
    if month2 == month1:
        month_gap_days = 0
    if month2 > month1:
        if month2 == 12:
            if month1 == 1:
                month_gap_days = feb2 + mar + apr + may + jun + jul + aug + sep + oct + nov
        if month2 == 11:
            if month1 == 1:
                month_gap_days = feb2 + mar + apr + may + jun + jul + aug + sep + oct 
        if month2 == 10:
            if month1 == 1:
                month_gap_days = feb2 + mar + apr + may + jun + jul + aug + sep 
        if month2 == 9:
            if month1 == 1:
                month_gap_days = feb2 + mar + apr + may + jun + jul + aug
        if month2 == 8:
            if month1 == 1:
                month_gap_days = feb2 + mar + apr + may + jun + jul
        if month2 == 7:
            if month1 == 1:
                month_gap_days = feb2 + mar + apr + may + jun
        if month2 == 6:
            if month1 == 1:
                month_gap_days = feb2 + mar + apr + may
        if month2 == 5:
            if month1 == 1:
                month_gap_days = feb2 + mar + apr
        if month2 == 4:
            if month1 == 1:
                month_gap_days = feb2 + mar
        if month2 == 3:
            if month1 == 1:
                month_gap_days = feb2
        if month2 == 12:
            if month1 == 2:
                month_gap_days = mar + apr + may + jun + jul + aug + sep + oct + nov
        if month2 == 11:
            if month1 == 2:
                month_gap_days = mar + apr + may + jun + jul + aug + sep + oct 
        if month2 == 10:
            if month1 == 2:
                month_gap_days = mar + apr + may + jun + jul + aug + sep 
        if month2 == 9:
            if month1 == 2:
                month_gap_days = mar + apr + may + jun + jul + aug
        if month2 == 8:
            if month1 == 2:
                month_gap_days = mar + apr + may + jun + jul
        if month2 == 7:
            if month1 == 2:
                month_gap_days = mar + apr + may + jun
        if month2 == 6:
            if month1 == 2:
                month_gap_days = mar + apr + may
        if month2 == 5:
            if month1 == 2:
                month_gap_days = mar + apr
        if month2 == 4:
            if month1 == 2:
                month_gap_days = mar
        if month2 == 12:
            if month1 == 3:
                month_gap_days = apr + may + jun + jul + aug + sep + oct + nov
        if month2 == 11:
            if month1 == 3:
                month_gap_days = apr + may + jun + jul + aug + sep + oct 
        if month2 == 10:
            if month1 == 3:
                month_gap_days = apr + may + jun + jul + aug + sep 
        if month2 == 9:
            if month1 == 3:
                month_gap_days = apr + may + jun + jul + aug
        if month2 == 8:
            if month1 == 3:
                month_gap_days = apr + may + jun + jul
        if month2 == 7:
            if month1 == 3:
                month_gap_days = apr + may + jun
        if month2 == 6:
            if month1 == 3:
                month_gap_days = apr + may
        if month2 == 5:
            if month1 == 3:
                month_gap_days = apr
        if month2 == 12:
            if month1 == 4:
                month_gap_days = may + jun + jul + aug + sep + oct + nov
        if month2 == 11:
            if month1 == 4:
                month_gap_days = may + jun + jul + aug + sep + oct 
        if month2 == 10:
            if month1 == 4:
                month_gap_days = may + jun + jul + aug + sep 
        if month2 == 9:
            if month1 == 4:
                month_gap_days = may + jun + jul + aug
        if month2 == 8:
            if month1 == 4:
                month_gap_days = may + jun + jul
        if month2 == 7:
            if month1 == 4:
                month_gap_days = may + jun
        if month2 == 6:
            if month1 == 4:
                month_gap_days = may
        if month2 == 12:
            if month1 == 5:
                month_gap_days = jun + jul + aug + sep + oct + nov
        if month2 == 11:
            if month1 == 5:
                month_gap_days = jun + jul + aug + sep + oct 
        if month2 == 10:
            if month1 == 5:
                month_gap_days = jun + jul + aug + sep 
        if month2 == 9:
            if month1 == 5:
                month_gap_days = jun + jul + aug
        if month2 == 8:
            if month1 == 5:
                month_gap_days = jun + jul
        if month2 == 7:
            if month1 == 5:
                month_gap_days = jun
        if month2 == 12:
            if month1 == 6:
                month_gap_days = jul + aug + sep + oct + nov
        if month2 == 11:
            if month1 == 6:
                month_gap_days = jul + aug + sep + oct 
        if month2 == 10:
            if month1 == 6:
                month_gap_days = jul + aug + sep 
        if month2 == 9:
            if month1 == 6:
                month_gap_days = jul + aug
        if month2 == 8:
            if month1 == 6:
                month_gap_days = jul
        if month2 == 12:
            if month1 == 7:
                month_gap_days = aug + sep + oct + nov
        if month2 == 11:
            if month1 == 7:
                month_gap_days = aug + sep + oct 
        if month2 == 10:
            if month1 == 7:
                month_gap_days = aug + sep 
        if month2 == 9:
            if month1 == 7:
                month_gap_days = aug
        if month2 == 12:
            if month1 == 8:
                month_gap_days = sep + oct + nov
        if month2 == 11:
            if month1 == 8:
                month_gap_days = sep + oct 
        if month2 == 10:
            if month1 == 8:
                month_gap_days = sep 
        if month2 == 12:
            if month1 == 9:
                month_gap_days = oct + nov
        if month2 == 11:
            if month1 == 9:
                month_gap_days = oct 
        if month2 == 12:
            if month1 == 10:
                month_gap_days = nov
    else:
        month_gap_days = 0
    
    day_gap_days = 0 
    day2_gap_days = day2
    day1_gap_days = month1var - day1
    
    if month1 == month2:
        if  day1 == day2:
            day_gap_days = 0
    else:
        day_gap_days = day2_gap_days + day1_gap_days
    
    #return year1, year2, years_old, num_leap_years, num_common_years, feb1, feb2, month1var, month2var, month_gap_days, day2_gap_days, day1_gap_days, extra_day
    
    return (num_leap_years * 366) + (num_common_years * 365) + month_gap_days + day_gap_days + extra_day
    
    
print daysBetweenDates(1900,1,1,1999,12,31)


# Test routine

def test():
   test_cases = [((2012,1,1,2012,2,28), 58), 
                 ((2012,1,1,2012,3,1), 60),
                 ((2011,6,30,2012,6,30), 366),
                 ((2011,1,1,2012,8,8), 585),
                 ((1900,1,1,1999,12,31), 36523)]
   for (args, answer) in test_cases:
       result = daysBetweenDates(*args)
       if result != answer:
           print "Test with data:", args, "failed"
       else:
           print "Test case passed!"

test()