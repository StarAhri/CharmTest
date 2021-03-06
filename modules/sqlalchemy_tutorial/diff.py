a = {'data': {'table': {
    'sort': {'current': [2, 'desc', 'avg-active_devices'], 'sortEscapeLoading': True, 'sortByBackend': False,
             'columns': [{'status': 'desc', 'name': 'avg-active_devices', 'idx': 2},
                         {'status': 'desc', 'name': 'avg-active_last_30_days', 'idx': 3},
                         {'status': 'desc', 'name': 'ratio-active_devices-by-active_last_30_days', 'idx': 4},
                         {'status': 'desc', 'name': 'sessions', 'idx': 5},
                         {'status': 'desc', 'name': 'ratio-sessions-by-active_devices', 'idx': 6}]},
    'rows': [[['CN'], ['China', 'CN'], 0, 0, [0, 0, 100], 0, 'N/A'],
             [['US'], ['United States', 'US'], 0, 0, [0, 0, 100], 0, 'N/A']],
    'top_row': [-1, ['Total'], 0, 0, [0, 0, 100], 0, 'N/A'], 'context': {'currency': '$'},
    'fixedColumns': {'tableWidth': 100, 'fixed': 0, 'recordML': True},
    'columns': [[[u'', u''], 'table_checkbox', 'table_checkbox'],
                [['Country/Region', u''], 'country_flag_with_text', 'country'],
                [['Avg DAD', 'Average number of Daily Active Devices (DAD).'], 'number', 'number'],
                [['Avg 30 Day Active', 'Average number of Active Devices over the last 30 Days.'], 'number', 'number'],
                [['DAD / 30 Day Active',
                  'Ratio of Daily Active Devices (DAD) to Active Devices over the last 30 Days (30 Day Active).'],
                 'percent-with-two-decimals', 'percent-with-two-decimals'],
                [['Total Sessions', 'Total number of sessions where app has been used for at least two seconds.'],
                 'number', 'number'],
                [['Avg Sessions / Device / Day', 'Average number of sessions per daily active device.'], 'number',
                 'number']]}, 'chart': {'hovertip': {'maxItem': 7}, 'percent': {'value': False, 'custom': True},
                                        'total_datapoints': {'data': [[1480550400000, 5], [1480636800000, 5]],
                                                             'stack': 'x', 'label': 'Total'}, 'datapoints': [
        {'id': 'CN', 'data': [[1480550400000, 5], [1480636800000, 5]], 'stack': 'x', 'label': 'China'},
        {'id': 'US', 'data': [[1480550400000, 5], [1480636800000, 5]], 'stack': 'x', 'label': 'United States'}],
                                        'totalValue': {'by': 'all'}, 'type': {'options': ['line', 'column']},
                                        'stack': {'value': True, 'custom': True}}, 'permission': True}, 'success': True}
b = {'data': {'table': {
    'sort': {'current': [2, 'desc', 'avg-active_devices'], 'sortEscapeLoading': True, 'sortByBackend': False,
             'columns': [{'status': 'desc', 'name': 'avg-active_devices', 'idx': 2},
                         {'status': 'desc', 'name': 'avg-active_last_30_days', 'idx': 3},
                         {'status': 'desc', 'name': 'ratio-active_devices-by-active_last_30_days', 'idx': 4},
                         {'status': 'desc', 'name': 'sessions', 'idx': 5},
                         {'status': 'desc', 'name': 'ratio-sessions-by-active_devices', 'idx': 6}]},
    'rows': [[['CN'], ['China', 'CN'], 5, 5, [100.0, 0, 100], 10, 1.0],
             [['US'], ['United States', 'US'], 5, 5, [100.0, 0, 100], 10, 1.0]], 'context': {'currency': '$'},
    'fixedColumns': {'tableWidth': 100, 'fixed': 0, 'recordML': True},
    'columns': [[['', ''], 'table_checkbox', 'table_checkbox'],
                [['Country/Region', ''], 'country_flag_with_text', 'country'],
                [['Avg DAD', 'Average number of Daily Active Devices (DAD).'], 'number', 'number'],
                [['Avg 30 Day Active', 'Average number of Active Devices over the last 30 Days.'], 'number', 'number'],
                [['DAD / 30 Day Active',
                  'Ratio of Daily Active Devices (DAD) to Active Devices over the last 30 Days (30 Day Active).'],
                 'percent-with-two-decimals', 'percent-with-two-decimals'],
                [['Total Sessions', 'Total number of sessions where app has been used for at least two seconds.'],
                 'number', 'number'],
                [['Avg Sessions / Device / Day', 'Average number of sessions per daily active device.'], 'number',
                 'number']], 'top_row': [-1, ['Total'], 10, 10, [100.0, 0, 100], 20, 1.0]},
    'chart': {'percent': {'value': False, 'custom': True}, 'type': {'options': ['line', 'column']},
              'datapoints': [{'stack': 'x', 'data': [[1480550400000, 5], [1480636800000, 5]], 'id': 'CN',
                              'label': 'China'},
                             {'stack': 'x', 'data': [[1480550400000, 5], [1480636800000, 5]], 'id': 'US',
                              'label': 'United States'}], 'hovertip': {'maxItem': 7},
              'totalValue': {'by': 'all'},
              'total_datapoints': {'data': [[1480550400000, 10], [1480636800000, 10]], 'stack': 'x',
                                   'label': 'Total'}, 'stack': {'value': True, 'custom': True}},
    'permission': True}, 'success': True}

set = {'device_code': [u'iPhone'], 'order_by': ['date', 'asc'], 'dimensions': ['country'], 'end_date': '2016-12-02',
       'country': [u'CN', u'US'], 'metrics': ['active_devices', 'active_last_30_days', 'sessions'], 'meta': {},
       'filters': {'user_product_ids': [195]}, 'granularity': 'daily', 'start_date': '2016-12-01'}
