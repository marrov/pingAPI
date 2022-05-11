from ping import Ping
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class Command(BaseModel):
    """Extends pydantic's BaseModel for use as the request
    body on a FastAPI get request of the linux ping command.
    Attributes:
      host_addr: The address (website) to be pinged.
      n_pings: The number of times the host should be pinged.
      interval: The wait interval in secons between pings.
    """
    host_addr: str = 'www.kambi.com'
    n_pings: int = 5
    interval: float = 0.2

class CustomError(BaseModel):
    """Extends pydantic's BaseModel for use as the response
    body after an error with a FastAPI get request.
    Attributes:
      detail: Provides details about the error.
    """
    detail: dict

# Explicit declaration of recurrent errors (so they show up in the API docs)
errors = {
    400: {"model": CustomError},
    503: {"model": CustomError}
}

app = FastAPI()


@app.post('/ping/', responses=errors)
async def ping(command: Command):
    # Instantiate Ping using the request body arguments
    ping = Ping(host_addr=command.host_addr,
                n_pings=command.n_pings,
                interval=command.interval)

    # Run and wait for the ping command to finish (async)
    await ping.run()

    # Raise error from stderr if the ping was not succesful
    if ping.process.returncode:
        return JSONResponse(status_code=400, content={'Error message': ping.stderr})

    # Raise error if API is shutdown
    if ping.output["packet_transmit"] != ping.n_pings:
        return JSONResponse(status_code=503, content={'Error message': {
            'Type': 'Request ended prematurely',
            f'Premature output ({ping.output["packet_transmit"]} out of {ping.n_pings} packets)': ping.output
        } })

    return ping.output
