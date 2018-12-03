## iReporter Application

[![Build Status](https://travis-ci.org/Elisha-Misoi/iReporter_V1.svg?branch=develop)](https://travis-ci.org/Elisha-Misoi/iReporter_V1)

[![Coverage Status](https://coveralls.io/repos/github/Phionanamugga/iReporter-API/badge.svg?branch=develop)](https://coveralls.io/github/Phionanamugga/iReporter-API?branch=develop)

Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

## Features
1. Users can create an account and log in.
2. Users can create a ​ red-flag ​ record (An incident linked to corruption)
3. Users can create ​ intervention​​ record​ ​ (a call for a government agency to intervene e.g repair bad road sections, collapsed bridges, flooding e.t.c).
4. Users can edit their ​ red-flag ​ or ​ intervention ​ records.
5. Users can delete their ​ red-flag ​ or ​ intervention ​ records.
6. Users can add geolocation (Lat Long Coordinates) to their ​ red-flag ​ or ​ intervention records​ .
7. Users can change the geolocation (Lat Long Coordinates) attached to their ​ red-flag ​ or intervention ​ records​ .
8. Admin can change the ​ status​​ of a record to either ​ under investigation, rejected ​ (in the event of a false claim)​ ​ or​ resolved ( ​ in the event that the claim has been investigated and resolved)​

### Running Tests
- Install nosetests
- Navigate to project root
- Use `nosetests app/tests/` to run the tests
- To run the tests with coverage, use `nosetests --with-coverage --cover-package=api && coverage report`
