from typing import List

from experiments.errors.generic_error import GenericError

class SolveDependencyError(GenericError):
    """Raised when you try to solve a dependency you aren't supposed to solve."""
    def __init__(self, causing_dependency: str, dependent: List[str], reason: str) -> None:
        dependent_str = ', '.join(dependent)
        message = f"You cannot solve the dependency between {causing_dependency} and dependent {dependent_str} because {reason}."
        super().__init__(message)