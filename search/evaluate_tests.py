def evaluate_tests(func, tests):
    '''Evaluate func against tests. Test example:
    tests = [{'input': {'nums': [34, 1]}, 'output': 1}]
    '''
    print('Evaluating tests')
    for i in range(len(tests)):
        if func(tests[i]['input']['nums']) == tests[i]['output']:
            result = 'PASS'
        else:
            result = 'FAILED'
        print('TEST:', i, result)