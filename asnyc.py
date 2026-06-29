# when implementing third-party, you use the async await keywords
# @app.get('/')
# async def read_results():
#     results = await some_library()
#     return results

# you do not need use it for normal functions.
# @app.get('/')
# def results():
#     results = some_library()
#     return results