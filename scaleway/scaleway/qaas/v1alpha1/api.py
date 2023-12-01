# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.utils import (
    OneOfPossibility,
    WaitForOptions,
    resolve_one_of,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    ListJobsRequestOrderBy,
    ListPlatformsRequestOrderBy,
    ListSessionsRequestOrderBy,
    PlatformTechnology,
    PlatformType,
    CreateJobRequest,
    CreateSessionRequest,
    Job,
    JobCircuit,
    ListJobsResponse,
    ListPlatformsResponse,
    ListSessionsResponse,
    Platform,
    Session,
    UpdateJobRequest,
    UpdateSessionRequest,
)
from .content import (
    JOB_TRANSIENT_STATUSES,
    SESSION_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_JobCircuit,
    unmarshal_Job,
    unmarshal_Platform,
    unmarshal_Session,
    unmarshal_ListJobsResponse,
    unmarshal_ListPlatformsResponse,
    unmarshal_ListSessionsResponse,
    marshal_CreateJobRequest,
    marshal_CreateSessionRequest,
    marshal_UpdateJobRequest,
    marshal_UpdateSessionRequest,
)


class QaasV1Alpha1API(API):
    """
    This API allows you to manage Scaleway Quantum as a Service.
    """

    def get_job(
        self,
        *,
        job_id: str,
    ) -> Job:
        """
        Get job information.
        Retrieve information about the provided **job ID**, such as status, payload, and result.
        :param job_id: Unique ID of the job you want to get.
        :return: :class:`Job <Job>`

        Usage:
        ::

            result = api.get_job(
                job_id="example",
            )
        """

        param_job_id = validate_path_param("job_id", job_id)

        res = self._request(
            "GET",
            f"/qaas/v1alpha1/jobs/{param_job_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Job(res.json())

    def wait_for_job(
        self,
        *,
        job_id: str,
        options: Optional[WaitForOptions[Job, bool]] = None,
    ) -> Job:
        """
        Get job information.
        Retrieve information about the provided **job ID**, such as status, payload, and result.
        :param job_id: Unique ID of the job you want to get.
        :return: :class:`Job <Job>`

        Usage:
        ::

            result = api.get_job(
                job_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in JOB_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_job,
            options=options,
            args={
                "job_id": job_id,
            },
        )

    def list_jobs(
        self,
        *,
        session_id: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobsRequestOrderBy] = None,
    ) -> ListJobsResponse:
        """
        List all jobs within a project or session.
        Retrieve information about all jobs within a given project or session.
        :param session_id: List jobs with this session ID.
        :param project_id: List jobs with this project ID.
        :param tags: List jobs with these tags.
        :param page: Page number.
        :param page_size: Maximum number of jobs to return per page.
        :param order_by: Sort order of the returned jobs.
        :return: :class:`ListJobsResponse <ListJobsResponse>`

        Usage:
        ::

            result = api.list_jobs()
        """

        res = self._request(
            "GET",
            "/qaas/v1alpha1/jobs",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "tags": tags,
                **resolve_one_of(
                    [
                        OneOfPossibility("project_id", project_id),
                        OneOfPossibility("session_id", session_id),
                    ]
                ),
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListJobsResponse(res.json())

    def list_jobs_all(
        self,
        *,
        session_id: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobsRequestOrderBy] = None,
    ) -> List[Job]:
        """
        List all jobs within a project or session.
        Retrieve information about all jobs within a given project or session.
        :param session_id: List jobs with this session ID.
        :param project_id: List jobs with this project ID.
        :param tags: List jobs with these tags.
        :param page: Page number.
        :param page_size: Maximum number of jobs to return per page.
        :param order_by: Sort order of the returned jobs.
        :return: :class:`List[Job] <List[Job]>`

        Usage:
        ::

            result = api.list_jobs_all()
        """

        return fetch_all_pages(
            type=ListJobsResponse,
            key="jobs",
            fetcher=self.list_jobs,
            args={
                "tags": tags,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "session_id": session_id,
                "project_id": project_id,
            },
        )

    def create_job(
        self,
        *,
        name: str,
        session_id: str,
        circuit: JobCircuit,
        tags: Optional[List[str]] = None,
        max_duration: Optional[str] = None,
    ) -> Job:
        """
        Create a job.
        Create a job to be executed inside a session.
        :param name: Name of the job.
        :param session_id: Session in which the job is executed.
        :param circuit: Quantum circuit that should be executed.
        :param tags: Tags of the job.
        :param max_duration: Maximum duration of the job.
        :return: :class:`Job <Job>`

        Usage:
        ::

            result = api.create_job(
                name="example",
                session_id="example",
                circuit=JobCircuit(),
            )
        """

        res = self._request(
            "POST",
            "/qaas/v1alpha1/jobs",
            body=marshal_CreateJobRequest(
                CreateJobRequest(
                    name=name,
                    session_id=session_id,
                    circuit=circuit,
                    tags=tags,
                    max_duration=max_duration,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Job(res.json())

    def update_job(
        self,
        *,
        job_id: str,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Job:
        """
        Update job information.
        Update job information about the provided **job ID**.
        :param job_id: Unique ID of the job.
        :param name: Name of the job.
        :param tags: Tags of the job.
        :return: :class:`Job <Job>`

        Usage:
        ::

            result = api.update_job(
                job_id="example",
            )
        """

        param_job_id = validate_path_param("job_id", job_id)

        res = self._request(
            "PATCH",
            f"/qaas/v1alpha1/jobs/{param_job_id}",
            body=marshal_UpdateJobRequest(
                UpdateJobRequest(
                    job_id=job_id,
                    name=name,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Job(res.json())

    def cancel_job(
        self,
        *,
        job_id: str,
    ) -> Job:
        """
        Cancel a job.
        Cancel the job corresponding to the provided **job ID**.
        :param job_id: Unique ID of the job.
        :return: :class:`Job <Job>`

        Usage:
        ::

            result = api.cancel_job(
                job_id="example",
            )
        """

        param_job_id = validate_path_param("job_id", job_id)

        res = self._request(
            "POST",
            f"/qaas/v1alpha1/jobs/{param_job_id}/cancel",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Job(res.json())

    def get_job_circuit(
        self,
        *,
        job_id: str,
    ) -> JobCircuit:
        """
        Get a job circuit.
        Retrieve the circuit of the provided **job ID**.
        :param job_id: Unique ID of the job.
        :return: :class:`JobCircuit <JobCircuit>`

        Usage:
        ::

            result = api.get_job_circuit(
                job_id="example",
            )
        """

        param_job_id = validate_path_param("job_id", job_id)

        res = self._request(
            "GET",
            f"/qaas/v1alpha1/jobs/{param_job_id}/circuit",
        )

        self._throw_on_error(res)
        return unmarshal_JobCircuit(res.json())

    def get_platform(
        self,
        *,
        platform_id: str,
    ) -> Platform:
        """
        Get platform information.
        Retrieve information about the provided **platform ID**, such as provider name, technology, and type.
        :param platform_id: Unique ID of the platform.
        :return: :class:`Platform <Platform>`

        Usage:
        ::

            result = api.get_platform(
                platform_id="example",
            )
        """

        param_platform_id = validate_path_param("platform_id", platform_id)

        res = self._request(
            "GET",
            f"/qaas/v1alpha1/platforms/{param_platform_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Platform(res.json())

    def list_platforms(
        self,
        *,
        provider_name: Optional[str] = None,
        name: Optional[str] = None,
        platform_type: Optional[PlatformType] = None,
        platform_technology: Optional[PlatformTechnology] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListPlatformsRequestOrderBy] = None,
    ) -> ListPlatformsResponse:
        """
        List all available platforms.
        Retrieve information about all platforms.
        :param provider_name: List platforms with this provider name.
        :param name: List platforms with this name.
        :param platform_type: List platforms with this type.
        :param platform_technology: List platforms with this technology.
        :param page: Page number.
        :param page_size: Maximum number of platforms to return per page.
        :param order_by: Sort order of the returned platforms.
        :return: :class:`ListPlatformsResponse <ListPlatformsResponse>`

        Usage:
        ::

            result = api.list_platforms()
        """

        res = self._request(
            "GET",
            "/qaas/v1alpha1/platforms",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "platform_technology": platform_technology,
                "platform_type": platform_type,
                "provider_name": provider_name,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPlatformsResponse(res.json())

    def list_platforms_all(
        self,
        *,
        provider_name: Optional[str] = None,
        name: Optional[str] = None,
        platform_type: Optional[PlatformType] = None,
        platform_technology: Optional[PlatformTechnology] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListPlatformsRequestOrderBy] = None,
    ) -> List[Platform]:
        """
        List all available platforms.
        Retrieve information about all platforms.
        :param provider_name: List platforms with this provider name.
        :param name: List platforms with this name.
        :param platform_type: List platforms with this type.
        :param platform_technology: List platforms with this technology.
        :param page: Page number.
        :param page_size: Maximum number of platforms to return per page.
        :param order_by: Sort order of the returned platforms.
        :return: :class:`List[Platform] <List[Platform]>`

        Usage:
        ::

            result = api.list_platforms_all()
        """

        return fetch_all_pages(
            type=ListPlatformsResponse,
            key="platforms",
            fetcher=self.list_platforms,
            args={
                "provider_name": provider_name,
                "name": name,
                "platform_type": platform_type,
                "platform_technology": platform_technology,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    def get_session(
        self,
        *,
        session_id: str,
    ) -> Session:
        """
        Get session infrormation.
        Retrieve information about the provided **session ID**, such as name, status, and number of executed jobs.
        :param session_id: Unique ID of the session.
        :return: :class:`Session <Session>`

        Usage:
        ::

            result = api.get_session(
                session_id="example",
            )
        """

        param_session_id = validate_path_param("session_id", session_id)

        res = self._request(
            "GET",
            f"/qaas/v1alpha1/sessions/{param_session_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Session(res.json())

    def wait_for_session(
        self,
        *,
        session_id: str,
        options: Optional[WaitForOptions[Session, bool]] = None,
    ) -> Session:
        """
        Get session infrormation.
        Retrieve information about the provided **session ID**, such as name, status, and number of executed jobs.
        :param session_id: Unique ID of the session.
        :return: :class:`Session <Session>`

        Usage:
        ::

            result = api.get_session(
                session_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in SESSION_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_session,
            options=options,
            args={
                "session_id": session_id,
            },
        )

    def list_sessions(
        self,
        *,
        platform_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSessionsRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListSessionsResponse:
        """
        List all sessions.
        Retrieve information about all sessions.
        :param platform_id: List sessions that have been created for this platform.
        :param tags: List sessions with these tags.
        :param page: Page number.
        :param page_size: Maximum number of sessions to return per page.
        :param order_by: Sort order of the returned sessions.
        :param project_id: List sessions belonging to this project ID.
        :return: :class:`ListSessionsResponse <ListSessionsResponse>`

        Usage:
        ::

            result = api.list_sessions()
        """

        res = self._request(
            "GET",
            "/qaas/v1alpha1/sessions",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "platform_id": platform_id,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSessionsResponse(res.json())

    def list_sessions_all(
        self,
        *,
        platform_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSessionsRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[Session]:
        """
        List all sessions.
        Retrieve information about all sessions.
        :param platform_id: List sessions that have been created for this platform.
        :param tags: List sessions with these tags.
        :param page: Page number.
        :param page_size: Maximum number of sessions to return per page.
        :param order_by: Sort order of the returned sessions.
        :param project_id: List sessions belonging to this project ID.
        :return: :class:`List[Session] <List[Session]>`

        Usage:
        ::

            result = api.list_sessions_all()
        """

        return fetch_all_pages(
            type=ListSessionsResponse,
            key="sessions",
            fetcher=self.list_sessions,
            args={
                "platform_id": platform_id,
                "tags": tags,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    def create_session(
        self,
        *,
        platform_id: str,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        max_idle_duration: Optional[str] = None,
        max_duration: Optional[str] = None,
        tags: Optional[List[str]] = None,
        deduplication_id: Optional[str] = None,
    ) -> Session:
        """
        Create a session.
        Create a dedicated session for the specified platform.
        :param platform_id: ID of the Platform for which the session was created.
        :param project_id: ID of the Project in which the session was created.
        :param name: Name of the session.
        :param max_idle_duration: Maximum idle duration before the session ends.
        :param max_duration: Maximum duration before the session ends.
        :param tags: Tags of the session.
        :param deduplication_id: Deduplication ID of the session.
        :return: :class:`Session <Session>`

        Usage:
        ::

            result = api.create_session(
                platform_id="example",
            )
        """

        res = self._request(
            "POST",
            "/qaas/v1alpha1/sessions",
            body=marshal_CreateSessionRequest(
                CreateSessionRequest(
                    platform_id=platform_id,
                    project_id=project_id,
                    name=name,
                    max_idle_duration=max_idle_duration,
                    max_duration=max_duration,
                    tags=tags,
                    deduplication_id=deduplication_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Session(res.json())

    def update_session(
        self,
        *,
        session_id: str,
        name: Optional[str] = None,
        max_idle_duration: Optional[str] = None,
        max_duration: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Session:
        """
        Update session information.
        Update session information of the provided **session ID**.
        :param session_id: Unique ID of the session.
        :param name: Name of the session.
        :param max_idle_duration: Maximum idle duration before the session ends.
        :param max_duration: Maximum duration before the session ends.
        :param tags: Tags of the session.
        :return: :class:`Session <Session>`

        Usage:
        ::

            result = api.update_session(
                session_id="example",
            )
        """

        param_session_id = validate_path_param("session_id", session_id)

        res = self._request(
            "PATCH",
            f"/qaas/v1alpha1/sessions/{param_session_id}",
            body=marshal_UpdateSessionRequest(
                UpdateSessionRequest(
                    session_id=session_id,
                    name=name,
                    max_idle_duration=max_idle_duration,
                    max_duration=max_duration,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Session(res.json())

    def delete_session(
        self,
        *,
        session_id: str,
    ) -> None:
        """
        Delete an existing session.
        Delete a session by its unique ID and cancel all its attached jobs.
        :param session_id: Unique ID of the session.

        Usage:
        ::

            result = api.delete_session(
                session_id="example",
            )
        """

        param_session_id = validate_path_param("session_id", session_id)

        res = self._request(
            "DELETE",
            f"/qaas/v1alpha1/sessions/{param_session_id}",
        )

        self._throw_on_error(res)
