# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_json_all 1'] = '''(
    {
        'args': {
        },
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/json',
            'Host': 'httpbin.org',
            'User-Agent': 'the-fabricator/1.0.0',
            'X-Flabber-Id': '8825bec2-0523-4621-bd21-f105d3920917'
        },
        'origin': '109.64.229.18, 109.64.229.18',
        'url': 'https://httpbin.org/get'
    },
    200,
    [
        (
            'Access-Control-Allow-Credentials',
            'true'
        ),
        (
            'Access-Control-Allow-Origin',
            '*'
        ),
        (
            'Connection',
            'keep-alive'
        ),
        (
            'Content-Encoding',
            'gzip'
        ),
        (
            'Content-Length',
            '247'
        ),
        (
            'Content-Type',
            'application/json'
        ),
        (
            'Date',
            'Wed, 08 May 2019 11:33:53 GMT'
        ),
        (
            'Referrer-Policy',
            'no-referrer-when-downgrade'
        ),
        (
            'Server',
            'nginx'
        ),
        (
            'X-Content-Type-Options',
            'nosniff'
        ),
        (
            'X-Frame-Options',
            'DENY'
        ),
        (
            'X-XSS-Protection',
            '1; mode=block'
        )
    ]
)'''

snapshots['test_json_all 2'] = '''(
    {
        'args': {
        },
        'data': 'testing=123',
        'files': {
        },
        'form': {
        },
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Length': '11',
            'Content-Type': 'application/json',
            'Host': 'httpbin.org',
            'User-Agent': 'the-fabricator/1.0.0',
            'X-Flabber-Id': '72c26da4-74e4-4659-a13c-84e3c27d529b'
        },
        'json': None,
        'origin': '109.64.229.18, 109.64.229.18',
        'url': 'https://httpbin.org/post'
    },
    200,
    [
        (
            'Access-Control-Allow-Credentials',
            'true'
        ),
        (
            'Access-Control-Allow-Origin',
            '*'
        ),
        (
            'Connection',
            'keep-alive'
        ),
        (
            'Content-Encoding',
            'gzip'
        ),
        (
            'Content-Length',
            '290'
        ),
        (
            'Content-Type',
            'application/json'
        ),
        (
            'Date',
            'Wed, 08 May 2019 11:33:54 GMT'
        ),
        (
            'Referrer-Policy',
            'no-referrer-when-downgrade'
        ),
        (
            'Server',
            'nginx'
        ),
        (
            'X-Content-Type-Options',
            'nosniff'
        ),
        (
            'X-Frame-Options',
            'DENY'
        ),
        (
            'X-XSS-Protection',
            '1; mode=block'
        )
    ]
)'''

snapshots['test_json_all 3'] = '''(
    {
        'args': {
        },
        'data': 'testing=123',
        'files': {
        },
        'form': {
        },
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Length': '11',
            'Content-Type': 'application/json',
            'Host': 'httpbin.org',
            'User-Agent': 'the-fabricator/1.0.0',
            'X-Flabber-Id': 'cdb0623c-11f8-47bd-b884-a86b7517096e'
        },
        'json': None,
        'origin': '109.64.229.18, 109.64.229.18',
        'url': 'https://httpbin.org/put'
    },
    200,
    [
        (
            'Access-Control-Allow-Credentials',
            'true'
        ),
        (
            'Access-Control-Allow-Origin',
            '*'
        ),
        (
            'Connection',
            'keep-alive'
        ),
        (
            'Content-Encoding',
            'gzip'
        ),
        (
            'Content-Length',
            '291'
        ),
        (
            'Content-Type',
            'application/json'
        ),
        (
            'Date',
            'Wed, 08 May 2019 11:33:54 GMT'
        ),
        (
            'Referrer-Policy',
            'no-referrer-when-downgrade'
        ),
        (
            'Server',
            'nginx'
        ),
        (
            'X-Content-Type-Options',
            'nosniff'
        ),
        (
            'X-Frame-Options',
            'DENY'
        ),
        (
            'X-XSS-Protection',
            '1; mode=block'
        )
    ]
)'''

snapshots['test_json_all 4'] = '''(
    {
        'args': {
        },
        'data': '',
        'files': {
        },
        'form': {
        },
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/json',
            'Host': 'httpbin.org',
            'User-Agent': 'the-fabricator/1.0.0',
            'X-Flabber-Id': '44bce06f-7af1-4bf1-8355-0aab574d5d10'
        },
        'json': None,
        'origin': '109.64.229.18, 109.64.229.18',
        'url': 'https://httpbin.org/delete'
    },
    200,
    [
        (
            'Access-Control-Allow-Credentials',
            'true'
        ),
        (
            'Access-Control-Allow-Origin',
            '*'
        ),
        (
            'Connection',
            'keep-alive'
        ),
        (
            'Content-Encoding',
            'gzip'
        ),
        (
            'Content-Length',
            '272'
        ),
        (
            'Content-Type',
            'application/json'
        ),
        (
            'Date',
            'Wed, 08 May 2019 11:33:55 GMT'
        ),
        (
            'Referrer-Policy',
            'no-referrer-when-downgrade'
        ),
        (
            'Server',
            'nginx'
        ),
        (
            'X-Content-Type-Options',
            'nosniff'
        ),
        (
            'X-Frame-Options',
            'DENY'
        ),
        (
            'X-XSS-Protection',
            '1; mode=block'
        )
    ]
)'''

snapshots['test_json_all 5'] = '''(
    {
        'args': {
        },
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'httpbin.org',
            'User-Agent': 'the-fabricator/1.0.0',
            'X-Flabber-Id': '1ec8ad6a-82c9-4dc4-b275-03a6d310e9dc'
        },
        'origin': '109.64.229.18, 109.64.229.18',
        'url': 'https://httpbin.org/get'
    },
    200,
    [
        (
            'Access-Control-Allow-Credentials',
            'true'
        ),
        (
            'Access-Control-Allow-Origin',
            '*'
        ),
        (
            'Connection',
            'keep-alive'
        ),
        (
            'Content-Encoding',
            'gzip'
        ),
        (
            'Content-Length',
            '223'
        ),
        (
            'Content-Type',
            'application/json'
        ),
        (
            'Date',
            'Wed, 08 May 2019 11:33:56 GMT'
        ),
        (
            'Referrer-Policy',
            'no-referrer-when-downgrade'
        ),
        (
            'Server',
            'nginx'
        ),
        (
            'X-Content-Type-Options',
            'nosniff'
        ),
        (
            'X-Frame-Options',
            'DENY'
        ),
        (
            'X-XSS-Protection',
            '1; mode=block'
        )
    ]
)'''

snapshots['test_json_all 6'] = '''(
    {
        'args': {
        },
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'httpbin.org',
            'User-Agent': 'the-fabricator/1.0.0',
            'X-Flabber-Id': '9afa181e-8ac3-4fdc-9226-798314b738d6'
        },
        'origin': '109.64.229.18, 109.64.229.18',
        'url': 'https://httpbin.org/get'
    },
    200,
    [
        (
            'Access-Control-Allow-Credentials',
            'true'
        ),
        (
            'Access-Control-Allow-Origin',
            '*'
        ),
        (
            'Connection',
            'keep-alive'
        ),
        (
            'Content-Encoding',
            'gzip'
        ),
        (
            'Content-Length',
            '224'
        ),
        (
            'Content-Type',
            'application/json'
        ),
        (
            'Date',
            'Wed, 08 May 2019 11:33:57 GMT'
        ),
        (
            'Referrer-Policy',
            'no-referrer-when-downgrade'
        ),
        (
            'Server',
            'nginx'
        ),
        (
            'X-Content-Type-Options',
            'nosniff'
        ),
        (
            'X-Frame-Options',
            'DENY'
        ),
        (
            'X-XSS-Protection',
            '1; mode=block'
        )
    ]
)'''

snapshots['test_html_response 1'] = '''(
    <Element html at 0x100000000>,
    200,
    [
        (
            'Alt-Svc',
            'quic=":443"; ma=2592000; v="46,44,43,39"'
        ),
        (
            'Cache-Control',
            'private, max-age=0'
        ),
        (
            'Content-Encoding',
            'gzip'
        ),
        (
            'Content-Type',
            'text/html; charset=ISO-8859-1'
        ),
        (
            'Date',
            'Wed, 08 May 2019 09:49:43 GMT'
        ),
        (
            'Expires',
            '-1'
        ),
        (
            'P3P',
            'CP="This is not a P3P policy! See g.co/p3phelp for more info."'
        ),
        (
            'Server',
            'gws'
        ),
        (
            'Set-Cookie',
            '1P_JAR=2019-05-08-09; expires=Fri, 07-Jun-2019 09:49:43 GMT; path=/; domain=.google.com, NID=183=w7zhe_zTVazag0tw5ieire797eXQsvWTMI4a0I59oK1Ihel_tmwLT52S16sbIIGBbhENNPeV5OLNkg1clkiHnAmqCfrnEjGtcE4GQxDjwFfByS9UTMJx_o4pDSEUJjtdN47lSs7vnF8NFEYYe7uley8xH2oEhqaFQQwKa6A2o5E; expires=Thu, 07-Nov-2019 09:49:43 GMT; path=/; domain=.google.com; HttpOnly'
        ),
        (
            'X-Frame-Options',
            'SAMEORIGIN'
        ),
        (
            'X-XSS-Protection',
            '0'
        )
    ]
)'''

snapshots['test_html_response 2'] = '''(
    <Element html at 0x100000000>,
    404,
    [
        (
            'Alt-Svc',
            'quic=":443"; ma=2592000; v="46,44,43,39"'
        ),
        (
            'Content-Length',
            '1578'
        ),
        (
            'Content-Type',
            'text/html; charset=UTF-8'
        ),
        (
            'Date',
            'Wed, 08 May 2019 09:49:43 GMT'
        ),
        (
            'Referrer-Policy',
            'no-referrer'
        )
    ]
)'''

snapshots['test_raw_response 1'] = '''(
    <Response [200]>,
    200,
    [
        (
            'Alt-Svc',
            'quic=":443"; ma=2592000; v="46,44,43,39"'
        ),
        (
            'Cache-Control',
            'private, max-age=0'
        ),
        (
            'Content-Encoding',
            'gzip'
        ),
        (
            'Content-Type',
            'text/html; charset=ISO-8859-1'
        ),
        (
            'Date',
            'Wed, 08 May 2019 09:49:44 GMT'
        ),
        (
            'Expires',
            '-1'
        ),
        (
            'P3P',
            'CP="This is not a P3P policy! See g.co/p3phelp for more info."'
        ),
        (
            'Server',
            'gws'
        ),
        (
            'Set-Cookie',
            '1P_JAR=2019-05-08-09; expires=Fri, 07-Jun-2019 09:49:44 GMT; path=/; domain=.google.com, NID=183=nz32fYoxWDSVnBQVCeQ6Vq3qsz5frRlXS56aDTklB4pb_jEKWNoSOoziZl_bAJNgmV9SZje0FlrPl1XGIfOAKguJ2ieQmuayWU6vC7FieinrYVR9GZpoFfMI0bV29ynziX5EYo8dZM7JwBUaiyE-KlkTY0wdXP-KWPnEx06_VTM; expires=Thu, 07-Nov-2019 09:49:44 GMT; path=/; domain=.google.com; HttpOnly'
        ),
        (
            'X-Frame-Options',
            'SAMEORIGIN'
        ),
        (
            'X-XSS-Protection',
            '0'
        )
    ]
)'''

snapshots['test_raw_response 2'] = '''(
    <Response [404]>,
    404,
    [
        (
            'Alt-Svc',
            'quic=":443"; ma=2592000; v="46,44,43,39"'
        ),
        (
            'Content-Length',
            '1578'
        ),
        (
            'Content-Type',
            'text/html; charset=UTF-8'
        ),
        (
            'Date',
            'Wed, 08 May 2019 09:49:44 GMT'
        ),
        (
            'Referrer-Policy',
            'no-referrer'
        )
    ]
)'''

snapshots['test_json_response 1'] = '''(
    [
        {
            'avatar_url': 'https://avatars0.githubusercontent.com/u/83390?v=4',
            'events_url': 'https://api.github.com/users/jondot/events{/privacy}',
            'followers_url': 'https://api.github.com/users/jondot/followers',
            'following_url': 'https://api.github.com/users/jondot/following{/other_user}',
            'gists_url': 'https://api.github.com/users/jondot/gists{/gist_id}',
            'gravatar_id': '',
            'html_url': 'https://github.com/jondot',
            'id': 83390,
            'login': 'jondot',
            'node_id': 'MDQ6VXNlcjgzMzkw',
            'organizations_url': 'https://api.github.com/users/jondot/orgs',
            'received_events_url': 'https://api.github.com/users/jondot/received_events',
            'repos_url': 'https://api.github.com/users/jondot/repos',
            'site_admin': False,
            'starred_url': 'https://api.github.com/users/jondot/starred{/owner}{/repo}',
            'subscriptions_url': 'https://api.github.com/users/jondot/subscriptions',
            'type': 'User',
            'url': 'https://api.github.com/users/jondot'
        },
        {
            'avatar_url': 'https://avatars2.githubusercontent.com/u/2821826?v=4',
            'events_url': 'https://api.github.com/users/cfirmo33/events{/privacy}',
            'followers_url': 'https://api.github.com/users/cfirmo33/followers',
            'following_url': 'https://api.github.com/users/cfirmo33/following{/other_user}',
            'gists_url': 'https://api.github.com/users/cfirmo33/gists{/gist_id}',
            'gravatar_id': '',
            'html_url': 'https://github.com/cfirmo33',
            'id': 2821826,
            'login': 'cfirmo33',
            'node_id': 'MDQ6VXNlcjI4MjE4MjY=',
            'organizations_url': 'https://api.github.com/users/cfirmo33/orgs',
            'received_events_url': 'https://api.github.com/users/cfirmo33/received_events',
            'repos_url': 'https://api.github.com/users/cfirmo33/repos',
            'site_admin': False,
            'starred_url': 'https://api.github.com/users/cfirmo33/starred{/owner}{/repo}',
            'subscriptions_url': 'https://api.github.com/users/cfirmo33/subscriptions',
            'type': 'User',
            'url': 'https://api.github.com/users/cfirmo33'
        },
        {
            'avatar_url': 'https://avatars0.githubusercontent.com/u/7372571?v=4',
            'events_url': 'https://api.github.com/users/urifridland/events{/privacy}',
            'followers_url': 'https://api.github.com/users/urifridland/followers',
            'following_url': 'https://api.github.com/users/urifridland/following{/other_user}',
            'gists_url': 'https://api.github.com/users/urifridland/gists{/gist_id}',
            'gravatar_id': '',
            'html_url': 'https://github.com/urifridland',
            'id': 7372571,
            'login': 'urifridland',
            'node_id': 'MDQ6VXNlcjczNzI1NzE=',
            'organizations_url': 'https://api.github.com/users/urifridland/orgs',
            'received_events_url': 'https://api.github.com/users/urifridland/received_events',
            'repos_url': 'https://api.github.com/users/urifridland/repos',
            'site_admin': False,
            'starred_url': 'https://api.github.com/users/urifridland/starred{/owner}{/repo}',
            'subscriptions_url': 'https://api.github.com/users/urifridland/subscriptions',
            'type': 'User',
            'url': 'https://api.github.com/users/urifridland'
        },
        {
            'avatar_url': 'https://avatars3.githubusercontent.com/u/4006829?v=4',
            'events_url': 'https://api.github.com/users/look4regev/events{/privacy}',
            'followers_url': 'https://api.github.com/users/look4regev/followers',
            'following_url': 'https://api.github.com/users/look4regev/following{/other_user}',
            'gists_url': 'https://api.github.com/users/look4regev/gists{/gist_id}',
            'gravatar_id': '',
            'html_url': 'https://github.com/look4regev',
            'id': 4006829,
            'login': 'look4regev',
            'node_id': 'MDQ6VXNlcjQwMDY4Mjk=',
            'organizations_url': 'https://api.github.com/users/look4regev/orgs',
            'received_events_url': 'https://api.github.com/users/look4regev/received_events',
            'repos_url': 'https://api.github.com/users/look4regev/repos',
            'site_admin': False,
            'starred_url': 'https://api.github.com/users/look4regev/starred{/owner}{/repo}',
            'subscriptions_url': 'https://api.github.com/users/look4regev/subscriptions',
            'type': 'User',
            'url': 'https://api.github.com/users/look4regev'
        }
    ],
    200,
    [
        (
            'Access-Control-Allow-Origin',
            '*'
        ),
        (
            'Access-Control-Expose-Headers',
            'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type'
        ),
        (
            'Cache-Control',
            'public, max-age=60, s-maxage=60'
        ),
        (
            'Content-Encoding',
            'gzip'
        ),
        (
            'Content-Security-Policy',
            "default-src 'none'"
        ),
        (
            'Content-Type',
            'application/json; charset=utf-8'
        ),
        (
            'Date',
            'Wed, 08 May 2019 11:24:33 GMT'
        ),
        (
            'ETag',
            'W/"df5cbf018e345904a693cf94b25ac97c"'
        ),
        (
            'Referrer-Policy',
            'origin-when-cross-origin, strict-origin-when-cross-origin'
        ),
        (
            'Server',
            'GitHub.com'
        ),
        (
            'Status',
            '200 OK'
        ),
        (
            'Strict-Transport-Security',
            'max-age=31536000; includeSubdomains; preload'
        ),
        (
            'Vary',
            'Accept'
        ),
        (
            'X-Content-Type-Options',
            'nosniff'
        ),
        (
            'X-Frame-Options',
            'deny'
        ),
        (
            'X-GitHub-Media-Type',
            'github.v3; format=json'
        ),
        (
            'X-GitHub-Request-Id',
            'EFC1:43DC:FE8377:27B4340:5CD2BC70'
        ),
        (
            'X-RateLimit-Limit',
            '60'
        ),
        (
            'X-RateLimit-Remaining',
            '59'
        ),
        (
            'X-RateLimit-Reset',
            '1557318273'
        ),
        (
            'X-XSS-Protection',
            '1; mode=block'
        )
    ]
)'''

snapshots['test_json_response 2'] = '''(
    {
        'documentation_url': 'https://developer.github.com/v3/activity/starring/#list-stargazers',
        'message': 'Not Found'
    },
    404,
    [
        (
            'Access-Control-Allow-Origin',
            '*'
        ),
        (
            'Access-Control-Expose-Headers',
            'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type'
        ),
        (
            'Content-Encoding',
            'gzip'
        ),
        (
            'Content-Security-Policy',
            "default-src 'none'"
        ),
        (
            'Content-Type',
            'application/json; charset=utf-8'
        ),
        (
            'Date',
            'Wed, 08 May 2019 11:24:33 GMT'
        ),
        (
            'Referrer-Policy',
            'origin-when-cross-origin, strict-origin-when-cross-origin'
        ),
        (
            'Server',
            'GitHub.com'
        ),
        (
            'Status',
            '404 Not Found'
        ),
        (
            'Strict-Transport-Security',
            'max-age=31536000; includeSubdomains; preload'
        ),
        (
            'X-Content-Type-Options',
            'nosniff'
        ),
        (
            'X-Frame-Options',
            'deny'
        ),
        (
            'X-GitHub-Media-Type',
            'github.v3; format=json'
        ),
        (
            'X-GitHub-Request-Id',
            'EFC2:5DB6:6D67D9:12DC53F:5CD2BC71'
        ),
        (
            'X-RateLimit-Limit',
            '60'
        ),
        (
            'X-RateLimit-Remaining',
            '58'
        ),
        (
            'X-RateLimit-Reset',
            '1557318273'
        ),
        (
            'X-XSS-Protection',
            '1; mode=block'
        )
    ]
)'''

snapshots['test_text_response 1'] = '''(
    '<!doctype html><html dir="rtl" itemscope="" itemtype="http://schema.org/WebPage" lang="iw"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="Q+gPYBCigqtB3vdbriEyTQ==">(function(){window.google={kEI:\\'AdHSXMn-E6eMlwShp4u4BQ\\',kEXPI:\\'0,1353746,58,50,1907,2423,698,527,730,224,510,713,352,1258,824,1069,57,528,803,214,170,467,68,2332925,329494,1294,12383,4855,32692,15247,867,12163,14324,2197,363,3320,5505,2442,260,4203,904,575,835,284,2,578,728,2432,1361,284,4041,4965,774,2256,5889,2,1968,2592,3601,669,1050,1808,1397,81,7,491,620,29,2373,7931,1288,2,4007,796,101,940,179,38,920,753,120,1217,1364,1612,2735,49,3012,2,631,1140,1422,2,4,2,670,44,4148,510,125,1160,1447,632,1097,1131,656,18,320,59,175,1331,415,143,1247,476,301,1,3,366,1016,300,705,758,96,392,29,400,376,2,614,1107,10,168,8,109,187,831,235,443,367,450,174,564,166,237,48,553,11,14,10,413,160,356,732,837,76,521,34,343,9,25,177,37,130,158,3,55,655,452,92,64,232,243,299,92,1,31,200,7,146,18,22,111,158,262,70,208,93,169,68,1,35,24,219,9,39,18,22,16,327,275,1226,85,472,72,14,10,112,226,532,89,818,260,661,506,22,2,126,1035,11,337,513,41,605,639,58,82,17,456,51,24,177,7,1,243,76,39,19,503,136,159,7,255,24,45,684,306,452,5937456,2888,33,5997514,42,2799863,4,1572,549,333,444,1,2,80,1,900,583,9,304,1,8,1,2,2132,1,1,1,1,1,414,1,748,141,59,726,3,7,563,1,2019,4,8,16,4,1,4,1,8,2,33,4,1,1\\',authuser:0,kscs:\\'c9c918f0_AdHSXMn-E6eMlwShp4u4BQ\\',kGL:\\'IL\\'};google.sn=\\'webhp\\';google.kHL=\\'iw\\';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||google.kEI};google.getLEI=function(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b};google.https=function(){return"https:"==window.location.protocol};google.ml=function(){return null};google.time=function(){return(new Date).getTime()};google.log=function(a,b,e,c,g){if(a=google.logUrl(a,b,e,c,g)){b=new Image;var d=google.lc,f=google.li;d[f]=b;b.onerror=b.onload=b.onabort=function(){delete d[f]};google.vel&&google.vel.lu&&google.vel.lu(a);b.src=a;google.li=f+1}};google.logUrl=function(a,b,e,c,g){var d="",f=google.ls||"";e||-1!=b.search("&ei=")||(d="&ei="+google.getEI(c),-1==b.search("&lei=")&&(c=google.getLEI(c))&&(d+="&lei="+c));c="";!e&&google.cshid&&-1==b.search("&cshid=")&&"slh"!=a&&(c="&cshid="+google.cshid);a=e||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+d+f+"&zx="+google.time()+c;/^http:/i.test(a)&&google.https()&&(google.ml(Error("a"),!1,{src:a,glmm:1}),a="");return a};}).call(this);(function(){google.y={};google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);google.f={};var a=window.location,b=a.href.indexOf("#");if(0<=b){var c=a.href.substring(b+1);/(^|&)q=/.test(c)&&-1==c.indexOf("#")&&a.replace("/search?"+c.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h")};</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:left}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-left:.5em;vertical-align:top}#gbar{float:right}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}\\n</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#36c}.q{color:#00c}.ts td{padding:0}.ts{border-collapse:collapse}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-right:4px}input{font-family:inherit}a.gb1,a.gb2,a.gb3,a.gb4{color:#11c !important}body{background:#fff;color:black}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#36c}a:visited{color:#551a8b}a.gb1,a.gb4{text-decoration:underline}a.gb3:hover{text-decoration:none}#ghead a.gb2:hover{color:#fff !important}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-right:13px;font-size:11px}.lsbb{background:#eee;border:solid 1px;border-color:#ccc #ccc #999 #999;height:30px}.lsbb{display:block}.ftl,#fll a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}.tiah{width:458px}</style><script nonce="Q+gPYBCigqtB3vdbriEyTQ=="></script></head><body bgcolor="#fff"><script nonce="Q+gPYBCigqtB3vdbriEyTQ==">(function(){var src=\\'/images/nav_logo229.png\\';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}\\nif (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}\\n}\\n})();</script><div id="mngb"> <div id=gbar><nobr><b class=gb1>&#1495;&#1497;&#1508;&#1493;&#1513;</b> <a class=gb1 href="https://www.google.co.il/imghp?hl=iw&tab=wi">&#1495;&#1497;&#1508;&#1493;&#1513; &#1514;&#1502;&#1493;&#1504;&#1493;&#1514;</a> <a class=gb1 href="https://maps.google.co.il/maps?hl=iw&tab=wl">&#1502;&#1508;&#1493;&#1514;</a> <a class=gb1 href="https://www.youtube.com/?gl=IL&tab=w1">YouTube</a> <a class=gb1 href="https://news.google.co.il/nwshp?hl=iw&tab=wn">&#1495;&#1491;&#1513;&#1493;&#1514;</a> <a class=gb1 href="https://mail.google.com/mail/?tab=wm">Gmail</a> <a class=gb1 href="https://drive.google.com/?tab=wo">Drive</a> <a class=gb1 href="https://www.google.com/calendar?tab=wc">&#1497;&#1493;&#1502;&#1503;</a> <a class=gb1 style="text-decoration:none" href="https://www.google.co.il/intl/iw/about/products?tab=wh"><u>&#1506;&#1493;&#1491;</u> &raquo;</a></nobr></div><div id=guser width=100%><nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a href="http://www.google.co.il/history/optout?hl=iw" class=gb4>&#1492;&#1497;&#1505;&#1496;&#1493;&#1512;&#1497;&#1497;&#1514; &#1488;&#1514;&#1512;&#1497;&#1501;</a> | <a  href="/preferences?hl=iw" class=gb4>&#1492;&#1490;&#1491;&#1512;&#1493;&#1514;</a> | <a target=_top id=gb_70 href="https://accounts.google.com/ServiceLogin?hl=iw&passive=true&continue=https://www.google.com/%3Fq%3Dformation" class=gb4>&#1499;&#1504;&#1497;&#1505;&#1492;</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0></div> </div><center><br clear="all" id="lgpd"><div id="lga"><img alt="Google" height="92" src="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png" style="padding:28px 0 14px" width="272" id="hplogo" onload="window.lol&&lol()"><br><br></div><form action="/search" name="f"><table cellpadding="0" cellspacing="0"><tr valign="top"><td width="25%">&nbsp;</td><td align="center" nowrap=""><input name="ie" value="ISO-8859-1" type="hidden"><input value="iw" name="hl" type="hidden"><input name="source" type="hidden" value="hp"><input name="biw" type="hidden"><input name="bih" type="hidden"><div class="ds" style="height:32px;margin:4px 0"><div style="position:relative;zoom:1"><input style="color:#000;margin:0;padding:5px 6px 0 8px;vertical-align:top;padding-left:38px" autocomplete="off" class="lst tiah" value="formation" title="&#1495;&#1497;&#1508;&#1493;&#1513; &#1489;-Google" maxlength="2048" name="q" size="57"><img src="/textinputassistant/tia.png" style="position:absolute;cursor:pointer;left:5px;top:4px;z-index:300" data-script-url="/textinputassistant/11/iw_tia.js" alt="" height="23" onclick="var s=document.createElement(\\'script\\');s.src=this.getAttribute(\\'data-script-url\\');(document.getElementById(\\'xjsc\\')||document.body).appendChild(s);" width="27"></div></div><br style="line-height:0"><span class="ds"><span class="lsbb"><input class="lsb" value="&#1495;&#1497;&#1508;&#1493;&#1513; &#1489;-Google" name="btnG" type="submit"></span></span><span class="ds"><span class="lsbb"><input class="lsb" value="&#1497;&#1493;&#1514;&#1512; &#1502;&#1494;&#1500; &#1502;&#1513;&#1499;&#1500;" name="btnI" onclick="if(this.form.q.value)this.checked=1; else top.location=\\'/doodles/\\'" type="submit"></span></span></td><td class="fl sblc" align="right" nowrap="" width="25%"><a href="/advanced_search?hl=iw&amp;authuser=0">&#1495;&#1497;&#1508;&#1493;&#1513; &#1502;&#1514;&#1511;&#1491;&#1501;</a><a href="/language_tools?hl=iw&amp;authuser=0">&#1499;&#1500;&#1497; &#1513;&#1508;&#1492;</a></td></tr></table><input id="gbv" name="gbv" type="hidden" value="1"><script nonce="Q+gPYBCigqtB3vdbriEyTQ==">(function(){var a,b="1";if(document&&document.getElementById)if("undefined"!=typeof XMLHttpRequest)b="2";else if("undefined"!=typeof ActiveXObject){var c,d,e=["MSXML2.XMLHTTP.6.0","MSXML2.XMLHTTP.3.0","MSXML2.XMLHTTP","Microsoft.XMLHTTP"];for(c=0;d=e[c++];)try{new ActiveXObject(d),b="2"}catch(h){}}a=b;if("2"==a&&-1==location.search.indexOf("&gbv=2")){var f=google.gbvu,g=document.getElementById("gbv");g&&(g.value=a);f&&window.setTimeout(function(){location.href=f},0)};}).call(this);</script></form><div id="gac_scont"></div><div style="font-size:83%;min-height:3.5em"><br><div id="prm"><style>.szppmdbYutt__middle-slot-promo{font-size:small;margin-bottom:32px}.szppmdbYutt__middle-slot-promo a.ZIeIlb{display:inline-block;text-decoration:none}.szppmdbYutt__middle-slot-promo img{border:none;margin-left:5px;vertical-align:middle}</style><div class="szppmdbYutt__middle-slot-promo" data-ved="0ahUKEwiJg6rt_IviAhUnxoUKHaHTAlcQnIcBCAQ"><img alt="&#1497;&#1493;&#1501; &#1492;&#1494;&#1499;&#1512;&#1493;&#1503; &#1500;&#1495;&#1500;&#1500;&#1497; &#1502;&#1506;&#1512;&#1499;&#1493;&#1514; &#1497;&#1513;&#1512;&#1488;&#1500; &#1493;&#1500;&#1504;&#1508;&#1490;&#1506;&#1497; &#1508;&#1506;&#1493;&#1500;&#1493;&#1514; &#1488;&#1497;&#1489;&#1492;" height="42" src="https://www.google.com/images/icons/hpcg/candle-white_42.png" title="&#1497;&#1493;&#1501; &#1492;&#1494;&#1499;&#1512;&#1493;&#1503; &#1500;&#1495;&#1500;&#1500;&#1497; &#1502;&#1506;&#1512;&#1499;&#1493;&#1514; &#1497;&#1513;&#1512;&#1488;&#1500; &#1493;&#1500;&#1504;&#1508;&#1490;&#1506;&#1497; &#1508;&#1506;&#1493;&#1500;&#1493;&#1514; &#1488;&#1497;&#1489;&#1492;" width="42"></div></div><div id="gws-output-pages-elements-homepage_additional_languages__als"><style>#gws-output-pages-elements-homepage_additional_languages__als{font-size:small;margin-bottom:24px}#SIvCob{display:inline-block;line-height:28px;}#SIvCob a{padding:0 3px;}.H6sW5{display:inline-block;margin:0 2px;white-space:nowrap}.z4hgWe{display:inline-block;margin:0 2px}</style><div id="SIvCob">Google &#1494;&#1502;&#1497;&#1504;&#1492; &#1489;:  <a href="https://www.google.com/setprefs?sig=0_l2XPFwtAZLP20TDJadxkDn3T8PY%3D&amp;hl=ar&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwiJg6rt_IviAhUnxoUKHaHTAlcQ2ZgBCAY">&#1575;&#1604;&#1593;&#1585;&#1576;&#1610;&#1577;</a>    <a dir="ltr" href="https://www.google.com/setprefs?sig=0_l2XPFwtAZLP20TDJadxkDn3T8PY%3D&amp;hl=en&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwiJg6rt_IviAhUnxoUKHaHTAlcQ2ZgBCAc">English</a>  </div></div></div><span id="footer"><div style="font-size:10pt"><div style="margin:19px auto;text-align:center" id="fll"><a href="/intl/iw/ads/"> &#1508;&#1512;&#1505;&#1493;&#1501; &#1489;-Google</a><a href="http://www.google.co.il/intl/iw/services/">&#1508;&#1514;&#1512;&#1493;&#1504;&#1493;&#1514; &#1506;&#1505;&#1511;&#1497;&#1497;&#1501;</a><a href="/intl/iw/about.html">&#1492;&#1499;&#1500; &#1506;&#1500; Google</a><a dir="ltr" href="https://www.google.com/setprefdomain?prefdom=IL&amp;prev=https://www.google.co.il/&amp;sig=K_LL6vBUYpTo1ZvJT4C_EbFs6-174%3D">Google.co.il</a></div></div><p style="color:#767676;font-size:8pt">&copy; 2019 - <a href="/intl/iw/policies/privacy/">&#1508;&#1512;&#1496;&#1497;&#1493;&#1514;</a> - <a href="/intl/iw/policies/terms/">&#1514;&#1504;&#1488;&#1497;&#1501;</a></p></span></center><script nonce="Q+gPYBCigqtB3vdbriEyTQ==">(function(){window.google.cdo={height:0,width:0};(function(){var a=window.innerWidth,b=window.innerHeight;if(!a||!b){var c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body;a=d.clientWidth;b=d.clientHeight}a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+google.kEI);}).call(this);})();(function(){var u=\\'/xjs/_/js/k\\\\x3dxjs.hp.en.Fm8pavzp7dw.O/m\\\\x3dsb_he,d/am\\\\x3dwKAW/rt\\\\x3dj/d\\\\x3d1/rs\\\\x3dACT90oEcFEn8bkmqEpa-2TqvyFvNpr-gPg\\';setTimeout(function(){var a=document.createElement("script");a.src=u;google.timers&&google.timers.load&&google.tick&&google.tick("load","xjsls");document.body.appendChild(a)},0);})();(function(){window.google.xjsu=\\'/xjs/_/js/k\\\\x3dxjs.hp.en.Fm8pavzp7dw.O/m\\\\x3dsb_he,d/am\\\\x3dwKAW/rt\\\\x3dj/d\\\\x3d1/rs\\\\x3dACT90oEcFEn8bkmqEpa-2TqvyFvNpr-gPg\\';})();function _DumpException(e){throw e;}\\n(function(){google.spjs=false;})();google.sm=1;(function(){var pmc=\\'{\\\\x22Qnk92g\\\\x22:{},\\\\x22RWGcrA\\\\x22:{},\\\\x22U5B21g\\\\x22:{},\\\\x22YFCs/g\\\\x22:{},\\\\x22ZI/YVQ\\\\x22:{},\\\\x22d\\\\x22:{},\\\\x22sb_he\\\\x22:{\\\\x22agen\\\\x22:true,\\\\x22cgen\\\\x22:true,\\\\x22client\\\\x22:\\\\x22heirloom-hp\\\\x22,\\\\x22dh\\\\x22:true,\\\\x22dhqt\\\\x22:true,\\\\x22ds\\\\x22:\\\\x22\\\\x22,\\\\x22ffql\\\\x22:\\\\x22en\\\\x22,\\\\x22fl\\\\x22:true,\\\\x22host\\\\x22:\\\\x22google.com\\\\x22,\\\\x22isbh\\\\x22:28,\\\\x22jsonp\\\\x22:true,\\\\x22msgs\\\\x22:{\\\\x22cibl\\\\x22:\\\\x22&#1504;&#1511;&#1492; &#1495;&#1497;&#1508;&#1493;&#1513;\\\\x22,\\\\x22dym\\\\x22:\\\\x22&#1492;&#1488;&#1501; &#1492;&#1514;&#1499;&#1493;&#1493;&#1504;&#1514; &#1500;:\\\\x22,\\\\x22lcky\\\\x22:\\\\x22&#1497;&#1493;&#1514;&#1512; &#1502;&#1494;&#1500; &#1502;&#1513;&#1499;&#1500;\\\\x22,\\\\x22lml\\\\x22:\\\\x22&#1500;&#1502;&#1497;&#1491;&#1506; &#1504;&#1493;&#1505;&#1507;\\\\x22,\\\\x22oskt\\\\x22:\\\\x22&#1499;&#1500;&#1497; &#1492;&#1494;&#1504;&#1492;\\\\x22,\\\\x22psrc\\\\x22:\\\\x22&#1495;&#1497;&#1508;&#1493;&#1513; &#1494;&#1492; &#1492;&#1493;&#1505;&#1512; &#1502;\\\\\\\\u003Ca href\\\\x3d\\\\\\\\\\\\x22/history\\\\\\\\\\\\x22\\\\\\\\u003E&#1492;&#1497;&#1505;&#1496;&#1493;&#1512;&#1497;&#1497;&#1514; &#1492;&#1488;&#1497;&#1504;&#1496;&#1512;&#1504;&#1496;\\\\\\\\u003C/a\\\\\\\\u003E &#1513;&#1500;&#1498;\\\\x22,\\\\x22psrl\\\\x22:\\\\x22&#1492;&#1505;&#1512;\\\\x22,\\\\x22sbit\\\\x22:\\\\x22&#1495;&#1497;&#1508;&#1493;&#1513; &#1500;&#1508;&#1497; &#1514;&#1502;&#1493;&#1504;&#1492;\\\\x22,\\\\x22srch\\\\x22:\\\\x22&#1495;&#1497;&#1508;&#1493;&#1513; &#1489;-Google\\\\x22},\\\\x22ovr\\\\x22:{},\\\\x22pq\\\\x22:\\\\x22formation\\\\x22,\\\\x22refpd\\\\x22:true,\\\\x22rfs\\\\x22:[],\\\\x22sbpl\\\\x22:24,\\\\x22sbpr\\\\x22:24,\\\\x22scd\\\\x22:10,\\\\x22sce\\\\x22:5,\\\\x22stok\\\\x22:\\\\x228sgkZUJfBetMnwoe0RUzw32URio\\\\x22,\\\\x22uhde\\\\x22:false}}\\';google.pmc=JSON.parse(pmc);})();</script>        </body></html>',
    200,
    [
        (
            'alt-svc',
            'quic=":443"; ma=2592000; v="46,44,43,39"'
        ),
        (
            'cache-control',
            'private, max-age=0'
        ),
        (
            'content-encoding',
            'gzip'
        ),
        (
            'content-type',
            'text/html; charset=ISO-8859-1'
        ),
        (
            'date',
            'Wed, 08 May 2019 12:52:17 GMT'
        ),
        (
            'expires',
            '-1'
        ),
        (
            'p3p',
            'CP="This is not a P3P policy! See g.co/p3phelp for more info."'
        ),
        (
            'server',
            'gws'
        ),
        (
            'set-cookie',
            '1P_JAR=2019-05-08-12; expires=Fri, 07-Jun-2019 12:52:17 GMT; path=/; domain=.google.com, NID=183=XmsEVYPIN_V25aoDL0ZZkSZ-d2K4TSDhWSFoFnY69aBRLTpmVpVgJN84tYtx13CnMEDV7PntuOx_yOauqaPeFUTQCpl4jKwfEx97Y-d9k8imTphu11DT3J7mkA_c1kKNj42qYHU2XZWaQGEd0vJUGrpP5970fxdelHBZ34cvhQU; expires=Thu, 07-Nov-2019 12:52:17 GMT; path=/; domain=.google.com; HttpOnly'
        ),
        (
            'x-frame-options',
            'SAMEORIGIN'
        ),
        (
            'x-xss-protection',
            '0'
        )
    ]
)'''

snapshots['test_xmldict_response 1'] = '''(
    {
        'slideshow': {
            '@author': 'Yours Truly',
            '@date': 'Date of publication',
            '@title': 'Sample Slide Show',
            'slide': [
                {
                    '@type': 'all',
                    'title': 'Wake up to WonderWidgets!'
                },
                {
                    '@type': 'all',
                    'item': [
                        {
                            '#text': 'Why  are great',
                            'em': 'WonderWidgets'
                        },
                        None,
                        {
                            '#text': 'Who  WonderWidgets',
                            'em': 'buys'
                        }
                    ],
                    'title': 'Overview'
                }
            ]
        }
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
            '295'
        ),
        (
            'content-type',
            'application/xml'
        ),
        (
            'date',
            'Wed, 08 May 2019 12:54:29 GMT'
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

snapshots['test_responses_sad 1'] = '''(
    None,
    None,
    None
)'''

snapshots['test_responses_sad 2'] = '''(
    None,
    None,
    None
)'''

snapshots['test_responses_sad 3'] = '''(
    None,
    None,
    None
)'''

snapshots['test_responses_sad 4'] = '''(
    None,
    None,
    None
)'''

snapshots['test_responses_sad 5'] = '''(
    None,
    None,
    None
)'''
