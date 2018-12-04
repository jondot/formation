# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_default_stack 1'] = [
    [
        'info',
        'request.http',
        {
            'headers': None,
            'method': 'get',
            'params': {
            },
            'url': 'http://example.com'
        },
        {
            'env': 'local',
            'ns': 'service',
            'pid': 'pid-1',
            'rid': 'req-1',
            'rid_p': None,
            'scope': 'all',
            'sha': 'dev',
            'tid': 'tid-1',
            'uid': None,
            'v': '0.01'
        }
    ],
    [
        'debug',
        'request.http',
        {
            'headers': {
                'x-request-id': 'req-1'
            }
        },
        {
            'env': 'local',
            'ns': 'service',
            'pid': 'pid-1',
            'rid': 'req-1',
            'rid_p': None,
            'scope': 'all',
            'sha': 'dev',
            'tid': 'tid-1',
            'uid': None,
            'v': '0.01'
        }
    ],
    [
        'info',
        'response.http',
        {
            'duration_us': None,
            'headers': None,
            'method': 'GET',
            'size': 1270,
            'status': 200,
            'url': 'http://example.com/'
        },
        {
            'env': 'local',
            'ns': 'service',
            'pid': 'pid-1',
            'rid': 'req-1',
            'rid_p': None,
            'scope': 'all',
            'sha': 'dev',
            'tid': 'tid-1',
            'uid': None,
            'v': '0.01'
        }
    ],
    [
        'debug',
        'response.http',
        {
            'headers': {
                'cache-control': 'max-age=604800',
                'content-encoding': 'gzip',
                'content-length': '606',
                'content-type': 'text/html; charset=UTF-8',
                'date': 'Tue, 04 Dec 2018 13:49:48 GMT',
                'expires': 'Tue, 11 Dec 2018 13:49:48 GMT',
                'last-modified': 'Fri, 09 Aug 2013 23:54:35 GMT',
                'server': 'ECS (dca/24AA)',
                'vary': 'Accept-Encoding',
                'x-cache': 'HIT'
            }
        },
        {
            'env': 'local',
            'ns': 'service',
            'pid': 'pid-1',
            'rid': 'req-1',
            'rid_p': None,
            'scope': 'all',
            'sha': 'dev',
            'tid': 'tid-1',
            'uid': None,
            'v': '0.01'
        }
    ]
]

snapshots['test_default_stack 2'] = {
    'env': 'local',
    'ns': 'service',
    'pid': 'pid-1',
    'rid': 'req-1',
    'rid_p': None,
    'scope': 'all',
    'sha': 'dev',
    'tid': 'tid-1',
    'uid': None,
    'v': '0.01'
}
