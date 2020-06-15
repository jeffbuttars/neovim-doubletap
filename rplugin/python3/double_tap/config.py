from dataclasses import dataclass, field
"""
Syntax strings
These are used to match Neovim's syntax detection to text we're interested in.
"""
SYN_STRINGS = (
    'string', 'quotes', 'heredoc', 'doctestvalue',
    'doctest', 'doctest2', 'bytesescape',
)

# future configurable,
# configurable per map will be available
DEFAULT_KEY_TIMEOUT = 0.750
INSERT_IN_STRING = 0
DEFAULT_SEARCH_TIMEOUT = 500

"""
Default insert map for all file types
"""
INSERT_MAP = {
    "(": {'insert': '()', 'r': ')'},
    "[": {'insert': '[]', 'r': ']'},
    "{": {'insert': '{}', 'r': '}'},
    "<": {'insert': '<>', 'r': '>'},
    "'": {'insert': "''", 'string': True},
    '"': {'insert': '""', 'string': True},
    "`": {'insert': "``", 'string': True},
}

"""
Default finishers map for all file types
"""
FINISHERS_MAP = {
    ';': ';',
    ',': ',',
}

"""
Default jump map values
"""
JUMP_MAP = {
    ")": {'r': ')'},
    "]": {'r': ']'},
    "}": {'r': '}'},
    ">": {'r': '>'},
    #  "'": {'string': True},
    #  '"': {'string': True},
    #  "`": {'string': True},
}


@dataclass
class DTConfig:
    inserts: dict = field(default_factory=INSERT_MAP.copy)
    finishers: dict = field(default_factory=FINISHERS_MAP.copy)
    jumps: dict = field(default_factory=JUMP_MAP.copy)
    timeout: float = field(default=DEFAULT_KEY_TIMEOUT)
    search_timeout: int = field(default=DEFAULT_SEARCH_TIMEOUT)
    #  def __post_init__(self):
    #      # Build defaults
    #      self._insert_map = INSERT_MAP.copy()
    #      self._jump_map = JUMP_MAP.copy()
    #      self._finishers_map = FINISHERS_MAP.copy()

    #      self._timeout = DEFAULT_KEY_TIMEOUT
    #      self._insert_in_string = bool(INSERT_IN_STRING)
    #      self._syntax_types = SYN_STRINGS

    #  @property
    #  def syntax_types(self):
    #      return self._syntax_types

    #  @property
    #  def timeout(self):
    #      return self._timeout

    #  @property
    #  def insert_in_string(self):
    #      return self._insert_in_string

    #  @property
    #  def insert_map(self):
    #      return self._insert_map

    #  @property
    #  def jump_map(self):
    #      return self._jump_map

    #  @property
    #  def finishers_map(self):
    #      return self._finishers_map