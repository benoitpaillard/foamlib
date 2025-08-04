"""run the parametric study."""

# %%
from pathlib import Path
import asyncio
from foamlib import AsyncFoamCase
from foamlib.postprocessing.load_tables import of_cases

root = Path(__file__).parent

cases = [AsyncFoamCase(x) for x in of_cases(root / "Cases")]

async def run_all():
    await asyncio.gather(*(case.run() for case in cases))

asyncio.run(run_all())
# %%


