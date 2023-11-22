from lib.mocking_bites_four import *
from unittest.mock import Mock

# returns the difference between my computer time x the time from the API get

def test_the_current_time():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime":1700656113}
    time_mock = Mock()
    time_mock.time.return_value = 1700656113
    time_difference = TimeError(requester_mock, time_mock)  
    assert time_difference.error() == 0


def test_cat_fact_return_somethign():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"fact": "Baking chocolate is the most dangerous chocolate to your cat."}
    final_message = CatFacts(requester_mock)
    assert final_message.provide() == "Cat fact: Baking chocolate is the most dangerous chocolate to your cat."