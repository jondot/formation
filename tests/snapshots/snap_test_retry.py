# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_retry 1'] = '''(
    {
        'args': {
        },
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'httpbin.org',
            'User-Agent': 'python-requests/2.21.0'
        },
        'origin': '109.64.229.18, 109.64.229.18',
        'url': 'https://httpbin.org/get'
    },
    200,
    [
        (
            'access-control-allow-credentials',
            'true'
        ),
        (
            'access-control-allow-origin',
            '*'
        ),
        (
            'connection',
            'keep-alive'
        ),
        (
            'content-encoding',
            'gzip'
        ),
        (
            'content-length',
            '183'
        ),
        (
            'content-type',
            'application/json'
        ),
        (
            'date',
            'Wed, 08 May 2019 13:17:21 GMT'
        ),
        (
            'referrer-policy',
            'no-referrer-when-downgrade'
        ),
        (
            'server',
            'nginx'
        ),
        (
            'x-content-type-options',
            'nosniff'
        ),
        (
            'x-frame-options',
            'DENY'
        ),
        (
            'x-xss-protection',
            '1; mode=block'
        )
    ]
)'''
