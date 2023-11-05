import pytest
from src.instantiate_csv_error import *


def test_instantiate_csv_error():
    inst_error = InstError([1, 2, 3])
    assert inst_error.field_name == [1, 2, 3]
    with pytest.raises(InstantiateCSVError):
        InstError([10, 25])
