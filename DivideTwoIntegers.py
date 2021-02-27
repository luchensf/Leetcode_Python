def devide(dividend, divisor):
    is_negative = (dividend < 0) != (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0
    d = divisor

    while d <= dividend:
        # as long as divisor is <= dividend, the quotient will be at least 1 to start with
        curq = 1
        while d <= dividend:
            # the goal here is to sum d by itself which in practice is multiple 2
            # curq is the current quotient sum itself which is to keep track how many multiplies has done
            # ex, divisor is 2 and dividend is 23, d = 2+2, curq = 1+1, for the first loop
            # then d = 4 + 4, curq = 2 + 2 for the second loop and so on
            d += d
            curq += curq
        # the previous while loop will break until the next multiple + next multiple is more than dividend
        dividend -= d # reassign dividend with the left over dividend
        d = divisor # reset d to divisor
        quotient += curq  # keep track of total quotient

    res = -quotient if is_negative else quotient
    # res should be in between -2147483648 and 2147483647, if not then return those numbers instead of res
    return min(2147483647, max(res, -2147483648))

