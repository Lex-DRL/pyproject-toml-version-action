#!/usr/bin/env python
# encoding: utf-8
"""
"""
from dataclasses import dataclass as _dataclass

from pyproject_toml_version import *

from _shared_utils import _cleanup_as_single_line, _EnvInputsABC, GithubOutput


@_dataclass
class EnvInputs(_EnvInputsABC):
	"""Script 'arguments' passed as env-vars (for security reasons)."""
	toml_file: str

	def __post_init__(self):
		self.toml_file = _cleanup_as_single_line(self.toml_file)


def version_main(github_output_env: str = 'GITHUB_OUTPUT', ) -> None:
	env_args = EnvInputs.from_env()
	env_args.print()

	version = pyproject_version(env_args.toml_file)

	GithubOutput(github_output_env=github_output_env).set(version=version)


if __name__ == '__main__':
	version_main()
