from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class GlobalErrorHandlerMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        """Catch unhandled exceptions globally (like 500 errors)."""
        return JsonResponse(
            {
                "error": True,
                "status": 500,
                "type": exception.__class__.__name__,
                "message": str(exception),
            },
            status=500,
        )

    def process_response(self, request, response):
        """Handle all HTTP error codes consistently."""
        status_code = response.status_code

        error_messages = {
            401: "Unauthorized 🔑 — Please log in first.",
            402: "Payment Required 💳 — Access restricted until payment.",
            403: "Forbidden 🚫 — You don’t have permission to access this resource.",
            404: "Not Found 🔍 — The requested resource doesn’t exist.",
            405: "Method Not Allowed 🚫 — This HTTP method is not allowed here.",
            408: "Request Timeout ⏳ — The server took too long to respond.",
            409: "Conflict ⚔️ — There’s a conflict with current resource state.",
            415: "Unsupported Media Type 📁 — Check your Content-Type header.",
            429: "Too Many Requests 🕒 — Please slow down.",
            500: "Internal Server Error 💥 — Something went wrong on our side.",
            502: "Bad Gateway 🔌 — Invalid response from upstream server.",
            503: "Service Unavailable 💤 — Try again later.",
            504: "Gateway Timeout ⏰ — Upstream server didn’t respond in time.",
        }

        if status_code in error_messages:
            return JsonResponse(
                {
                    "error": True,
                    "status": status_code,
                    "message": error_messages[status_code],
                },
                status=status_code,
            )

        # otherwise return normal response
        return response
