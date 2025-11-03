# MongoDB tests (VCR)

This suite uses VCR cassettes to replay HTTP calls in CI.

How to record locally:

1. Ensure you have valid Scaleway credentials exported (access key, secret key, default region).
2. Pick a MongoDB instance to target for snapshot creation.
3. Temporarily replace the fixed `instance_id` in `test_custom_api.py` with your instance id or set breakpoints to inject it.
4. Run the specific test once to record the cassette:

   ```bash
   pytest -k test_create_snapshot_with_naive_expires_at_vcr
   ```

5. Commit the generated cassette file:
   - Path: `scaleway/scaleway/mongodb/v1/tests/cassettes/test_create_snapshot_with_naive_expires_at_vcr.cassette.yaml`

Notes:
- The test will skip in CI if the cassette file is missing.
- After recording, restore the fixed `instance_id` value used by the test to keep requests stable across replays.
