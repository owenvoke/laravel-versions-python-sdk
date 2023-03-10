# Laravel Versions Python

[![Latest Version on PyPi][ico-version]][link-pypi]
[![Software License][ico-license]](LICENSE.md)
[![Build Status][ico-github-actions]][link-github-actions]
[![Buy us a tree][ico-treeware-gifting]][link-treeware-gifting]

An SDK to easily work with the [Laravel Versions API](https://laravelversions.com)

## Install

Via Pip

```shell
pip install laravel-versions-sdk
```

## Usage

```python
from laravel_versions import LaravelVersions

laravel_versions = LaravelVersions()

versions = laravel_versions.versions()
version = laravel_versions.version(9)
```

| Available Methods                     | Description                                                                              |
|:--------------------------------------|:-----------------------------------------------------------------------------------------|
| `laravel_versions.versions()`         | Retrieve a `LaravelVersionsCollection` dict containing information for all versions.     |
| `laravel_versions.version("version")` | Retrieve a `LaravelVersionsSingular` dict containing information for a specific version. |

## Change log

Please see [CHANGELOG](CHANGELOG.md) for more information on what has changed recently.

## Testing

```shell
hatch shell

hatch run test
```

## Security

If you discover any security related issues, please email security@voke.dev instead of using the issue tracker.

## Credits

- [Owen Voke][link-author]
- [All Contributors][link-contributors]

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.

## Treeware

You're free to use this package, but if it makes it to your production environment you are required to buy the world a tree.

It’s now common knowledge that one of the best tools to tackle the climate crisis and keep our temperatures from rising above 1.5C is to plant trees. If you support this package and contribute to the Treeware forest you’ll be creating employment for local families and restoring wildlife habitats.

You can buy trees [here][link-treeware-gifting].

Read more about Treeware at [treeware.earth][link-treeware].

[ico-version]: https://img.shields.io/pypi/v/laravel-versions-sdk.svg?style=flat-square
[ico-license]: https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square
[ico-github-actions]: https://img.shields.io/github/actions/workflow/status/owenvoke/laravel-versions-python-sdk/tests.yml?branch=main&style=flat-square
[ico-treeware-gifting]: https://img.shields.io/badge/Treeware-%F0%9F%8C%B3-lightgreen?style=flat-square

[link-pypi]: https://pypi.org/project/laravel-versions-sdk
[link-github-actions]: https://github.com/owenvoke/laravel-versions-python-sdk/actions
[link-treeware]: https://treeware.earth
[link-treeware-gifting]: https://ecologi.com/owenvoke?gift-trees
[link-author]: https://github.com/owenvoke
[link-contributors]: https://github.com/owenvoke/laravel-versions-python-sdk/contributors
