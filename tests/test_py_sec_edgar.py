#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `py_sec_edgar` package."""

import pytest
import unittest

from click.testing import CliRunner

import py_sec_edgar
import py_sec_edgar.__main__

import pytest



@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

def test_content(response):
    """Sample pytest tests function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    feed_item = {
            'CIK': 104169,
            'Company Name': 'Walmart Inc.',
            'Date Filed': '2019-03-28',
            'Filename': 'edgar/data/104169/0000104169-19-000016.txt',
            'Form Type': '10-K',
            'cik_directory': 'sec_gov\\Archives\\edgar\\data\\104169\\',
            'extracted_filing_directory': 'sec_gov\\Archives\\edgar\\data\\104169\\000010416919000016',
            'filing_filepath': 'sec_gov\\Archives\\edgar\\data\\104169\\0000104169-19-000016.txt',
            'filing_folder': '000010416919000016',
            'filing_url': 'https://www.sec.gov/Archives/edgar/data/104169/0000104169-19-000016.txt',
            'filing_zip_filepath': 'sec_gov\\Archives\\edgar\\data\\104169\\0000104169-19-000016.zip',
            'published': '2019-03-28',
            'url': 'https://www.sec.gov/Archives/edgar/data/104169/0000104169-19-000016.txt'
    }

def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()

    from py_sec_edgar.settings import CONFIG

    result = runner.invoke(py_sec_edgar.__main__.main, args=CONFIG)
    assert result.exit_code == 0
    assert 'py_sec_edgar.main' in result.output
    help_result = runner.invoke(py_sec_edgar.__main__.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

class TestPy_sec_edgar(unittest.TestCase):
    """Tests for `refinitiv_permid_data_exploration` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(py_sec_edgar.__main__.main)
        assert result.exit_code == 0
        assert 'refinitiv_permid_data_exploration.cli.main' in result.output
        help_result = runner.invoke(py_sec_edgar.__main__.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
