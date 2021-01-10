import pytest


@pytest.fixture()
def env_data():
    with open(".env") as f:
        lines = f.read().split("\n")
        list_variable = []
        for line in lines:
            variable_name = line.split("=")[0]
            list_variable.append(variable_name)

    return list_variable


@pytest.fixture()
def env_example_data():
    with open(".env.example") as f:
        lines = f.read().split("\n")
        list_variable = []
        for line in lines:
            variable_name = line.split("=")[0]
            list_variable.append(variable_name)

    return list_variable


def test_variable_name_in_env_is_uppercase(env_data):
    """check used name of variable are uppercase"""
    for variable in env_data:
        assert variable.upper() == variable, f"{variable} isn't uppercase"


def test_variable_name_in_env_example_is_uppercase(env_example_data):
    """check used name of variable are uppercase"""
    for variable in env_example_data:
        assert variable.upper() == variable, f"{variable} isn't uppercase"


def test_compare_variable_name_of_env_and_env_example_files(env_data, env_example_data):
    """
    check both of file - .env.example and .env have that same name of variables
    """
    env_data.sort()
    env_example_data.sort()
    for variable in env_data:
        assert (
            variable in env_example_data
        ), f"{variable} is not exist in .env.example file"
        assert env_data.count(variable) == 1, f"{variable} is duplicated in .env"

    for variable in env_example_data:
        assert variable in env_data, f"{variable} is not exist in .env file"
        assert (
            env_example_data.count(variable) == 1
        ), f"{variable} is duplicated in .env.example"
