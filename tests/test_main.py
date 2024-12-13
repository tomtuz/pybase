import os
from collections.abc import Generator
from unittest.mock import patch

import pytest

from core.main import get_config, validate_config


@pytest.fixture
def mock_env_vars() -> Generator[None, None, None]:
    """Fixture to provide a clean environment for each test"""
    with patch.dict(os.environ, {}, clear=True):
        yield


def test_get_config_defaults(mock_env_vars: None) -> None:
    """Test get_config returns correct defaults when no env vars are set"""
    config = get_config()
    assert config == {
        "debug": False,
        "api_key": None,
        "database_url": None,
        "env": "development",
    }


def test_get_config_with_values(mock_env_vars: None) -> None:
    """Test get_config returns correct values from environment"""
    test_values = {
        "DEBUG": "true",
        "API_KEY": "test-key",
        "DATABASE_URL": "postgresql://test",
        "ENV": "production",
    }
    with patch.dict(os.environ, test_values):
        config = get_config()
        assert config == {
            "debug": True,
            "api_key": "test-key",
            "database_url": "postgresql://test",
            "env": "production",
        }


def test_validate_config_development() -> None:
    """Test config validation in development environment"""
    config = {
        "debug": False,
        "api_key": None,  # Missing API key in development is OK
        "database_url": None,  # Missing DB URL in development is OK
        "env": "development",
    }
    # Should not raise any exceptions in development
    validate_config(config)


def test_validate_config_production_missing_api_key() -> None:
    """Test config validation fails in production with missing API key"""
    config = {
        "debug": False,
        "api_key": None,  # Missing API key in production should fail
        "database_url": "postgresql://test",
        "env": "production",
    }
    with pytest.raises(ValueError, match="API key is required in production"):
        validate_config(config)


def test_validate_config_production_missing_db_url() -> None:
    """Test config validation fails in production with missing database URL"""
    config = {
        "debug": False,
        "api_key": "test-key",
        "database_url": None,  # Missing DB URL in production should fail
        "env": "production",
    }
    with pytest.raises(ValueError, match="Database URL is required in production"):
        validate_config(config)


def test_validate_config_production_valid() -> None:
    """Test config validation passes in production with all required values"""
    config = {
        "debug": False,
        "api_key": "test-key",
        "database_url": "postgresql://test",
        "env": "production",
    }
    # Should not raise any exceptions
    validate_config(config)
