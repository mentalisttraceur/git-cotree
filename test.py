import subprocess

from hypothesis import given
from hypothesis.strategies import composite, sampled_from
import pytest


def _git_cotree(*arguments):
    result = subprocess.run(
        ['./git-cotree', *arguments],
        capture_output=True,
        check=True,
    )
    assert result.stderr == b''
    return result.stdout.removesuffix(b'\n')


help_options = sampled_from(('--usage', '--help', '-h'))
init_options = sampled_from(('--initialize', '--init', '-i'))
delete_options = sampled_from(('--delete', '-d'))
force_options = sampled_from(('--force', '-f'))
force_delete_options = sampled_from(('-D', '-fd', '-df'))
base_options = sampled_from(('--base', '-b'))
show_root_options = sampled_from(('--show-root',))
collapse_options = sampled_from(('--collapse', '-c'))


def _git_cotree_init(init_option):
    output = _git_cotree(init_option)
    assert not output


@given(init_options)
def test_empty_directory(tmp_path, init_option):
    _git_cotree_init(init_option)


def test_empty_repo(tmp_path):
    result = subprocess.run(['git', 'init'])
    
