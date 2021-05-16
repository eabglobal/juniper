.. currentmodule:: juniper

Juniper Changelog
===============

Version 0.5.5
-------------

Released on May 16 2021

- Updating the dependencies of juniper (thanks to andreburto).


Version 0.5.4
-------------

Released on Aug 20 2020

- Updated the juniper dependencies to prevent constant failures when installing awscli.
  Before this change, juniper had a top fix version for docker-compose as well as PyYAML
  these limits have been updated (pdiazvargas).


Version 0.5.3
-------------

Released on Nov 15 2019

- Support partial builds. Ability to build a subset of the functions defined in the manifest
  thanks to @parhumeab for the contribution. (pr/43)


Version 0.5.2
-------------

Released on July 2 2019

- Support adding binaries to the `bin` folder of a lambda layer (issues/43)


Version 0.5.1
-------------

Released on June 28th 2019

- Ability to configure pip using a pip.conf file (/issues/40)
- Updated the README documentation to keep it up to date with latest
  feature enhancements


Version 0.5.0
-------------

Released on June 24th 2019

- New feature to external libraries (/issues/39)


Version 0.4.0
-------------

Released on April 18th 2019, codename Fondo 4

- New feature to support layers (/issues/38)


Version 0.3.0
-------------

Released on April 5th 2019, codename Fondo I

- Deprecating the package section as a way to override output directory. Using
  the globals section instead.
- Adding a new cli flag `skip-clean` as a way to control weather or not to "clean"
  the output directory before the packaging process starts.
- Explicitly building a new output directory. Before, we relied on the internal
  volume mapping of the docker container as the entity that would create the output
  directory. Now, juniper will delete and create the directory.


Version 0.2.6
-------------

Released on March 22nd 2019, codename Izzi.6

- Setting specific versions of install dependencies.


Version 0.2.5
-------------

Released on March 22nd 2019, codename Izzi.5

- Updating documentation based on feedback.
- Fixing docker mapping issue when includes ended in slash (/issues/24)
- Fixing a bug when packaging includes './' (/issues/30)


Version 0.2.4
-------------

Released on March 17th 2019, codename Izzi.4

- Mayor refactoring of docker-compose building process. Using jinja2 (/issues/21)
- Ability to specify a new docker image globaly and per function (/issue/21)
- Simplified documentation to make the project more readable and accesible (/issue/21)
- Added features section to documentation to keep track of ongoing dev (/issue/21)


Version 0.2.2
-------------

Released on March 4th 2019, codename Izzi.2

- Added the requirements as optional parameter in the manifest (/issues/19)


Version 0.2.1
-------------

Released on March 2nd 2019, codename Izzi

- Added validation of the manifest file (/issues/15)
  Thanks to safuya for the contribution.

- Added initial set of badges to the README (/issues/13)


Version 0.1
-----------

Released on February 1st 2019, codename Fondo

- First public preview release.

- Juniper's MVP is fully complete!
