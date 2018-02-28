#!/usr/bin/env python3
"""
Exercises example Acumos model onboarded to DCAE via message router
"""
import time
import uuid
import json
from threading import Thread

import requests


def send(data):
    '''Publishes a dict on the test subscribe topic'''
    body = _make_body(data)

    topic = 'com.att.dcae.dmaap.SOLN.AcumosTopic1'
    server = 'http://aggsolmrtr01.dcae.solutioning.homer.att.com:3904'
    username = 'm14983@onapClient1.att.com'
    password = 'uhana.io1'

    resp = requests.post('{0}/events/{1}'.format(server, topic),
                         auth=(username, password),
                         headers={'Content-Type': 'application/cambria'},
                         data=body)
    resp.raise_for_status()


def _make_body(data):
    '''Creates a message router body'''
    key = uuid.uuid4().hex
    data = json.dumps(data)
    body = '{0}.{1}.{2}{3}'.format(len(key), len(data), key, data)
    return body


def get():
    '''Subscribes to the test publish topic and returns the model output dict'''
    groupid = uuid.uuid4().hex
    clientid = uuid.uuid4().hex
    topic = 'com.att.dcae.dmaap.SOLN.AcumosTopic2'
    server = 'http://aggsolmrtr01.dcae.solutioning.homer.att.com:3904'
    username = 'm14984@onapClient2.att.com'
    password = 'uhana.io2'

    resp = requests.get('{0}/events/{1}/{2}/{3}?timeout=15000&limit=5'.format(server, topic, groupid, clientid),
                        auth=(username, password))
    resp.raise_for_status()

    json_list = resp.json()
    return None if not json_list else json.loads(json_list[0])


if __name__ == '__main__':
    '''Test area'''

    # create sample data for adder model
    input_data = {'x': 1, 'y': 2}
    output_data = {'result': '3'}

    # create listener that populates list of responses received from model output
    resps = []

    def listener(n=5):
        '''Listens for multiple messages and populates the resps list'''
        for _ in range(n):
            resp = get()
            resps.append(resp)
            if resp == output_data:
                break

    # start listener before sending data
    thread = Thread(target=listener)
    thread.start()

    # allow a short period of time for the listener to run, then send input data
    time.sleep(3)
    send(input_data)

    # wait for thread to terminate, either by receiving correct data or exhaustive checking
    thread.join()

    assert any(r == output_data for r in resps), "Did not receive any expected model output: {}".format(resps)
