## [1.7.3](https://gitlab.evanrichardsonphotography.com/erichardson/py-eagle-mqtt/compare/v1.7.2...v1.7.3) (2021-04-12)


### Bug Fixes

* Empty commit to get recent changes into build (last commit should've been labeled this) ([e513752](https://gitlab.evanrichardsonphotography.com/erichardson/py-eagle-mqtt/commit/e513752c46cc0b3beb93530f6549661d67196905))

## [1.7.2](https://gitlab.evanrichardsonphotography.com/erichardson/py-eagle-mqtt/compare/v1.7.1...v1.7.2) (2021-04-08)


### Bug Fixes

* Cleanup CHANGELOG.md since using new semantic-release format ([a72ac7a](https://gitlab.evanrichardsonphotography.com/erichardson/py-eagle-mqtt/commit/a72ac7a1df91cb2231e38e8bbceb5ccf9c93328a))
* fix asset info for git commit ([00c95c4](https://gitlab.evanrichardsonphotography.com/erichardson/py-eagle-mqtt/commit/00c95c42ea98921a1b2da9d2069d41e8e32f34f5))

## [1.7.1](https://gitlab.evanrichardsonphotography.com/erichardson/py-eagle-mqtt/compare/v1.7.0...v1.7.1) (2021-04-08)


### Bug Fixes

* refactor Dockerfile to improve build ([40ac8c5](https://gitlab.evanrichardsonphotography.com/erichardson/py-eagle-mqtt/commit/40ac8c5ada9b993f53b72dcc14b2d9b7cd183e2f))

## [1.6.10] - 2021-04-06

### Fixed

- Fix docker tagging issue

## [1.6.9] - 2021-04-06

### Fixed

- Remove release-cli section of CI file
- Add updated README.md

## [1.6.8] - 2021-04-06

### Changed

- Fixed slight issue with tagging

## [1.6.7] - 2021-04-06

### Changed

- Updated base image to Python 3.9.4-alpine3.13
- Moved changes to this file

### Removed

- Changelog from README.md

## [1.6.6] - 2021-04-03

### Added

- Added CI/CD pipeline to project

### Changed

- Moved project to my own personal Gitlab server for CI/CD pipelines as well as to run security scans on the container image and code

- Updated base image to Python 3.9.3-alpine3.12

## [Unversioned history]

- 2019-07-24: Rebase to python 3.7.4-alpine3.10, update bottle to 0.12.17

- 2019-04-12: Rebase to python 3.7.3-alpine3.9

- 2019-03-08: Rebase to python 3.7.2-alpine3.9, update bottle and astral versions to latest

- 2019-01-03: Rebase to python 3.7.2-alpine3.8, changed logging level to Info (should output to /var/log/tHome/eagle.log)

- 2018-09-10: Ported to Python3, Added pricing info.  Merged into master branch
