#!/usr/bin/env python
# encoding: utf-8
"""
"""
import typing as _t
from typing import Any as _A, Optional as _O, Union as _U

from dataclasses import dataclass as _dataclass

import tomli

from _shared_utils import _cleanup_as_single_line, _EnvInputsABC, GithubOutput


@_dataclass
class EnvInputs(_EnvInputsABC):
	"""Script 'arguments' passed as env-vars (for security reasons)."""
	toml_file: str

	def __post_init__(self):
		self.toml_file = _cleanup_as_single_line(self.toml_file)


def _validate_value(version, toml_path: str) -> str:
	if not version:
		raise ValueError(f"No version in {toml_path!r}: {version!r}")
	if not isinstance(version, str):
		raise TypeError(f"Version isn't a string: {version!r}")
	return version


def read_version(toml_path: str = 'pyproject.toml'):
	with open(toml_path, 'rb') as f:  # tomli.load needs a binary file
		toml_data = tomli.load(f)

	project: _O[_t.Dict[str, _A]] = toml_data.get("project", None)
	if not project:
		raise ValueError(f"Missing/empty 'project' section in: {toml_path!r}")
	if not isinstance(project, dict):
		raise TypeError(f"Internal error - 'project' section isn't a dict: {project!r}")

	dynamic = project.get("dynamic", [])
	if isinstance(dynamic, str):
		dynamic = [dynamic]
	if not isinstance(dynamic, (list, tuple, set, _t.Iterable)):
		try:
			dynamic = iter(dynamic)
		except Exception:
			if dynamic is None:
				dynamic = []
			else:
				raise TypeError(f"Invalid type for 'project.dynamic' field: {dynamic!r}")
	dynamic_set: _t.Set[str] = set(dynamic)

	is_static = 'version' in project
	is_dynamic = 'version' in dynamic_set
	if is_static == is_dynamic:
		what = 'version is both static and dynamic' if is_static else 'neither static nor dynamic version is present'
		raise ValueError(f"Invalid project file - {what}: {toml_path!r}")

	if is_static:
		# Simple case: static version
		return _validate_value(project["version"], toml_path)

	assert is_dynamic and not is_static
	# TODO: using `build` is fragile, need to reimplement for each popular build-backend
	raise NotImplementedError("Dynamic version detection isn't implemented yet")


def version_main(github_output_env: str = 'GITHUB_OUTPUT', ) -> None:
	env_args = EnvInputs.from_env()
	env_args.print()

	version = read_version(toml_path=env_args.toml_file)

	GithubOutput(github_output_env=github_output_env).set(version=version)


if __name__ == '__main__':
	version_main()
