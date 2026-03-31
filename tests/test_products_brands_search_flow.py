"""
API tests for Automation Exercise APIs 1 to 6.
Covers products list, brands list, search product, and negative method checks.
"""

from __future__ import annotations

import logging
import requests

logger = logging.getLogger(__name__)

BASE_URL = "https://automationexercise.com"


def test_api_1_get_all_products_list():
    """
    API 1: GET all products list.
    """
    response = requests.get(f"{BASE_URL}/api/productsList", timeout=30)

    logger.info("API 1 RESPONSE: %s %s", response.status_code, response.text)
    print(f"API 1 RESPONSE: {response.status_code} {response.text}")

    assert response.status_code == 200, "API 1 did not return HTTP 200"
    assert "products" in response.text.lower(), "Products data not found in API 1 response"


def test_api_2_post_to_all_products_list():
    """
    API 2: POST to products list should fail with method not supported.
    """
    response = requests.post(f"{BASE_URL}/api/productsList", timeout=30)

    logger.info("API 2 RESPONSE: %s %s", response.status_code, response.text)
    print(f"API 2 RESPONSE: {response.status_code} {response.text}")

    assert response.status_code == 200, "Public demo API returned unexpected HTTP status"
    assert '"responseCode": 405' in response.text or '"responseCode":405' in response.text, \
        "API 2 business response code is not 405"
    assert "method is not supported" in response.text.lower(), \
        "API 2 expected error message not found"


def test_api_3_get_all_brands_list():
    """
    API 3: GET all brands list.
    """
    response = requests.get(f"{BASE_URL}/api/brandsList", timeout=30)

    logger.info("API 3 RESPONSE: %s %s", response.status_code, response.text)
    print(f"API 3 RESPONSE: {response.status_code} {response.text}")

    assert response.status_code == 200, "API 3 did not return HTTP 200"
    assert "brands" in response.text.lower(), "Brands data not found in API 3 response"


def test_api_4_put_to_all_brands_list():
    """
    API 4: PUT to brands list should fail with method not supported.
    """
    response = requests.put(f"{BASE_URL}/api/brandsList", timeout=30)

    logger.info("API 4 RESPONSE: %s %s", response.status_code, response.text)
    print(f"API 4 RESPONSE: {response.status_code} {response.text}")

    assert response.status_code == 200, "Public demo API returned unexpected HTTP status"
    assert '"responseCode": 405' in response.text or '"responseCode":405' in response.text, \
        "API 4 business response code is not 405"
    assert "method is not supported" in response.text.lower(), \
        "API 4 expected error message not found"


def test_api_5_post_to_search_product():
    """
    API 5: POST to search product with valid parameter.
    """
    payload = {
        "search_product": "top"
    }

    response = requests.post(f"{BASE_URL}/api/searchProduct", data=payload, timeout=30)

    logger.info("API 5 RESPONSE: %s %s", response.status_code, response.text)
    print(f"API 5 RESPONSE: {response.status_code} {response.text}")

    assert response.status_code == 200, "API 5 did not return HTTP 200"
    assert "products" in response.text.lower(), "Searched products not found in API 5 response"


def test_api_6_post_to_search_product_without_parameter():
    """
    API 6: POST to search product without search_product parameter.
    """
    response = requests.post(f"{BASE_URL}/api/searchProduct", data={}, timeout=30)

    logger.info("API 6 RESPONSE: %s %s", response.status_code, response.text)
    print(f"API 6 RESPONSE: {response.status_code} {response.text}")

    assert response.status_code == 200, "Public demo API returned unexpected HTTP status"
    assert '"responseCode": 400' in response.text or '"responseCode":400' in response.text, \
        "API 6 business response code is not 400"
    assert "search_product parameter is missing" in response.text.lower(), \
        "API 6 expected error message not found"