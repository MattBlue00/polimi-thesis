from typing import List

from experiments.errors.generic_error import GenericError

class SolveDependencyError(GenericError):
    """Raised when you try to solve a dependency you aren't supposed to solve."""
    def __init__(self, causing_dependency_ids: List[str], dependent_ids: List[str], reason: str) -> None:
        causing_dependency_str = ", ".join(causing_dependency_ids)
        dependent_str = ', '.join(dependent_ids)
        message = f"You cannot solve the dependency between {causing_dependency_str} and dependent {dependent_str} because {reason}."
        super().__init__(message)