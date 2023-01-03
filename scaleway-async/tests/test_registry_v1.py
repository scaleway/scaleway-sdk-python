import unittest
from contextlib import AsyncExitStack

import utils

from scaleway_async import Client
from scaleway_async.registry.v1 import NamespaceStatus, RegistryV1API
from scaleway_core.utils.waiter import WaitForOptions


class TestRegistryV1(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        client = Client.from_config_file_and_env()
        self.api = RegistryV1API(client)

    async def test_create_namespace(self) -> None:
        name = utils.random_name()

        async with AsyncExitStack() as stack:
            namespace = await self.api.create_namespace(
                name=name,
                description="test",
                is_public=False,
            )
            stack.push_async_callback(
                self.api.delete_namespace, namespace_id=namespace.id
            )

            await self.api.wait_for_namespace(
                namespace_id=namespace.id,
                options=WaitForOptions(
                    stop=lambda x: x.status == NamespaceStatus.READY
                ),
            )

            self.assertEqual(namespace.name, name)

    async def test_list_namespaces(self) -> None:
        namespaces = await self.api.list_namespaces()
        self.assertTrue(type(namespaces.namespaces) is list)

    async def test_list_namespaces_all(self) -> None:
        namespaces = await self.api.list_namespaces_all()
        self.assertTrue(type(namespaces) is list)

    async def test_get_namespace(self) -> None:
        name = utils.random_name()

        async with AsyncExitStack() as stack:
            namespace = await self.api.create_namespace(
                name=name,
                description="test",
                is_public=False,
            )
            stack.push_async_callback(
                self.api.delete_namespace, namespace_id=namespace.id
            )

            await self.api.wait_for_namespace(
                namespace_id=namespace.id,
                options=WaitForOptions(
                    stop=lambda x: x.status == NamespaceStatus.READY
                ),
            )

            namespace2 = await self.api.get_namespace(namespace_id=namespace.id)
            self.assertEqual(namespace.id, namespace2.id)

    async def test_update_namespace(self) -> None:
        name = utils.random_name()

        async with AsyncExitStack() as stack:
            namespace = await self.api.create_namespace(
                name=name,
                description="test",
                is_public=False,
            )
            stack.push_async_callback(
                self.api.delete_namespace, namespace_id=namespace.id
            )

            await self.api.wait_for_namespace(
                namespace_id=namespace.id,
                options=WaitForOptions(
                    stop=lambda x: x.status == NamespaceStatus.READY
                ),
            )

            namespace2 = await self.api.update_namespace(
                namespace_id=namespace.id,
                description="test2",
                is_public=True,
            )

            self.assertEqual(namespace.id, namespace2.id)
            self.assertEqual(namespace2.description, "test2")
            self.assertEqual(namespace2.is_public, True)

    async def test_delete_namespace(self) -> None:
        name = utils.random_name()

        async with AsyncExitStack() as stack:
            namespace = await self.api.create_namespace(
                name=name,
                description="test",
                is_public=False,
            )
            stack.push_async_callback(
                self.api.delete_namespace, namespace_id=namespace.id
            )

            await self.api.wait_for_namespace(
                namespace_id=namespace.id,
                options=WaitForOptions(
                    stop=lambda x: x.status == NamespaceStatus.READY
                ),
            )

        try:
            await self.api.wait_for_namespace(
                namespace_id=namespace.id,
                options=WaitForOptions(
                    stop=lambda x: x.status == NamespaceStatus.DELETING
                ),
            )
        except Exception as e:
            self.assertNotIsInstance(e, TimeoutError)
            pass
