######
## Justification prepared_framework
######
from typing import Callable

from jpipe_runner.framework.decorators.jpipe_decorator import jpipe  # type: ignore


## Strategy verify_prepfram_available
def verifying_preparedness_framework_availability() -> bool:
    return True


## Evidence prepfram_tracked_categories
@jpipe(consume=["tracked_categories"], produce=["tracked_categories_list"])  # type: ignore
def track_categories_list(
    tracked_categories: list[str], produce: Callable[[str, list[str]], None]
) -> bool:
    produce("tracked_categories_list", tracked_categories)
    return True


## Evidence prepfram_document
@jpipe(consume=["framework_document_url"], produce=["framework_document_is_present"])  # type: ignore
def preparedness_framework_document(
    framework_document_url: str, produce: Callable[[str, bool], None]
) -> bool:
    return True
