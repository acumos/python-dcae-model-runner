# -*- coding: utf-8 -*-
# ===============LICENSE_START=======================================================
# Acumos Apache-2.0
# ===================================================================================
# Copyright (C) 2017-2018 AT&T Intellectual Property & Tech Mahindra. All rights reserved.
# ===================================================================================
# This Acumos software file is distributed by AT&T and Tech Mahindra
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============LICENSE_END=========================================================
'''
Provides model runner tests
'''
import time
import os
import json
import contextlib
from tempfile import TemporaryDirectory
from collections import defaultdict
from datetime import datetime, timedelta

import pytest
from mock import patch, MagicMock, call as MockCall

from acumos.modeling import Model
from acumos.session import AcumosSession
from acumos.wrapped import load_model

from acumos_dcae_model_runner.runner import ModelRunner, _init_runner, _GETDATA_TIMEOUT_MS


def test_runner():
    '''Tests ModelRunner and ModelMethod basic usage'''

    get_data = MagicMock()
    get_data.return_value = json.dumps({'x': 1, 'y': 2})

    send_data = MagicMock()

    with _mock_model() as model:
        config = None
        runner = ModelRunner(model, get_data, send_data, config)

        methods = {method.name: method for method in runner._methods}
        assert len(methods) == 2

        add_method = methods['add']
        add_method.process()

        mult_method = methods['multiply']
        mult_method.process()

        get_calls = _segment_calls(get_data.call_args_list)
        assert get_calls['add_subscriber'] == [MockCall('add_subscriber', _GETDATA_TIMEOUT_MS), ]
        assert get_calls['multiply_subscriber'] == [MockCall('multiply_subscriber', _GETDATA_TIMEOUT_MS), ]

        # need to convert send_data call json back to dict for evaluation
        send_calls = _segment_calls(send_data.call_args_list)
        add_calls = [(c[0][0], c[0][1], json.loads(c[0][2])) for c in send_calls['add_publisher']]
        mult_calls = [(c[0][0], c[0][1], json.loads(c[0][2])) for c in send_calls['multiply_publisher']]

        assert add_calls == [('add_publisher', 'group1', {'value': '3'}), ]
        assert mult_calls == [('multiply_publisher', 'group1', {'value': '2'}), ]


def test_run_model():
    '''Tests the _init_runner helper and expected usage of threaded ModelRunner'''

    def get_data(key, timeout):
        '''Mocks the DCAE env get_data method'''
        time.sleep(0.2)  # simulate delay
        return json.dumps({'x': 1, 'y': 2})

    mock_env = MagicMock()
    mock_env.getdata.side_effect = get_data

    config = {'foo': 1}
    mock_env.getconfig.return_value = config

    mock_dcaeenv = MagicMock()
    mock_dcaeenv.return_value = mock_env

    with _mock_model(yield_model=False) as model_dir, patch('acumos_dcae_model_runner.runner.DcaeEnv', mock_dcaeenv):
        runner, dcae = _init_runner(model_dir)

        assert all(m._config == config for m in runner._methods)  # all methods should have initial config

        # runner has not been started
        assert runner.health_check() is False
        assert dcae._health_check() is False

        runner.start()

        # simulate new dcae config
        new_config = {'foo': 2}
        mock_env.getconfig.return_value = new_config
        dcae._on_config()
        assert all(m._config == new_config for m in runner._methods)

        _wait(mock_env.getdata, ('add_subscriber', 'multiply_subscriber'))  # blocks until enough calls are made, otherwise raises TimeoutError

        # threads should be running
        assert runner.health_check() is True
        assert dcae._health_check() is True

        runner.stop()  # blocks until threads are joined

        # threads should be stopped
        assert runner.health_check() is False
        assert dcae._health_check() is False

        # there should be an equal number of send_data and get_data calls
        get_calls = _segment_calls(mock_env.getdata.call_args_list)
        send_calls = _segment_calls(mock_env.senddata.call_args_list)
        assert len(send_calls['add_publisher']) == len(get_calls['add_subscriber'])
        assert len(send_calls['multiply_publisher']) == len(get_calls['multiply_subscriber'])


@contextlib.contextmanager
def _mock_model(yield_model=True):
    '''Context manager that yields an acumos.wrapped.WrappedModel model for testing purposes'''
    def add(x: int, y: int) -> int:
        return x + y

    def multiply(x: int, y: int) -> int:
        return x * y

    model = Model(add=add, multiply=multiply)

    session = AcumosSession()
    with TemporaryDirectory() as tdir:
        session.dump(model, 'test-model', tdir)
        model_dir = os.path.join(tdir, 'test-model')
        wrapped_model = load_model(model_dir)
        yield wrapped_model if yield_model else model_dir


def _wait(mock, keys, step=0.25, count=5, timeout=5):
    '''Periodically checks mock object for `count` number of calls every `step` seconds until timeout'''
    stop_time = datetime.now() + timedelta(seconds=timeout)
    while datetime.now() < stop_time:
        calls = _segment_calls(mock.call_args_list)
        if all(len(calls[key]) >= count for key in keys):
            return
        time.sleep(step)
    raise TimeoutError()


def _segment_calls(calls):
    '''Returns a dict of segmented calls'''
    dd = defaultdict(list)
    for call in calls:
        key = call[0][0]
        dd[key].append(call)
    return dd


if __name__ == '__main__':
    '''Test area'''
    pytest.main([__file__, ])
