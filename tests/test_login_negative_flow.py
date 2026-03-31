"""
API tests for Automation Exercise APIs 8, 9, and 10.
Covers negative login scenarios.
"""

from __future__ import annotations

import logging
import requests

logger = logging.getLogger(__name__)

BASE_URL = "https://automationexercise.com"


def test_api_8_verify_login_without_email_parameter():
    """
    API 8: POST to verify login without email parameter.
    """
    payload = {
        "password": "Test@123"
    }

    response = requests.post(f"{BASE_URL}/api/verifyLogin", data=payload, timeout=30)

    logger.info("API 8 RESPONSE: %s %s", response.status_code, response.text)
    print(f"API 8 RESPONSE: {response.status_code} {response.text}")

    assert response.status_code == 200, "Public demo API returned unexpected HTTP status"
    assert '"responseCode": 400' in response.text or '"responseCode":400' in response.text, \
        "API 8 business response code is not 400"
    assert "email or password parameter is missing" in response.text.lower(), \
        "API 8 expected error message not found"


def test_api_9_delete_to_verify_login():
    """
    API 9: DELETE to verify login.
    """
    response = requests.delete(f"{BASE_URL}/api/verifyLogin", timeout=30)

    logger.info("API 9 RESPONSE: %s %s", response.status_code, response.text)
    print(f"API 9 RESPONSE: {response.status_code} {response.text}")

    assert response.status_code == 200, "Public demo API returned unexpected HTTP status"
    assert '"responseCode": 405' in response.text or '"responseCode":405' in response.text, \
        "API 9 business response code is not 405"
    assert "method is not supported" in response.text.lower(), \
        "API 9 expected error message not found"


def test_api_10_verify_login_with_invalid_details():
    """
    API 10: POST to verify login with invalid details.
    """
    payload = {
        "email": "invalid_test_user@test.com",
        "password": "Invalid@123"
    }

    response = requests.post(f"{BASE_URL}/api/verifyLogin", data=payload, timeout=30)

    logger.info("API 10 RESPONSE: %s %s", response.status_code, response.text)
    print(f"API 10 RESPONSE: {response.status_code} {response.text}")

    assert response.status_code == 200, "Public demo API returned unexpected HTTP status"
    assert '"responseCode": 404' in response.text or '"responseCode":404' in response.text, \
        "API 10 business response code is not 404"
    assert "user not found" in response.text.lower(), \
        "API 10 expected error message not found"