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
