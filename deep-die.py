#!/usr/bin/python

# Copyright 2013 Jeff Mendoza
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

prob_2 = [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]

def possibility(num, choose):
    results = []
    for choice in choose:
        if num > choice:
            newchoose = list(choose)
            newchoose.remove(choice)
            oneresult = possibility(num - choice, newchoose)
            for res in oneresult:
                res.insert(0, choice)
            results.extend(oneresult)
    newres = []
    for res in results:
        res.sort()
        if res not in newres:
            newres.append(res)
    if num in choose:
        newres.append([num])
    return newres

def one_ok(list):
    for num in list:
        if num > 6:
            return False
    return True

def choose_best(list, roll):
    choices =  possibility(roll, list)
    if not choices:
        sum = reduce(lambda x, y: x+y, list, 0)
        return sum, None, None
    best_choice = None
    lowest_sum = 99999
    num_roll = 0
    for choice in choices:
        tent_list = [ num for num in list if num not in choice ]
        weighted_sum = 0
        for next_roll in range(2, 13):
            sum, a, b = choose_best(tent_list, next_roll)
            weighted_sum += (float(sum) / 36) * prob_2[next_roll]
        if weighted_sum < lowest_sum:
            lowest_sum = weighted_sum
            best_choice = choice
            num_roll = 2
        if one_ok(tent_list):
            one_sum = 0
            for next_roll in range(1, 7):
                sum, a, b = choose_best(tent_list, next_roll)
                one_sum += (float(sum) / 6)
            if one_sum < lowest_sum:
                lowest_sum = one_sum
                best_choice = choice
                num_roll = 1
    return lowest_sum, best_choice, num_roll

def main():
    current_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while True:
        print "current list %s" % current_list
        dice_roll = int(raw_input('Dice roll: '))
        weighted_sum, best_choice, num_roll = choose_best(current_list, dice_roll)
        if best_choice:
            print "sum %f cross %s roll %d" % (weighted_sum, best_choice, num_roll)
            for num in best_choice:
                current_list.remove(num)
        else:
            print 'you lose'
            return

if __name__ == '__main__':
    main()
