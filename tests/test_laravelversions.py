import requests_mock

from laravel_versions import LaravelVersions

laravel_versions = LaravelVersions()


def test_all():
    with requests_mock.Mocker() as m:
        m.get(
            url="https://laravelversions.com/api/versions",
            json={
                "data": [
                    {
                        "major": 9,
                        "latest_minor": 0,
                        "latest_patch": 0,
                        "latest": "9.0.0",
                        "is_lts": False,
                        "released_at": "2022-02-08T00:00:00.000000Z",
                        "ends_bugfixes_at": "2023-08-08T00:00:00.000000Z",
                        "ends_securityfixes_at": "2024-02-08T00:00:00.000000Z",
                        "status": "active",
                        "links": [
                            {
                                "type": "GET",
                                "rel": "self",
                                "href": "https://laravelversions.com/api/versions/9",
                            },
                            {
                                "type": "GET",
                                "rel": "latest",
                                "href": "https://laravelversions.com/api/versions/9.0.0",
                            },
                        ],
                        "global": {
                            "latest_version": "9.0.0",
                            "latest_version_is_lts": False,
                        },
                    }
                ]
            },
        )
        versions = laravel_versions.versions()

        assert type(versions) == dict
        assert len(versions.get("data")) == 1


def test_version():
    with requests_mock.Mocker() as m:
        m.get(
            url="https://laravelversions.com/api/versions/9",
            json={
                "data": {
                    "major": 9,
                    "latest_minor": 0,
                    "latest_patch": 0,
                    "latest": "9.0.0",
                    "is_lts": False,
                    "released_at": "2022-02-08T00:00:00.000000Z",
                    "ends_bugfixes_at": "2023-08-08T00:00:00.000000Z",
                    "ends_securityfixes_at": "2024-02-08T00:00:00.000000Z",
                    "status": "active",
                    "links": [
                        {
                            "type": "GET",
                            "rel": "self",
                            "href": "https://laravelversions.com/api/versions/9",
                        },
                        {
                            "type": "GET",
                            "rel": "latest",
                            "href": "https://laravelversions.com/api/versions/9.0.0",
                        },
                    ],
                    "global": {
                        "latest_version": "9.0.0",
                        "latest_version_is_lts": False,
                    },
                }
            },
        )
        versions = laravel_versions.version("9")

        assert type(versions) == dict
        assert type(versions.get("data")) == dict
