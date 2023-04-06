import os
from pathlib import Path

from endpoints import (
    failover,
    live_postcode_form,
    live_postcode_view,
    live_uprn_view,
    redirect_root_to_postcode_form,
    sandbox_postcode_view,
    sandbox_uprn_view,
)
from mangum import Mangum
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from utils import ForwardedForMiddleware, i18nMiddleware

if sentry_dsn := os.environ.get("SENTRY_DSN"):
    import sentry_sdk
    from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration
    from sentry_sdk.integrations.starlette import StarletteIntegration

    sentry_sdk.init(
        dsn=sentry_dsn,
        traces_sample_rate=0,
        integrations=[
            StarletteIntegration(transaction_style="endpoint"),
            AwsLambdaIntegration(),
        ],
    )

routes = [
    Route("/", endpoint=redirect_root_to_postcode_form),
    Route("/failover", endpoint=failover, name="failover"),
    Route(
        "/i-am-a/voter/your-election-information",
        endpoint=live_postcode_form,
        name="live_postcode_form_en",
    ),
    Route(
        "/polling-stations/address/{postcode}/{uprn}",
        endpoint=live_uprn_view,
        name="live_uprn_en",
    ),
    Route(
        "/polling-stations",
        endpoint=live_postcode_view,
        name="live_postcode_en",
    ),
    Route(
        "/cy/rwyf-yneg-pleidleisiwr/pleidleisiwr/gwybodaeth-etholiad",
        endpoint=live_postcode_form,
        name="live_postcode_form_cy",
    ),
    Route(
        "/cy/polling-stations/{postcode}/{uprn}",
        endpoint=live_uprn_view,
        name="live_uprn_cy",
    ),
    Route(
        "/cy/polling-stations",
        endpoint=live_postcode_view,
        name="live_postcode_cy",
    ),
    # Sandbox
    Route(
        "/sandbox/polling-stations",
        endpoint=sandbox_postcode_view,
        name="sandbox_postcode_en",
    ),
    Route(
        "/cy/sandbox/polling-stations",
        endpoint=sandbox_postcode_view,
        name="sandbox_postcode_cy",
    ),
    Route(
        "/sandbox/polling-stations/{postcode}/{uprn}",
        endpoint=sandbox_uprn_view,
        name="sandbox_uprn_en",
    ),
    Route(
        "/cy/sandbox/polling-stations/{postcode}/{uprn}",
        endpoint=sandbox_uprn_view,
        name="sandbox_uprn_cy",
    ),
    Mount(
        "/themes/",
        app=StaticFiles(directory=Path(__file__).parent / "themes"),
        name="themes",
    ),
    Mount(
        "/static/",
        app=StaticFiles(directory=Path(__file__).parent / "static"),
        name="static",
    ),
]

app = Starlette(
    debug=True,
    routes=routes,
    middleware=[
        Middleware(i18nMiddleware),
        Middleware(ForwardedForMiddleware),
    ],
)

handler = Mangum(app)
