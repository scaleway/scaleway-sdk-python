# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Optional

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
    ApplicationType,
    ListApplicationsRequestOrderBy,
    ListBookingsRequestOrderBy,
    ListJobResultsRequestOrderBy,
    ListJobsRequestOrderBy,
    ListModelsRequestOrderBy,
    ListPlatformsRequestOrderBy,
    ListProcessResultsRequestOrderBy,
    ListProcessesRequestOrderBy,
    ListSessionACLsRequestOrderBy,
    ListSessionsRequestOrderBy,
    PlatformTechnology,
    PlatformType,
    SessionAccess,
    Application,
    Booking,
    CreateJobRequest,
    CreateModelRequest,
    CreateProcessRequest,
    CreateSessionRequest,
    CreateSessionRequestBookingDemand,
    Job,
    JobCircuit,
    JobResult,
    ListApplicationsResponse,
    ListBookingsResponse,
    ListJobResultsResponse,
    ListJobsResponse,
    ListModelsResponse,
    ListPlatformsResponse,
    ListProcessResultsResponse,
    ListProcessesResponse,
    ListSessionACLsResponse,
    ListSessionsResponse,
    Model,
    Platform,
    Process,
    ProcessResult,
    Session,
    UpdateBookingRequest,
    UpdateJobRequest,
    UpdateProcessRequest,
    UpdateSessionRequest,
)
from .content import (
    BOOKING_TRANSIENT_STATUSES,
    JOB_TRANSIENT_STATUSES,
    PROCESS_TRANSIENT_STATUSES,
    SESSION_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_JobCircuit,
    unmarshal_Application,
    unmarshal_Booking,
    unmarshal_Job,
    unmarshal_Model,
    unmarshal_Platform,
    unmarshal_Process,
    unmarshal_Session,
    unmarshal_ListApplicationsResponse,
    unmarshal_ListBookingsResponse,
    unmarshal_ListJobResultsResponse,
    unmarshal_ListJobsResponse,
    unmarshal_ListModelsResponse,
    unmarshal_ListPlatformsResponse,
    unmarshal_ListProcessResultsResponse,
    unmarshal_ListProcessesResponse,
    unmarshal_ListSessionACLsResponse,
    unmarshal_ListSessionsResponse,
    marshal_CreateJobRequest,
    marshal_CreateModelRequest,
    marshal_CreateProcessRequest,
    marshal_CreateSessionRequest,
    marshal_UpdateBookingRequest,
    marshal_UpdateJobRequest,
    marshal_UpdateProcessRequest,
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
        tags: Optional[list[str]] = None,
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
        tags: Optional[list[str]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobsRequestOrderBy] = None,
    ) -> list[Job]:
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
        :return: :class:`list[Job] <list[Job]>`

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

    def list_job_results(
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

            result = api.list_job_results(
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

    def list_job_results_all(
        self,
        *,
        job_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListJobResultsRequestOrderBy] = None,
    ) -> list[JobResult]:
        """
        List all results of a job.
        Retrieve all intermediate and final results of a job.
        :param job_id: ID of the job.
        :param page: Page number.
        :param page_size: Maximum number of results to return per page.
        :param order_by: Sort order of the returned results.
        :return: :class:`list[JobResult] <list[JobResult]>`

        Usage:
        ::

            result = api.list_job_results_all(
                job_id="example",
            )
        """

        return fetch_all_pages(
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

    def create_job(
        self,
        *,
        name: str,
        session_id: str,
        circuit: JobCircuit,
        tags: Optional[list[str]] = None,
        max_duration: Optional[str] = None,
        model_id: Optional[str] = None,
        parameters: Optional[str] = None,
    ) -> Job:
        """
        Create a job.
        Create a job to be executed inside a session.
        :param name: Name of the job.
        :param session_id: Session in which the job is executed.
        :param circuit: Quantum circuit that should be executed.
        :param tags: Tags of the job.
        :param max_duration: Maximum duration of the job.
        :param model_id: Computation model ID to be executed by the job.
        :param parameters: Execution parameters for this job.
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
                    model_id=model_id,
                    parameters=parameters,
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
        tags: Optional[list[str]] = None,
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

    def delete_job(
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

            result = api.delete_job(
                job_id="example",
            )
        """

        param_job_id = validate_path_param("job_id", job_id)

        res = self._request(
            "DELETE",
            f"/qaas/v1alpha1/jobs/{param_job_id}",
        )

        self._throw_on_error(res)

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

            result = api.list_platforms()
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

    def list_platforms_all(
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
    ) -> list[Platform]:
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
        :return: :class:`list[Platform] <list[Platform]>`

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
                "backend_name": backend_name,
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
        Get session information.
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
        Get session information.
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
        tags: Optional[list[str]] = None,
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
        tags: Optional[list[str]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSessionsRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> list[Session]:
        """
        List all sessions.
        Retrieve information about all sessions.
        :param platform_id: List sessions that have been created for this platform.
        :param tags: List sessions with these tags.
        :param page: Page number.
        :param page_size: Maximum number of sessions to return per page.
        :param order_by: Sort order of the returned sessions.
        :param project_id: List sessions belonging to this project ID.
        :return: :class:`list[Session] <list[Session]>`

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
        tags: Optional[list[str]] = None,
        deduplication_id: Optional[str] = None,
        booking_demand: Optional[CreateSessionRequestBookingDemand] = None,
        model_id: Optional[str] = None,
        parameters: Optional[str] = None,
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
        :param booking_demand: A booking demand to schedule the session, only applicable if the platform is bookable.
        :param model_id: Default computation model ID to be executed by job assigned to this session.
        :param parameters: Optional platform configuration parameters applied to this session.
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
                    booking_demand=booking_demand,
                    model_id=model_id,
                    parameters=parameters,
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
        tags: Optional[list[str]] = None,
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

    def terminate_session(
        self,
        *,
        session_id: str,
    ) -> Session:
        """
        Terminate an existing session.
        Terminate a session by its unique ID and cancel all its attached jobs and booking.
        :param session_id: Unique ID of the session.
        :return: :class:`Session <Session>`

        Usage:
        ::

            result = api.terminate_session(
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

    def delete_session(
        self,
        *,
        session_id: str,
    ) -> None:
        """
        Delete an existing session.
        Delete a session by its unique ID and delete all its attached job and booking.
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

    def list_session_ac_ls(
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

            result = api.list_session_ac_ls(
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

    def list_session_ac_ls_all(
        self,
        *,
        session_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSessionACLsRequestOrderBy] = None,
    ) -> list[SessionAccess]:
        """
        :param session_id:
        :param page:
        :param page_size:
        :param order_by:
        :return: :class:`list[SessionAccess] <list[SessionAccess]>`

        Usage:
        ::

            result = api.list_session_ac_ls_all(
                session_id="example",
            )
        """

        return fetch_all_pages(
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

    def create_process(
        self,
        *,
        name: str,
        project_id: Optional[str] = None,
        platform_id: Optional[str] = None,
        application_id: Optional[str] = None,
        input: Optional[str] = None,
        tags: Optional[list[str]] = None,
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

            result = api.create_process(
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

    def get_process(
        self,
        *,
        process_id: str,
    ) -> Process:
        """
        Get process information.
        Retrieve information about the provided **process ID**, such as name, status and progress.
        :param process_id: Unique ID of the process.
        :return: :class:`Process <Process>`

        Usage:
        ::

            result = api.get_process(
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

    def wait_for_process(
        self,
        *,
        process_id: str,
        options: Optional[WaitForOptions[Process, bool]] = None,
    ) -> Process:
        """
        Get process information.
        Retrieve information about the provided **process ID**, such as name, status and progress.
        :param process_id: Unique ID of the process.
        :return: :class:`Process <Process>`

        Usage:
        ::

            result = api.get_process(
                process_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in PROCESS_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_process,
            options=options,
            args={
                "process_id": process_id,
            },
        )

    def list_processes(
        self,
        *,
        application_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
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

            result = api.list_processes()
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

    def list_processes_all(
        self,
        *,
        application_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListProcessesRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> list[Process]:
        """
        List all processes.
        Retrieve information about all processes.
        :param application_id: List processes that have been created for this application.
        :param tags: List processes with these tags.
        :param page: Page number.
        :param page_size: Maximum number of processes to return per page.
        :param order_by: Sort order of the returned processes.
        :param project_id: List processes belonging to this project ID.
        :return: :class:`list[Process] <list[Process]>`

        Usage:
        ::

            result = api.list_processes_all()
        """

        return fetch_all_pages(
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

    def update_process(
        self,
        *,
        process_id: str,
        name: Optional[str] = None,
        tags: Optional[list[str]] = None,
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

            result = api.update_process(
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

    def cancel_process(
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

            result = api.cancel_process(
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

    def delete_process(
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

            result = api.delete_process(
                process_id="example",
            )
        """

        param_process_id = validate_path_param("process_id", process_id)

        res = self._request(
            "DELETE",
            f"/qaas/v1alpha1/processes/{param_process_id}",
        )

        self._throw_on_error(res)

    def list_process_results(
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

            result = api.list_process_results(
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

    def list_process_results_all(
        self,
        *,
        process_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListProcessResultsRequestOrderBy] = None,
    ) -> list[ProcessResult]:
        """
        List all results of a process.
        Retrieve all intermediate and final result of a process.
        :param process_id: ID of the process.
        :param page: Page number.
        :param page_size: Maximum number of results to return per page.
        :param order_by: Sort order of the returned results.
        :return: :class:`list[ProcessResult] <list[ProcessResult]>`

        Usage:
        ::

            result = api.list_process_results_all(
                process_id="example",
            )
        """

        return fetch_all_pages(
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

    def get_application(
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

            result = api.get_application(
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

    def list_applications(
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

            result = api.list_applications()
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

    def list_applications_all(
        self,
        *,
        name: Optional[str] = None,
        application_type: Optional[ApplicationType] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListApplicationsRequestOrderBy] = None,
    ) -> list[Application]:
        """
        List all available applications.
        Retrieve information about all applications.
        :param name: List applications with this name.
        :param application_type: List applications with this type.
        :param page: Page number.
        :param page_size: Maximum number of applications a to return per page.
        :param order_by: Sort order of the returned applications.
        :return: :class:`list[Application] <list[Application]>`

        Usage:
        ::

            result = api.list_applications_all()
        """

        return fetch_all_pages(
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

    def get_booking(
        self,
        *,
        booking_id: str,
    ) -> Booking:
        """
        Get booking information.
        Retrieve information about the provided **booking ID**, such as description, status and progress message.
        :param booking_id: Unique ID of the booking.
        :return: :class:`Booking <Booking>`

        Usage:
        ::

            result = api.get_booking(
                booking_id="example",
            )
        """

        param_booking_id = validate_path_param("booking_id", booking_id)

        res = self._request(
            "GET",
            f"/qaas/v1alpha1/bookings/{param_booking_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Booking(res.json())

    def wait_for_booking(
        self,
        *,
        booking_id: str,
        options: Optional[WaitForOptions[Booking, bool]] = None,
    ) -> Booking:
        """
        Get booking information.
        Retrieve information about the provided **booking ID**, such as description, status and progress message.
        :param booking_id: Unique ID of the booking.
        :return: :class:`Booking <Booking>`

        Usage:
        ::

            result = api.get_booking(
                booking_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in BOOKING_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_booking,
            options=options,
            args={
                "booking_id": booking_id,
            },
        )

    def list_bookings(
        self,
        *,
        project_id: Optional[str] = None,
        platform_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListBookingsRequestOrderBy] = None,
    ) -> ListBookingsResponse:
        """
        List all bookings according the filter.
        Retrieve information about all bookings of the provided **project ID** or ** platform ID**.
        :param project_id: List bookings belonging to this project ID.
        :param platform_id: List bookings attached to this platform ID.
        :param page: Page number.
        :param page_size: Maximum number of results to return per page.
        :param order_by: Sort order of the returned results.
        :return: :class:`ListBookingsResponse <ListBookingsResponse>`

        Usage:
        ::

            result = api.list_bookings()
        """

        res = self._request(
            "GET",
            "/qaas/v1alpha1/bookings",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "platform_id": platform_id,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListBookingsResponse(res.json())

    def list_bookings_all(
        self,
        *,
        project_id: Optional[str] = None,
        platform_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListBookingsRequestOrderBy] = None,
    ) -> list[Booking]:
        """
        List all bookings according the filter.
        Retrieve information about all bookings of the provided **project ID** or ** platform ID**.
        :param project_id: List bookings belonging to this project ID.
        :param platform_id: List bookings attached to this platform ID.
        :param page: Page number.
        :param page_size: Maximum number of results to return per page.
        :param order_by: Sort order of the returned results.
        :return: :class:`list[Booking] <list[Booking]>`

        Usage:
        ::

            result = api.list_bookings_all()
        """

        return fetch_all_pages(
            type=ListBookingsResponse,
            key="bookings",
            fetcher=self.list_bookings,
            args={
                "project_id": project_id,
                "platform_id": platform_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    def update_booking(
        self,
        *,
        booking_id: str,
        description: Optional[str] = None,
    ) -> Booking:
        """
        Update booking information.
        Update booking information of the provided **booking ID**.
        :param booking_id: Unique ID of the booking.
        :param description: Description of the booking slot.
        :return: :class:`Booking <Booking>`

        Usage:
        ::

            result = api.update_booking(
                booking_id="example",
            )
        """

        param_booking_id = validate_path_param("booking_id", booking_id)

        res = self._request(
            "PATCH",
            f"/qaas/v1alpha1/bookings/{param_booking_id}",
            body=marshal_UpdateBookingRequest(
                UpdateBookingRequest(
                    booking_id=booking_id,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Booking(res.json())

    def create_model(
        self,
        *,
        project_id: Optional[str] = None,
        payload: Optional[str] = None,
    ) -> Model:
        """
        Create a new model.
        Create and register a new model that can be executed through next jobs. A model can also be assigned to a Session.
        :param project_id: Project ID to attach this model.
        :param payload: The serialized model data.
        :return: :class:`Model <Model>`

        Usage:
        ::

            result = api.create_model()
        """

        res = self._request(
            "POST",
            "/qaas/v1alpha1/models",
            body=marshal_CreateModelRequest(
                CreateModelRequest(
                    project_id=project_id,
                    payload=payload,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Model(res.json())

    def get_model(
        self,
        *,
        model_id: str,
    ) -> Model:
        """
        Get model information.
        Retrieve information about of the provided **model ID**.
        :param model_id: Unique ID of the model.
        :return: :class:`Model <Model>`

        Usage:
        ::

            result = api.get_model(
                model_id="example",
            )
        """

        param_model_id = validate_path_param("model_id", model_id)

        res = self._request(
            "GET",
            f"/qaas/v1alpha1/models/{param_model_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Model(res.json())

    def list_models(
        self,
        *,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListModelsRequestOrderBy] = None,
    ) -> ListModelsResponse:
        """
        List all models attached to the **project ID**.
        Retrieve information about all models of the provided **project ID**.
        :param project_id: List models belonging to this project ID.
        :param page: Page number.
        :param page_size: Maximum number of results to return per page.
        :param order_by: Sort order of the returned results.
        :return: :class:`ListModelsResponse <ListModelsResponse>`

        Usage:
        ::

            result = api.list_models()
        """

        res = self._request(
            "GET",
            "/qaas/v1alpha1/models",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListModelsResponse(res.json())

    def list_models_all(
        self,
        *,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListModelsRequestOrderBy] = None,
    ) -> list[Model]:
        """
        List all models attached to the **project ID**.
        Retrieve information about all models of the provided **project ID**.
        :param project_id: List models belonging to this project ID.
        :param page: Page number.
        :param page_size: Maximum number of results to return per page.
        :param order_by: Sort order of the returned results.
        :return: :class:`list[Model] <list[Model]>`

        Usage:
        ::

            result = api.list_models_all()
        """

        return fetch_all_pages(
            type=ListModelsResponse,
            key="models",
            fetcher=self.list_models,
            args={
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )
