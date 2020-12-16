# encoding: utf-8

# Standard Library
from abc import ABC
from abc import abstractmethod

# 3rd Party Library
# Current Folder
# Current Application

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


class FeatureToggle(ABC):
    """
    Feature Toggle interface.
    """

    @abstractmethod
    def toggle(self, name: str) -> bool:
        """
        Toggle the feature.

        Parameters:
            name: The identification name of the feature

        Returns:
            True if the feature has been toggled, False otherwise.
        """
        pass

    @abstractmethod
    def is_active(self, name: str) -> bool:
        """
        Indicates if feature is active or not.

        Parameters:
            name: The identification name of the feature

        Returns:
            True if the feature is active, False otherwise.
        """
        pass
