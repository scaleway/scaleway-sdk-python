import unittest
from scaleway.domain.v2beta1.marshalling import marshal_RecordChange
from scaleway_core.profile.profile import ProfileDefaults
from scaleway.domain.v2beta1.types import RecordChangeSet, RecordChange, Record, RecordType

class TestRecordChangeMarshalling(unittest.TestCase):
    def test_marshalRecord(self):
        recordToUpdate: Record = Record(data="1.1.1.1", name="test", priority=1, ttl=3600, type_=RecordType.A, id="1536b046-23c8-4a67-9266-8828d7cd2785",
                                        comment=None, geo_ip_config=None, http_service_config=None, view_config=None, weighted_config=None)
        changes: RecordChange = RecordChange(
            set_ = [
                RecordChangeSet(records=[recordToUpdate], id=recordToUpdate.id, id_fields=None)
            ],
            delete = None,
            clear = None,
            add = None
        )
        defaults = ProfileDefaults()
        actual = marshal_RecordChange(changes, defaults)

        expected = {'set': {'id': '1536b046-23c8-4a67-9266-8828d7cd2785',
                    'records': [{'data': '1.1.1.1',
                    'id': '1536b046-23c8-4a67-9266-8828d7cd2785',
                    'name': 'test',
                    'priority': 1,
                    'ttl': 3600,
                    'type': 'a'}]}}
        self.assertEqual(actual, expected)