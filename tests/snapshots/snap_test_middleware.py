# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots[
    "test_middleware_default 1"
] = """[<function request_id_middleware at 0x10dbbcf50>, <function context_middleware at 0x10dbbc320>, <function request_duration_middleware at 0x10dbbccf8>, <function request_logger_middleware at 0x10dbbca28>]"""
