# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from enum import Enum

from scaleway_core.utils import (
    StrEnumMeta,
)


class LanguageCode(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_LANGUAGE_CODE = "unknown_language_code"
    EN_US = "en_us"
    FR_FR = "fr_fr"
    DE_DE = "de_de"

    def __str__(self) -> str:
        return str(self.value)
