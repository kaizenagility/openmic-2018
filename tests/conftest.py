import pytest

import glob
import os


@pytest.fixture()
def data_dir():
    return os.path.join(os.path.dirname(__file__), 'data')


@pytest.fixture()
def audio_file(data_dir):
    return os.path.join(data_dir, 'audio', '000046_3840.ogg')


@pytest.fixture()
def empty_audio_file(data_dir):
    return os.path.join(data_dir, 'audio', 'empty.wav')


@pytest.fixture()
def tfrecords(data_dir):
    return glob.glob(os.path.join(data_dir, 'tfrecords', '*.tfrecord'))
