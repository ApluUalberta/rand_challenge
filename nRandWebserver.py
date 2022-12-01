from fastapi import FastAPI

import numpy


app = FastAPI()


@app.get("/{n}")
async def root(n: int):
    return {"rand": numpy.random.uniform(-9223372036854775808,
                                         9223372036854775807, n).tolist()}
