test = {
  'name': 'Understanding scheme.py',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'b141a4dc342bd6678f7aa30b3f0f1f1a',
          'choices': [
            'For a user-defined procedure only',
            'For a primitive procedure only',
            'For a either a user-defined or primitive procedure'
          ],
          'hidden': False,
          'locked': True,
          'question': 'When does scheme_apply call scheme_eval?'
        },
        {
          'answer': '1cdd2d5fb59a2ec5de42ad89f88b73a9',
          'choices': [
            'env.lookup(expr)',
            'expr.first',
            'scheme_eval(first, env)',
            'scheme_apply(procedure, args, env)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What expression in the body of scheme_eval computes
          the value of a symbol
          """
        },
        {
          'answer': '129b7b576a5261e847c34e60832b5620',
          'choices': [
            'SchemeError("malformed list: (1)")',
            'SchemeError("cannot call: 1")',
            'AssertionError',
            'SchemeError("unknown identifier: 1")'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What exception will be raised for the expression (1)'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}