import random
import unittest
import calendar
import itertools
import datetime as dt
import collections as cl

import lab
import helpers

def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda x: x
    return unittest.skip("'{0}' not implemented".format(attr))

CoinGameInput = cl.namedtuple('CoinGameInput', 'strategies, players, winner')

def coin_game_input():
    players = [ 'alice', 'bob' ]

    yield from [
        (1, CoinGameInput(1, players, 'alice')),
        (2, CoinGameInput(1, reversed(players), 'bob')),
        (3, CoinGameInput(2, players, 'bob')),
        (10, CoinGameInput(22, players, 'alice')),
        (25, CoinGameInput(3344, players, 'alice')),
        (30, CoinGameInput(18272, players, 'bob')),
    ]

class RecursionTest(unittest.TestCase):
    @skipUnlessHasattr(lab, 'exponentiate')
    def test_a_rsum(self):
        for _ in range(3):
            mylist = random.sample(range(100), 10)
            with self.subTest(values=mylist):
                    self.assertEqual(sum(mylist), lab.rsum(mylist))

    @skipUnlessHasattr(lab, 'exponentiate')
    def test_b_exponentiate(self):
        for i in range(3):
            for j in range(0, 10, 2):
                with self.subTest(base=i, exponent=j):
                    self.assertEqual(i ** j, lab.exponentiate(i, j))

    @skipUnlessHasattr(lab, 'get_nth')
    def test_c_get_nth(self):
        for i in range(3):
            rlist = random.sample(range(2 ** 10), 100)
            for j in range(10):
                item = random.randrange(len(rlist))
                with self.subTest(mylist=rlist, item=item):
                    self.assertEqual(rlist[item], lab.get_nth(rlist, item))

    @skipUnlessHasattr(lab, 'reverse')
    def test_d_reverse(self):
        for i in range(3):
            rlist = random.sample(range(2 ** 10), 100)
            for j in range(10):
                with self.subTest(mylist=rlist):
                    self.assertListEqual(rlist[::-1], lab.reverse(rlist))

    @skipUnlessHasattr(lab, 'is_older')
    def test_e_is_older(self):
        mkargs = lambda x: [ getattr(x, y) for y in ('year', 'month', 'day') ]
        today = dt.datetime.now()
        conditions = [ False ] * 3

        while not all(conditions):
            tomo = today + dt.timedelta(days=random.randrange(-10, 10))
            conditions[(today > tomo) - (today < tomo)] = True

            older = lab.is_older(*map(mkargs, (today, tomo)))
            with self.subTest(date_1=today, date_2=tomo):
                self.assertEqual(older, tomo > today)

    @skipUnlessHasattr(lab, 'number_before_reaching_sum')
    def test_f_number_before_reaching_sum(self):
        total = 10
        numbers = list(range(1, 6))

        with self.subTest(total=10, numbers=numbers):
            self.assertEqual(lab.number_before_reaching_sum(total, numbers), 3)

    @skipUnlessHasattr(lab, 'what_month')
    def test_g_what_month(self):
        now = dt.datetime.now()
        for i in itertools.count():
            year = now.year + i
            if not calendar.isleap(year):
                break

        days = 1
        for i in range(1, 13):
            (_, d) = calendar.monthrange(year, i)
            for j in range(d):
                with self.subTest(day=days):
                    self.assertEqual(lab.what_month(days), i)
                days += 1

    @skipUnlessHasattr(lab, 'elfish')
    def test_h_elfish(self):
        for i in helpers.elves():
            with self.subTest(elf=i):
                self.assertTrue(lab.elfish(i))

    @skipUnlessHasattr(lab, 'elfish')
    def test_i_not_elfish(self):
        for i in helpers.elves():
            bad_elf = i
            for j in 'elf':
                bad_elf = bad_elf.replace(j, 'x')

            with self.subTest(elf=bad_elf):
                self.assertFalse(lab.elfish(bad_elf))

    @skipUnlessHasattr(lab, 'coin_game_strategies')
    def test_j_coin_game_strategies(self):
        for (i, j) in coin_game_input():
            with self.subTest(coins=i):
                self.assertEqual(lab.coin_game_strategies(i), j.strategies)

    @skipUnlessHasattr(lab, 'coin_game_winner')
    def test_k_coin_game_winner(self):
        for (i, j) in coin_game_input():
            with self.subTest(coins=i):
                self.assertEqual(lab.coin_game_winner(i, *j.players), j.winner)

if __name__ == '__main__':
    unittest.main(verbosity=3, failfast=True)
