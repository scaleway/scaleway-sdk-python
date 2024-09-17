# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.utils import (
    OneOfPossibility,
    WaitForOptions,
    resolve_one_of,
    validate_path_param,
    fetch_all_pages_async,
    wait_for_resource_async,
)
from .types import (
    ApplicationType,
    ListApplicationsRequestOrderBy,
    ListJobResultsRequestOrderBy,
    ListJobsRequestOrderBy,
    ListPlatformsRequestOrderBy,
    ListProcessResultsRequestOrderBy,
    ListProcessesRequestOrderBy,
    ListSessionACLsRequestOrderBy,
    ListSessionsRequestOrderBy,
    PlatformTechnology,
    PlatformType,
    SessionAccess,
    Application,
    CreateJobRequest,
    CreateProcessRequest,
    CreateSessionRequest,
    Job,
    JobCircuit,
    JobResult,
    ListApplicationsResponse,
    ListJobResultsResponse,
    ListJobsResponse,
    ListPlatformsResponse,
    ListProcessResultsResponse,
    ListProcessesResponse,
    ListSessionACLsResponse,
    ListSessionsResponse,
    Platform,
    Process,
    ProcessResult,
    Session,
    UpdateJobRequest,
    UpdateProcessRequest,
    UpdateSessionRequest,
)
from .content import (
    JOB_TRANSIENT_STATUSES,
    PROCESS_TRANSIENT_STATUSES,
    SESSION_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_JobCircuit,
    unmarshal_Application,
    unmarshal_Job,
    unmarshal_Platform,
    unmarshal_Process,
    unmarshal_Session,
    unmarshal_ListApplicationsResponse,
    unmarshal_ListJobResultsResponse,
    unmarshal_ListJobsResponse,
    unmarshal_ListPlatformsResponse,
    unmarshal_ListProcessResultsResponse,
    unmarshal_ListProcessesResponse,
    unmarshal_ListSessionACLsResponse,
    unmarshal_ListSessionsResponse,
    marshal_CreateJobRequest,
    marshal_CreateProcessRequest,
    marshal_CreateSessionRequest,
    marshal_UpdateJobRequest,
    marshal_UpdateProcessRequest,
    marshal_UpdateSessionRequest,
)


class QaasV1Alpha1API(API):
    """
    This API allows you to manage Scaleway Quantum as a Service.
    """

    async def get_job(
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

            result = await api.get_job(
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

    async def wait_for_job(
        self,
        *,
        job_id: str,
        options: Optional[WaitForOptions[Job, Union[bool, Awaitable[bool]]]] = None,
    ) -> Job:
        """
        Get job information.
        Retrieve information about the provided **job ID**, such as status, payload, and result.
        :param job_id: Unique ID of the job you want to get.
        :return: :class:`Job <Job>`

        Usage:
        ::

            result = await api.get_job(
                job_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in JOB_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_job,
            options=options,
            args={
                "job_id": job_id,
            },
        )

    async def list_jobs(
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
        One-Of ('resource_id'): at most one of 'session_id', 'project_id' could be set.
        :param project_id: List jobs with this project ID.
        One-Of ('resource_id'): at most one of 'session_id', 'project_id' could be set.
        :param tags: List jobs with these tags.
        :param page: Page number.
        :param page_size: Maximum number of jobs to return per page.
        :param order_by: Sort order of the returned jobs.
        :return: :class:`ListJobsResponse <ListJobsResponse>`

        Usage:
        ::

            result = await api.list_jobs()
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

    async def list_jobs_all(
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
        One-Of ('resource_id'): at most one of 'session_id', 'project_id' could be set.
        :param project_id: List jobs with this project ID.
        One-Of ('resource_id'): at most one of 'session_id', 'project_id' could be set.
        :param tags: List jobs with these tags.
        :param page: Page number.
        :param page_size: Maximum number of jobs to return per page.
        :param order_by: Sort order of the returned jobs.
        :return: :class:`List[Job] <List[Job]>`

        Usage:
        ::

            result = await api.list_jobs_all()
        """

        return await fetch_all_pages_async(
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

    async def list_job_results(
        self,
        *,
        job_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobResultsRequestOrderBy] = None,
    ) -> ListJobResultsResponse:
        """
        List all results of a job.
        Retrieve all intermediate and final results of a job.
        :param job_id: ID of the job.
        :param page: Page number.
        :param page_size: Maximum number of results to return per page.
        :param order_by: Sort order of the returned results.
        :return: :class:`ListJobResultsResponse <ListJobResultsResponse>`

        Usage:
        ::

            result = await api.list_job_results(
                job_id="example",
            )
        """

        param_job_id = validate_path_param("job_id", job_id)

        res = self._request(
            "GET",
            f"/qaas/v1alpha1/jobs/{param_job_id}/results",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListJobResultsResponse(res.json())

    async def list_job_results_all(
        self,
        *,
        job_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobResultsRequestOrderBy] = None,
    ) -> List[JobResult]:
        """
        List all results of a job.
        Retrieve all intermediate and final results of a job.
        :param job_id: ID of the job.
        :param page: Page number.
        :param page_size: Maximum number of results to return per page.
        :param order_by: Sort order of the returned results.
        :return: :class:`List[JobResult] <List[JobResult]>`

        Usage:
        ::

            result = await api.list_job_results_all(
                job_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListJobResultsResponse,
            key="job_results",
            fetcher=self.list_job_results,
            args={
                "job_id": job_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def create_job(
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

            result = await api.create_job(
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

    async def update_job(
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

            result = await api.update_job(
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

    async def cancel_job(
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

            result = await api.cancel_job(
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

    async def delete_job(
        self,
        *,
        job_id: str,
    ) -> None:
        """
        Delete a job.
        Delete the job corresponding to the provided **job ID**.
        :param job_id: Unique ID of the job.

        Usage:
        ::

            result = await api.delete_job(
                job_id="example",
            )
        """

        param_job_id = validate_path_param("job_id", job_id)

        res = self._request(
            "DELETE",
            f"/qaas/v1alpha1/jobs/{param_job_id}",
        )

        self._throw_on_error(res)

    async def get_job_circuit(
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

            result = await api.get_job_circuit(
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

    async def get_platform(
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

            result = await api.get_platform(
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

    async def list_platforms(
        self,
        *,
        provider_name: Optional[str] = None,
        backend_name: Optional[str] = None,
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
        :param backend_name: List platforms with this backend name.
        :param name: List platforms with this name.
        :param platform_type: List platforms with this type.
        :param platform_technology: List platforms with this technology.
        :param page: Page number.
        :param page_size: Maximum number of platforms to return per page.
        :param order_by: Sort order of the returned platforms.
        :return: :class:`ListPlatformsResponse <ListPlatformsResponse>`

        Usage:
        ::

            result = await api.list_platforms()
        """

        res = self._request(
            "GET",
            "/qaas/v1alpha1/platforms",
            params={
                "backend_name": backend_name,
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

    async def list_platforms_all(
        self,
        *,
        provider_name: Optional[str] = None,
        backend_name: Optional[str] = None,
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
        :param backend_name: List platforms with this backend name.
        :param name: List platforms with this name.
        :param platform_type: List platforms with this type.
        :param platform_technology: List platforms with this technology.
        :param page: Page number.
        :param page_size: Maximum number of platforms to return per page.
        :param order_by: Sort order of the returned platforms.
        :return: :class:`List[Platform] <List[Platform]>`

        Usage:
        ::

            result = await api.list_platforms_all()
        """

        return await fetch_all_pages_async(
            type=ListPlatformsResponse,
            key="platforms",
            fetcher=self.list_platforms,
            args={
                "provider_name": provider_name,
                "backend_name": backend_name,
                "name": name,
                "platform_type": platform_type,
                "platform_technology": platform_technology,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def get_session(
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

            result = await api.get_session(
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

    async def wait_for_session(
        self,
        *,
        session_id: str,
        options: Optional[WaitForOptions[Session, Union[bool, Awaitable[bool]]]] = None,
    ) -> Session:
        """
        Get session infrormation.
        Retrieve information about the provided **session ID**, such as name, status, and number of executed jobs.
        :param session_id: Unique ID of the session.
        :return: :class:`Session <Session>`

        Usage:
        ::

            result = await api.get_session(
                session_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in SESSION_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_session,
            options=options,
            args={
                "session_id": session_id,
            },
        )

    async def list_sessions(
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

            result = await api.list_sessions()
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

    async def list_sessions_all(
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

            result = await api.list_sessions_all()
        """

        return await fetch_all_pages_async(
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

    async def create_session(
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

            result = await api.create_session(
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

    async def update_session(
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
        :param max_duration: Maximum time before the session ends.
        :param tags: Tags of the session.
        :return: :class:`Session <Session>`

        Usage:
        ::

            result = await api.update_session(
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

    async def terminate_session(
        self,
        *,
        session_id: str,
    ) -> Session:
        """
        Terminate an existing session.
        Terminate a session by its unique ID and cancel all its attached jobs.
        :param session_id: Unique ID of the session.
        :return: :class:`Session <Session>`

        Usage:
        ::

            result = await api.terminate_session(
                session_id="example",
            )
        """

        param_session_id = validate_path_param("session_id", session_id)

        res = self._request(
            "POST",
            f"/qaas/v1alpha1/sessions/{param_session_id}/terminate",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Session(res.json())

    async def delete_session(
        self,
        *,
        session_id: str,
    ) -> None:
        """
        Delete an existing session.
        Delete a session by its unique ID and delete all its attached jobs.
        :param session_id: Unique ID of the session.

        Usage:
        ::

            result = await api.delete_session(
                session_id="example",
            )
        """

        param_session_id = validate_path_param("session_id", session_id)

        res = self._request(
            "DELETE",
            f"/qaas/v1alpha1/sessions/{param_session_id}",
        )

        self._throw_on_error(res)

    async def list_session_ac_ls(
        self,
        *,
        session_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSessionACLsRequestOrderBy] = None,
    ) -> ListSessionACLsResponse:
        """
        :param session_id:
        :param page:
        :param page_size:
        :param order_by:
        :return: :class:`ListSessionACLsResponse <ListSessionACLsResponse>`

        Usage:
        ::

            result = await api.list_session_ac_ls(
                session_id="example",
            )
        """

        param_session_id = validate_path_param("session_id", session_id)

        res = self._request(
            "GET",
            f"/qaas/v1alpha1/sessions/{param_session_id}/acls",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSessionACLsResponse(res.json())

    async def list_session_ac_ls_all(
        self,
        *,
        session_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSessionACLsRequestOrderBy] = None,
    ) -> List[SessionAccess]:
        """
        :param session_id:
        :param page:
        :param page_size:
        :param order_by:
        :return: :class:`List[SessionAccess] <List[SessionAccess]>`

        Usage:
        ::

            result = await api.list_session_ac_ls_all(
                session_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListSessionACLsResponse,
            key="acls",
            fetcher=self.list_session_ac_ls,
            args={
                "session_id": session_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def create_process(
        self,
        *,
        name: str,
        project_id: Optional[str] = None,
        platform_id: Optional[str] = None,
        application_id: Optional[str] = None,
        input: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Process:
        """
        Create a process.
        Create a new process for the specified application on a specified platform.
        :param name: Name of the process.
        :param project_id: ID of the project in which the process was created.
        :param platform_id: ID of the platform for which the process was created.
        :param application_id: ID of the application for which the process was created.
        :param input: Process parameters in JSON format.
        :param tags: Tags of the process.
        :return: :class:`Process <Process>`

        Usage:
        ::

            result = await api.create_process(
                name="example",
            )
        """

        res = self._request(
            "POST",
            "/qaas/v1alpha1/processes",
            body=marshal_CreateProcessRequest(
                CreateProcessRequest(
                    name=name,
                    project_id=project_id,
                    platform_id=platform_id,
                    application_id=application_id,
                    input=input,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Process(res.json())

    async def get_process(
        self,
        *,
        process_id: str,
    ) -> Process:
        """
        Get process infrormation.
        Retrieve information about the provided **process ID**, such as name, status and progress.
        :param process_id: Unique ID of the process.
        :return: :class:`Process <Process>`

        Usage:
        ::

            result = await api.get_process(
                process_id="example",
            )
        """

        param_process_id = validate_path_param("process_id", process_id)

        res = self._request(
            "GET",
            f"/qaas/v1alpha1/processes/{param_process_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Process(res.json())

    async def wait_for_process(
        self,
        *,
        process_id: str,
        options: Optional[WaitForOptions[Process, Union[bool, Awaitable[bool]]]] = None,
    ) -> Process:
        """
        Get process infrormation.
        Retrieve information about the provided **process ID**, such as name, status and progress.
        :param process_id: Unique ID of the process.
        :return: :class:`Process <Process>`

        Usage:
        ::

            result = await api.get_process(
                process_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in PROCESS_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_process,
            options=options,
            args={
                "process_id": process_id,
            },
        )

    async def list_processes(
        self,
        *,
        application_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListProcessesRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> ListProcessesResponse:
        """
        List all processes.
        Retrieve information about all processes.
        :param application_id: List processes that have been created for this application.
        :param tags: List processes with these tags.
        :param page: Page number.
        :param page_size: Maximum number of processes to return per page.
        :param order_by: Sort order of the returned processes.
        :param project_id: List processes belonging to this project ID.
        :return: :class:`ListProcessesResponse <ListProcessesResponse>`

        Usage:
        ::

            result = await api.list_processes()
        """

        res = self._request(
            "GET",
            "/qaas/v1alpha1/processes",
            params={
                "application_id": application_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListProcessesResponse(res.json())

    async def list_processes_all(
        self,
        *,
        application_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListProcessesRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[Process]:
        """
        List all processes.
        Retrieve information about all processes.
        :param application_id: List processes that have been created for this application.
        :param tags: List processes with these tags.
        :param page: Page number.
        :param page_size: Maximum number of processes to return per page.
        :param order_by: Sort order of the returned processes.
        :param project_id: List processes belonging to this project ID.
        :return: :class:`List[Process] <List[Process]>`

        Usage:
        ::

            result = await api.list_processes_all()
        """

        return await fetch_all_pages_async(
            type=ListProcessesResponse,
            key="processes",
            fetcher=self.list_processes,
            args={
                "application_id": application_id,
                "tags": tags,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    async def update_process(
        self,
        *,
        process_id: str,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Process:
        """
        Update process information.
        Update process information of the provided **process ID**.
        :param process_id: Unique ID of the process.
        :param name: Name of the process.
        :param tags: Tags of the process.
        :return: :class:`Process <Process>`

        Usage:
        ::

            result = await api.update_process(
                process_id="example",
            )
        """

        param_process_id = validate_path_param("process_id", process_id)

        res = self._request(
            "PATCH",
            f"/qaas/v1alpha1/processes/{param_process_id}",
            body=marshal_UpdateProcessRequest(
                UpdateProcessRequest(
                    process_id=process_id,
                    name=name,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Process(res.json())

    async def cancel_process(
        self,
        *,
        process_id: str,
    ) -> Process:
        """
        Cancel a running process.
        Cancel a process by its unique ID. Intermediate results are still available.
        :param process_id: Unique ID of the process.
        :return: :class:`Process <Process>`

        Usage:
        ::

            result = await api.cancel_process(
                process_id="example",
            )
        """

        param_process_id = validate_path_param("process_id", process_id)

        res = self._request(
            "POST",
            f"/qaas/v1alpha1/processes/{param_process_id}/cancel",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Process(res.json())

    async def delete_process(
        self,
        *,
        process_id: str,
    ) -> None:
        """
        Delete an existing process.
        Delete a process by its unique ID and delete all its data.
        :param process_id: Unique ID of the process.

        Usage:
        ::

            result = await api.delete_process(
                process_id="example",
            )
        """

        param_process_id = validate_path_param("process_id", process_id)

        res = self._request(
            "DELETE",
            f"/qaas/v1alpha1/processes/{param_process_id}",
        )

        self._throw_on_error(res)

    async def list_process_results(
        self,
        *,
        process_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListProcessResultsRequestOrderBy] = None,
    ) -> ListProcessResultsResponse:
        """
        List all results of a process.
        Retrieve all intermediate and final result of a process.
        :param process_id: ID of the process.
        :param page: Page number.
        :param page_size: Maximum number of results to return per page.
        :param order_by: Sort order of the returned results.
        :return: :class:`ListProcessResultsResponse <ListProcessResultsResponse>`

        Usage:
        ::

            result = await api.list_process_results(
                process_id="example",
            )
        """

        param_process_id = validate_path_param("process_id", process_id)

        res = self._request(
            "GET",
            f"/qaas/v1alpha1/processes/{param_process_id}/results",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListProcessResultsResponse(res.json())

    async def list_process_results_all(
        self,
        *,
        process_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListProcessResultsRequestOrderBy] = None,
    ) -> List[ProcessResult]:
        """
        List all results of a process.
        Retrieve all intermediate and final result of a process.
        :param process_id: ID of the process.
        :param page: Page number.
        :param page_size: Maximum number of results to return per page.
        :param order_by: Sort order of the returned results.
        :return: :class:`List[ProcessResult] <List[ProcessResult]>`

        Usage:
        ::

            result = await api.list_process_results_all(
                process_id="example",
            )
        """

        return await fetch_all_pages_async(
            type=ListProcessResultsResponse,
            key="process_results",
            fetcher=self.list_process_results,
            args={
                "process_id": process_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def get_application(
        self,
        *,
        application_id: str,
    ) -> Application:
        """
        Get application information.
        Retrieve information about the provided **applcation ID**, such as name, type and compatible platforms.
        :param application_id: Unique ID of the application.
        :return: :class:`Application <Application>`

        Usage:
        ::

            result = await api.get_application(
                application_id="example",
            )
        """

        param_application_id = validate_path_param("application_id", application_id)

        res = self._request(
            "GET",
            f"/qaas/v1alpha1/applications/{param_application_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Application(res.json())

    async def list_applications(
        self,
        *,
        name: Optional[str] = None,
        application_type: Optional[ApplicationType] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListApplicationsRequestOrderBy] = None,
    ) -> ListApplicationsResponse:
        """
        List all available applications.
        Retrieve information about all applications.
        :param name: List applications with this name.
        :param application_type: List applications with this type.
        :param page: Page number.
        :param page_size: Maximum number of applications a to return per page.
        :param order_by: Sort order of the returned applications.
        :return: :class:`ListApplicationsResponse <ListApplicationsResponse>`

        Usage:
        ::

            result = await api.list_applications()
        """

        res = self._request(
            "GET",
            "/qaas/v1alpha1/applications",
            params={
                "application_type": application_type,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListApplicationsResponse(res.json())

    async def list_applications_all(
        self,
        *,
        name: Optional[str] = None,
        application_type: Optional[ApplicationType] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListApplicationsRequestOrderBy] = None,
    ) -> List[Application]:
        """
        List all available applications.
        Retrieve information about all applications.
        :param name: List applications with this name.
        :param application_type: List applications with this type.
        :param page: Page number.
        :param page_size: Maximum number of applications a to return per page.
        :param order_by: Sort order of the returned applications.
        :return: :class:`List[Application] <List[Application]>`

        Usage:
        ::

            result = await api.list_applications_all()
        """

        return await fetch_all_pages_async(
            type=ListApplicationsResponse,
            key="applications",
            fetcher=self.list_applications,
            args={
                "name": name,
                "application_type": application_type,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )
