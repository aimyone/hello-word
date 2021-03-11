from bin.module.get_token_b import *
authorization = get_token('c12345678','18797908791','BPassword')
print(authorization)
# def get_header():
#     headers = {
#         "X-Organ-Id": "659599591487537152",
#         "authorization": "eyJhbGciOiJSUzI1NiJ9.eyJkdCI6InBjX3dlYiIsInR0IjoiMSIsInN1YiI6IjY0MzM1MDkzMTUzOTk4NDM4NCIsIlVOb25jZSI6ImUxMmE2ZWQ0LTU3NDEtNDI0NS04MTJmLTRmYTMxNmVlN2E4NCIsInJvbGUiOiI1ODUwMTQ2NDUxNzU4NDQ4NjQiLCJpc3MiOiJ5anl6LmNvbSIsImV4cCI6MTYxMzg4NjY2OCwiaWF0IjoxNjEzNzEzODY4LCJqdGkiOiJmYTkyY2M4OS0xOTE0LTRiY2ItYTdkNy02YzVkMjJkMWYyNzIifQ.fpj638ZuA4KxAYNdBHuJTYHsqH9SNE-48wb9WPjb2QaLQrnEWf78LcY5mKnEqXahSGq574Sg7ILzZrf6MkWZCkpEI52uZf0xYRh3QXz63ztSAFhAFVrq1tUJ-hphEZ6w4TusA222xP8rdfsTSaGvhF3gIu8cKBA_-NAYx1o3xzA"
#     }
#     return headers
# a = get_header()
# print(a)
def get_header():
    headers = {
        "X-Organ-Id": "659599591487537152",
        "authorization": authorization,
        "Content-Type":"application/json"
    }
    return headers
a = get_header()
print(a)
