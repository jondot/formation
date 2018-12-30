from formation.for_requests import client, json_response
from formation.middleware import request_logger
from attr import attrib, attrs
from attrs_serde import serde
import structlog


@serde
@attrs
class Query(object):
    owner = attrib(metadata={"to": [":owner"]})
    repo = attrib(metadata={"to": [":repo"]})


@client
class Github(object):
    base_uri = "https://api.github.com/"
    middleware = [request_logger(structlog.getLogger())]
    response_as = json_response

    def stargazers(self, owner, repo):
        return self.request.get(
            "repos/:owner/:repo/stargazers", params=Query(owner, repo)
        )

    def download(self, release):
        pass


if __name__ == "__main__":
    github = Github()
    (res, _, _) = github.stargazers("jondot", "formation")
    print(res)
