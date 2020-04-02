# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Utility functions not specific to any submodule.
"""

import logging
from configparser import ConfigParser
from functools import wraps
from typing import Callable

PROGRAM_ROOT_LOGGER_NAME = "gcsfast"

def validate_log_level(level: str) -> bool:
    """Test whether a log level is valid.

    Arguments:
        level {str} -- The log level to test.

    Returns:
        bool -- True if the log level is valid.
    """
    return hasattr(logging, level)


def set_program_log_level(command_line_arg,
                          config: ConfigParser = None) -> None:
    """Set the log level for the root logger for this program.

    Arguments:
        args {Namespace} -- Arguments given to program execution.
        config {ConfigParser} -- Configuration given to the program.

    Returns:
        None
    """
    program_root_logger = logging.getLogger(PROGRAM_ROOT_LOGGER_NAME)
    level = 'INFO'  # Default log level
    set_by = 'default'
    if config and config.get('RUNTIME', 'LOG_LEVEL', fallback=None):
        # Config file should override the default
        candidate = config['RUNTIME']['LOG_LEVEL']
        if validate_log_level(candidate):
            level = candidate
            set_by = 'config file'
        else:
            print("Invalid log level from config file: {}".format(candidate))
    if command_line_arg:
        # Argument should override the config file and the default
        candidate = command_line_arg
        if validate_log_level(candidate):
            level = candidate
            set_by = 'command line argument'
        else:
            print("Invalid log level from command line: {}".format(candidate))
    program_root_logger.setLevel(level)
    print("Log level is {}, set by {}".format(level, set_by))


def memoize(func: Callable) -> Callable:
    """Decorator to memoize a function.

    Arguments:
        func {func} -- The function to memoize.

    Returns:
        func -- A function with results cached for specific arguments.
    """
    # Define the dictionary for memoized responses
    memos = func.memos = {}

    @wraps(func)
    def memoized(*args, **kwargs):
        # devise a key based on string representation of arguments given
        # in this function call
        call = str(args) + str(kwargs)
        # if the result isn't stored, call the function and store it
        if call not in memos:
            memos[call] = func(*args, **kwargs)
        # return the stored value
        return memos[call]

    return memoized


def b_to_mb(byts: int, decimals: int = 1) -> float:
    """Convert a count of bytes into a count of megabytes.
    
    Arguments:
        byts {int} -- The count of bytes.
    
    Keyword Arguments:
        decimals {int} -- The number of decimal points to include in the count of megabytes. (default: {1})
    
    Returns:
        float -- The count of megabytes.
    """
    return round(byts / 1000 / 1000, decimals)