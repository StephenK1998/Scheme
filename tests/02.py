test = {
  'name': 'Question 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> read_line("(a . b)")
          cbbe2ccb7cba34e792300000210a2f6c
          # locked
          # choice: Pair('a', Pair('b'))
          # choice: Pair('a', Pair('b', nil))
          # choice: SyntaxError
          # choice: Pair('a', 'b')
          # choice: Pair('a', 'b', nil)
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(a b . c)")
          38df9234d9ed7ef7689d5922651cf4c7
          # locked
          # choice: Pair('a', Pair('b', Pair('c', nil)))
          # choice: Pair('a', Pair('b', Pair('c')))
          # choice: Pair('a', 'b', 'c')
          # choice: Pair('a', Pair('b', 'c'))
          # choice: SyntaxError
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> read_line("(a b . c d)")
          82640ec73ce860e60829be0e1dea9112
          # locked
          # choice: Pair('a', Pair('b', Pair('c', 'd')))
          # choice: Pair('a', Pair('b', 'c'))
          # choice: Pair('a', Pair('b', Pair('c', Pair('d', nil))))
          # choice: SyntaxError
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(a . (b . (c . ())))")
          517c16dfcaacc682e57c4a5e91f07a51
          # locked
          # choice: Pair('a', Pair('b', Pair('c', nil)))
          # choice: SyntaxError
          # choice: Pair('a', Pair('b', Pair('c', Pair(nil, nil))))
          # choice: Pair('a', 'b', 'c')
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(a . ((b . (c)))))")
          24558e7cd69096da40da549c2fb7d828
          # locked
          # choice: Pair('a', Pair(Pair('b', Pair('c', nil)), nil))
          # choice: Pair('a', Pair('b', Pair('c', nil)), nil)
          # choice: Pair('a', Pair('b', Pair('c')), nil)
          # choice: Pair('a', Pair(Pair('b', Pair('c', nil)), nil), nil)
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(. . 2)")
          SyntaxError
          >>> read_line("(2 . 3 4 . 5)")
          SyntaxError
          >>> read_line("(2 (3 . 4) 5)")
          Pair(2, Pair(Pair(3, 4), Pair(5, nil)))
          >>> read_line("(1 2")
          SyntaxError
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}