import importlib
import pkgutil
from typing import TypeVar, cast

T = TypeVar("T")


class ModuleUtility:
    """Simple utility for extracting typed attributes from submodules.

    Provides .NET-like generic method syntax: ModuleUtility.get<T>(package, attribute)
    """

    @staticmethod
    def get(target_type: type[T], package_name: str, attribute_name: str) -> list[T]:
        """Get all attributes of specified type from submodules.

        Usage:
            routers = ModuleUtility.get(APIRouter, "api.routers.v1", "router")
            services = ModuleUtility.get(BaseService, "services", "service")

        Args:
            target_type: The expected type of the attributes (like <T> in .NET)
            package_name: Package to scan for submodules
            attribute_name: Attribute name to extract from each module

        Returns:
            List of found attributes with proper typing
        """
        package = importlib.import_module(package_name)
        items: list[T] = []

        for _, module_name, _ in pkgutil.iter_modules(package.__path__):
            module = importlib.import_module(f"{package_name}.{module_name}")
            if hasattr(module, attribute_name):
                attribute = getattr(module, attribute_name)
                # Runtime type checking for safety
                if isinstance(attribute, target_type):
                    items.append(cast(T, attribute))

        return items
