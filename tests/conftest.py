import os, pytest

from nornir import InitNornir
from nornir.core.state import GlobalState
from enum import Enum

global_data = GlobalState(dry_run=True)


@pytest.fixture(scope="session", autouse=True)
def nr(request):
    """Initializes nornir"""
    dir_path = os.path.dirname(os.path.realpath(__file__))

    nornir = InitNornir(
        inventory={
            "plugin": "SimpleInventory",
            "options": {
                "host_file": f"{dir_path}/inventory_data/hosts.yaml",
                "group_file": f"{dir_path}/inventory_data/groups.yaml",
                "defaults_file": f"{dir_path}/inventory_data/defaults.yaml",
            },
        },
        dry_run=True,
    )
    nornir.data = global_data
    return nornir


@pytest.fixture(scope="function", autouse=True)
def reset_data():
    global_data.dry_run = True
    global_data.reset_failed_hosts()


class NestedDataMap(Enum):
    """Enum Extended Class Example with a NESTED_DICT option."""

    NESTED_DICT = 0
    SYSTEM_NAME = 2


class DataMap(Enum):
    """Enum Extended Class Example."""

    NESTED_DICT = 0
    SYSTEM_NAME = 2