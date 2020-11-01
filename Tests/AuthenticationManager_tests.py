"""
Testing script for AuthenticationManager class
"""

from Application.AuthenticationManager import AuthenticationManager


def test_auth_manager():
    assert_status = AuthenticationManager().authenticate("arnab", "test")
    assert assert_status == True
