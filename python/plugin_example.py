import importlib
from abc import ABC, abstractmethod

# 1. Define the Plugin Interface
class Plugin(ABC):
    """
    Abstract base class that all plugins must inherit from.
    Enforces a structure for any plugin created.
    """
    @abstractmethod
    def run(self, data):
        """The main method the plugin must implement."""
        pass

    @property
    @abstractmethod
    def name(self):
        """A name for the plugin."""
        pass

# 2. Define the Plugin Manager
class PluginManager:
    def __init__(self):
        self._plugins = []

    def register_plugin(self, plugin: Plugin):
        """Register a new plugin instance."""
        if not isinstance(plugin, Plugin):
            print(f"Error: {plugin} is not a valid Plugin.")
            return
        
        print(f"-> Registered plugin: {plugin.name}")
        self._plugins.append(plugin)

    def execute_plugins(self, data):
        """Run the 'run' method on all registered plugins."""
        print(f"\nRunning plugins on data: '{data}'")
        print("-" * 30)
        for plugin in self._plugins:
            try:
                plugin.run(data)
            except Exception as e:
                print(f"Error in {plugin.name}: {e}")
        print("-" * 30)

# 3. Implement Concrete Plugins
class GreetingPlugin(Plugin):
    @property
    def name(self):
        return "Greeting Plugin"

    def run(self, data):
        print(f"[{self.name}] Hello, {data}!")

class UpperCasePlugin(Plugin):
    @property
    def name(self):
        return "All Caps Plugin"

    def run(self, data):
        result = str(data).upper()
        print(f"[{self.name}] Converted: {result}")

class WordCountPlugin(Plugin):
    @property
    def name(self):
        return "Word Counter"

    def run(self, data):
        count = len(str(data).split())
        print(f"[{self.name}] Word count: {count}")

# 4. Main Execution
if __name__ == "__main__":
    # Create the manager
    manager = PluginManager()

    # Create instances of our plugins
    p1 = GreetingPlugin()
    p2 = UpperCasePlugin()
    p3 = WordCountPlugin()

    # Register them
    manager.register_plugin(p1)
    manager.register_plugin(p2)
    manager.register_plugin(p3)

    # Run the system
    manager.execute_plugins("Python Plugin System")
