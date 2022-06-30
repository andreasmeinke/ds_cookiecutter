""" This module provides the applications settings
"""

from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    """This class provides the applications settings
    Values are automatically loaded from env and from the `.env`-file
    """

    # add project relevant env variables here e.g.
    # model_path = "path/to/model/model.bin"
    # the entries below are mandatory

    origin: Optional[str] = None
    api_version: str

    """Current version of the API, `local` for local, commit hash (sha256) on develop,
       and tag-based for release versions
    """

    class Config:
        """This class provides the config for the applications settings"""

        env_file = ".env"
