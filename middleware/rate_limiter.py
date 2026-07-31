import time
from collections import defaultdict
from typing import Callable, Awaitable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from starlette.types import ASGIApp


class RateLimiterMiddleware(BaseHTTPMiddleware):
    # Simple rate limit settings
    RATE_LIMIT_DURATION = 60  # in seconds
    RATE_LIMIT_REQUESTS = 100  # max requests per duration

    def __init__(self, app: ASGIApp):
        super().__init__(app)
        # This is a simple in-memory store for request timestamps.
        # For a production application, you would want to use a more robust
        # and shared storage like Redis to handle multiple server processes/workers.
        self.request_counts = defaultdict(list)

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        # Use the client's IP address as a unique identifier.
        client_ip = request.client.host if request.client else "unknown"

        current_time = time.time()

        # Get the list of timestamps for the client's IP
        request_timestamps = self.request_counts[client_ip]

        # Remove timestamps that are older than the rate limit duration window
        # This is an efficient way to keep the list from growing indefinitely
        while request_timestamps and request_timestamps[0] <= current_time - self.RATE_LIMIT_DURATION:
            request_timestamps.pop(0)

        # If the number of requests in the current window exceeds the limit, block it.
        if len(request_timestamps) >= self.RATE_LIMIT_REQUESTS:
            return JSONResponse(
                status_code=429,  # Too Many Requests
                content={"detail": f"Too many requests. Try again in {self.RATE_LIMIT_DURATION} seconds."},
            )

        # Record the timestamp of the current request
        self.request_counts[client_ip].append(current_time)

        # Allow the request to proceed to the next middleware or the endpoint
        response = await call_next(request)
        return response
