import unittest
from contextlib import ExitStack
from typing import Optional

import utils

from scaleway import Client
from scaleway_core.utils.waiter import WaitForOptions
from scaleway.registry.v1 import Namespace, NamespaceStatus, RegistryV1API


class TestRegistryV1(unittest.TestCase):
    def setUp(self) -> None:
        client = Client.from_config_file_and_env()
        self.api = RegistryV1API(client)

    def test_create_namespace(self) -> None:
        name = utils.random_name()

        with ExitStack() as stack:
            namespace = self.api.create_namespace(
                name=name,
                description="test",
                is_public=False,
            )
            stack.callback(self.api.delete_namespace, namespace_id=namespace.id)

            self.api.wait_for_namespace(
                namespace_id=namespace.id,
                options=WaitForOptions(
                    stop=lambda x: x.status == NamespaceStatus.READY
                ),
            )

            self.assertEqual(namespace.name, name)

    def test_list_namespaces(self) -> None:
        namespaces = self.api.list_namespaces()
        self.assertTrue(type(namespaces.namespaces) is list)

    def test_list_namespaces_all(self) -> None:
        namespaces = self.api.list_namespaces_all()
        self.assertTrue(type(namespaces) is list)

    def test_get_namespace(self) -> None:
        name = utils.random_name()

        with ExitStack() as stack:
            namespace = self.api.create_namespace(
                name=name,
                description="test",
                is_public=False,
            )
            stack.callback(self.api.delete_namespace, namespace_id=namespace.id)

            self.api.wait_for_namespace(
                namespace_id=namespace.id,
                options=WaitForOptions(
                    stop=lambda x: x.status == NamespaceStatus.READY
                ),
            )

            namespace2 = self.api.get_namespace(namespace_id=namespace.id)
            self.assertEqual(namespace.id, namespace2.id)

    def test_update_namespace(self) -> None:
        name = utils.random_name()

        with ExitStack() as stack:
            namespace = self.api.create_namespace(
                name=name,
                description="test",
                is_public=False,
            )
            stack.callback(self.api.delete_namespace, namespace_id=namespace.id)

            self.api.wait_for_namespace(
                namespace_id=namespace.id,
                options=WaitForOptions(
                    stop=lambda x: x.status == NamespaceStatus.READY
                ),
            )

            namespace2 = self.api.update_namespace(
                namespace_id=namespace.id,
                description="test2",
                is_public=True,
            )

            self.assertEqual(namespace.id, namespace2.id)
            self.assertEqual(namespace2.description, "test2")
            self.assertEqual(namespace2.is_public, True)

    def test_delete_namespace(self) -> None:
        name = utils.random_name()

        namespace: Optional[Namespace] = None

        with ExitStack() as stack:
            namespace = self.api.create_namespace(
                name=name,
                description="test",
                is_public=False,
            )
            stack.callback(self.api.delete_namespace, namespace_id=namespace.id)

            self.api.wait_for_namespace(
                namespace_id=namespace.id,
                options=WaitForOptions(
                    stop=lambda x: x.status == NamespaceStatus.READY
                ),
            )

        try:
            self.api.wait_for_namespace(
                namespace_id=namespace.id,
                options=WaitForOptions(
                    stop=lambda x: x.status == NamespaceStatus.DELETING
                ),
            )
        except Exception as e:
            self.assertNotIsInstance(e, TimeoutError)
            pass
