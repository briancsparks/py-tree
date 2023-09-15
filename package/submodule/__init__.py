#!/usr/bin/env python3

# Initialize package-level variables if needed

# Import key functions/classes for easier access
from .math_operations import add, subtract
from .string_operations import concatenate

# Define what gets imported with "from package import *"
__all__ = ["add", "subtract", "concatenate"]

