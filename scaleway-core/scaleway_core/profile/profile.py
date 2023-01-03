from __future__ import annotations

import dataclasses
import logging
import os
from dataclasses import dataclass
from typing import Optional, Type, TypeVar

import yaml

from scaleway_core import __version__
from scaleway_core.profile.file import CONFIG_PROPERTIES_TO_PROFILE

from .env import ENV_KEY_SCW_CONFIG_PATH, ENV_VARIABLES_TO_PROFILE


@dataclass
class ProfileDefaults:
    default_organization_id: Optional[str] = None
    """
    Your organization ID is the identifier of your account inside Scaleway infrastructure.
    """

    default_project_id: Optional[str] = None
    """
    Your project ID is the identifier of the project your resources are attached to.
    """

    default_region: Optional[str] = None
    """
    A region is represented as a geographical area such as France (Paris) or the Netherlands (Amsterdam).
    It can contain multiple availability zones.

    Examples: fr-par, nl-ams.
    """

    default_zone: Optional[str] = None
    """
    A region can be split into many availability zones (AZ).
    Latency between multiple AZ of the same region are low as they have a common network layer.

    Examples: fr-par-1, nl-ams-1
    """

    default_page_size: Optional[int] = None
    """
    The default number of results when requesting a paginated resource.
    """


@dataclass
class ProfileConfig:
    access_key: Optional[str] = None
    """
    You need an access key and a secret key to connect to Scaleway API.
    Generate your access key at the following address: https://console.scaleway.com/project/credentials.
    """

    secret_key: Optional[str] = None
    """
    The secret key is the value that can be used to authenticate against the API (the value used in X-Auth-Token HTTP-header).
    The secret key MUST remain secret and not given to anyone or published online.
    Generate your secret key at the following address: https://console.scaleway.com/project/credentials.
    """

    api_url: str = "https://api.scaleway.com"
    """
    The Scaleway API URL.
    Change that if you want to direct requests to a different endpoint.
    """

    api_allow_insecure: bool = False
    """
    Allow insecure connection to the API.
    """

    user_agent: str = f"scaleway-sdk-python/{__version__}"
    """
    The User-Agent sent with each request.
    """


ProfileSelf = TypeVar("ProfileSelf", bound="Profile")


@dataclass
class Profile(ProfileDefaults, ProfileConfig):
    @classmethod
    def merge(cls: Type[ProfileSelf], other: ProfileSelf) -> ProfileSelf:
        """
        Create a new profile by merging the current profile with another one.
        """
        fields = dataclasses.fields(Profile)
        merged = {}

        for field in fields:
            merged[field.name] = getattr(cls, field.name) or getattr(other, field.name)

        return cls(**merged)

    @classmethod
    def from_env(cls: Type[ProfileSelf]) -> ProfileSelf:
        """
        Loads profile from environment variables.
        """
        profile = cls()
        for env_variable, profile_property in ENV_VARIABLES_TO_PROFILE.items():
            value = os.environ.get(env_variable)
            if value is not None:
                setattr(profile, profile_property, value)

        return profile

    @classmethod
    def get_default_config_directory(cls) -> str:
        xdg_config_path = os.environ.get("XDG_CONFIG_HOME")
        if xdg_config_path is not None and xdg_config_path != "":
            return os.path.join(xdg_config_path, "scw")

        return os.path.join(os.path.expanduser("~"), ".config", "scw")

    @classmethod
    def get_default_config_file_path(cls, filepath: Optional[str] = None) -> str:
        if filepath is not None:
            return filepath

        filepath = os.environ.get(ENV_KEY_SCW_CONFIG_PATH)
        if filepath is not None and filepath != "":
            return filepath

        return os.path.join(Profile.get_default_config_directory(), "config.yaml")

    @classmethod
    def from_config_file(
        cls: Type[ProfileSelf],
        filepath: Optional[str] = None,
        profile_name: Optional[str] = "default",
    ) -> ProfileSelf:
        filepath = cls.get_default_config_file_path(filepath)

        with open(filepath, "r") as f:
            config = yaml.safe_load(f)

            if type(config) is not dict:
                raise ValueError("Invalid config file")

            profile = cls()
            for file_property, profile_property in CONFIG_PROPERTIES_TO_PROFILE.items():
                value = config.get(file_property)
                if value is not None:
                    setattr(profile, profile_property, value)

            if profile_name is not None and profile_name != "default":
                has_profile = (
                    "profiles" in config
                    and type(config["profiles"]) is dict
                    and profile_name in config["profiles"]
                )

                if not has_profile:
                    raise ValueError(f"Profile '{profile_name}' not found")

                overrides = config["profiles"][profile_name]

                if type(overrides) is not dict:
                    raise ValueError(f"Invalid profile '{profile_name}'")

                for (
                    file_property,
                    profile_property,
                ) in CONFIG_PROPERTIES_TO_PROFILE.items():
                    value = overrides.get(file_property)
                    if value is not None:
                        setattr(profile, profile_property, value)

            return profile

    @classmethod
    def from_config_file_and_env(
        cls: Type[ProfileSelf],
        filepath: Optional[str] = None,
        profile_name: Optional[str] = "default",
    ) -> ProfileSelf:
        """
        Loads profile from a config file and environment variables.

        Environment variables override config file.
          - If config file is not found, the profile is still loaded from environment variables.
          - If you want it to throw an error in case of missing or invalid config file, use `Profile.from_config_file` and `Profile.from_env` instead.
        """
        profile = cls.from_env()

        try:
            a = cls.from_config_file(filepath, profile_name)
            return profile.merge(a)
        except Exception as e:
            print(e)
            return profile
