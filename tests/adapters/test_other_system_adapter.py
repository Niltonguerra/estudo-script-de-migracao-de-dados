import pytest

from src.modules.data_migration.adapters.Other_system_adapter import OtherSystemAdapter


@pytest.mark.asyncio
async def test_send_products_returns_success_status():
    adapter = OtherSystemAdapter()
    products = ["produto1", "produto2"]

    result = await adapter.send_products(products)

    assert result["status"] == "success"


@pytest.mark.asyncio
async def test_send_products_returns_correct_total():
    adapter = OtherSystemAdapter()
    products = ["produto1", "produto2", "produto3"]

    result = await adapter.send_products(products)

    assert result["total"] == 3


@pytest.mark.asyncio
async def test_send_products_returns_success_message():
    adapter = OtherSystemAdapter()
    products = ["produto1"]

    result = await adapter.send_products(products)

    assert result["message"] == "products received successfully"


@pytest.mark.asyncio
async def test_send_products_with_empty_list():
    adapter = OtherSystemAdapter()

    result = await adapter.send_products([])

    assert result["total"] == 0
    assert result["status"] == "success"