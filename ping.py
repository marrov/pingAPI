from pingparsing import PingParsing
from asyncio import create_subprocess_exec
from asyncio.subprocess import PIPE


class Ping():
    """A ping process with asynchronous run functionality.
    Attributes:
      process: The ping process object (asyncio.subprocess.Process).
      stdout: The output string of the ping command. 
      stderr: The error string of the ping command.
      output: The parsed dict of the stats from the ping output.
      host_addr: The address (website) to be pinged.
      n_pings: The number of times the host should be pinged.
      interval: The wait interval in secons between pings.
    """

    process = None
    stdout = ''
    stderr = ''
    output = {}

    def __init__(self, host_addr: str, n_pings: int, interval: float = 0.2):
        self.host_addr = host_addr
        self.n_pings = n_pings
        self.interval = interval

    async def run(self):
        """Asynchronously run a linux ping command."""
        # Define the ping command to run
        cmd = ['ping',
               self.host_addr,
               f'-c {self.n_pings}',
               f'-i {self.interval}']

        # Asynchronously execute the ping command
        self.process = await create_subprocess_exec(
            *cmd,
            stdout=PIPE,
            stderr=PIPE)

        # Retrieve the output and error
        self.stdout, self.stderr = await self.process.communicate()
        
        # Parse the output of the ping command
        self._parse()

    def _parse(self):
        """Parse the output of a ping command."""
        # Decode stdout and stderr from byte strings to strings
        self.stdout = str(self.stdout.decode("utf-8")).strip()
        self.stderr = str(self.stderr.decode("utf-8")).strip()
        
        # Parse stdout to extract ping stats to output if succesful ping
        if not self.process.returncode:
            self.output = PingParsing().parse(self.stdout).as_dict()
            # Add wall time (not given by PingParsing)
            self.output['wall_time'] = int(
                self.stdout.split('time')[-1].split('ms')[0].strip())
