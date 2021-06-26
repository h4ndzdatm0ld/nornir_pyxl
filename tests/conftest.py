"""Conftest for Nornir_Pyxl UnitTests."""
import os
from enum import Enum
import pytest

from nornir import InitNornir
from nornir.core.state import GlobalState

global_data = GlobalState(dry_run=True)
DIR_PATH = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture(scope="session", autouse=True)
def nornir():
    """Initializes nornir"""
    nr_nr = InitNornir(
        inventory={
            "plugin": "SimpleInventory",
            "options": {
                "host_file": f"{DIR_PATH}/inventory_data/hosts.yaml",
                "group_file": f"{DIR_PATH}/inventory_data/groups.yaml",
                "defaults_file": f"{DIR_PATH}/inventory_data/defaults.yaml",
            },
        },
        logging={
            "log_file": f"{DIR_PATH}/unit/test_data/nornir_test.log",
            "level": "DEBUG",
        },
        dry_run=True,
    )
    nr_nr.data = global_data
    return nr_nr


@pytest.fixture(scope="function", autouse=True)
def reset_data():
    """Reset Data."""
    global_data.dry_run = True
    global_data.reset_failed_hosts()


@pytest.fixture
def nested_dict():
    """Return a nested dict inside a list as a fixture."""
    return [{"Q345501": {"SYSTEM_NAME": "PHNZAZ -635696-01"}}]


@pytest.fixture
def list_of_dicts():
    """Return a simple list of dictionaries."""
    return [
        {"CLLI": "PHNZAZ", "SITE_ID": "Q345501", "SYSTEM_NAME": "PHNZAZ -635696-01"}
    ]


@pytest.fixture
def get_success_ez_data():
    """Results of loading a successfull ez data task."""
    return {
        "site_id": "Q345501",
        "clli": "PHNZAZ",
        "system_name": "PHNZAZ -635696-01",
        "ntp_server_1_ip": "192.168.1.100",
        "ntp_server_2_ip": "192.168.1.102/32",
        "ntp_server_3_ip": "192.168.100.3",
        "ntp_server_4_ip": "time.ntp.com",
    }


@pytest.fixture
def get_success_ez_data_bad_wb():
    """Results of loading a successfull ez data task, even with poor populated data.."""
    return [
        {
            "site_id": "Q345501",
            "clli": "PHNZAZ",
            "8digit_code": 635696,
            "system_name": "PHNZAZ -635696-01",
            "system_location": "Phoenix, Arizona",
            "system_contact": "‘John Doe’",
            "system_time_zone": "EST",
            "dst_zone": "EST",
            "ntp_server_1_ip": "192.168.100.1",
        }
    ]


class NestedDataMap(Enum):
    """Enum Extended Class Example with a NESTED_DICT option."""

    NESTED_DICT = 0
    SYSTEM_NAME = 2


class DataMap(Enum):
    """Enum Extended Class Example."""

    SITE_ID = 0
    CLLI = 1
    SYSTEM_NAME = 2
