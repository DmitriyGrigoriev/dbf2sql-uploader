"""
Global exception and warning classes.
"""
class SuspiciousOperation(Exception):
    """The user did something suspicious"""

class SuspiciousFileOperation(SuspiciousOperation):
    """A Suspicious filesystem operation was attempted"""
    pass

class ImproperlyConfigured(Exception):
    """App is somehow improperly configured"""
    pass
