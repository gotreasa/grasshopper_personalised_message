# Grasshopper_Personalised_Message

[![License: AGPL](https://img.shields.io/badge/License-AGPL-blue.svg)](https://github.com/gotreasa/grasshopper_personalised_message/blob/main/LICENSE)
[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=gotreasa_grasshopper_personalised_message&metric=alert_status)](https://sonarcloud.io/dashboard?id=gotreasa_grasshopper_personalised_message)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=gotreasa_grasshopper_personalised_message&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=gotreasa_grasshopper_personalised_message)
[![Build Status](https://github.com/gotreasa/grasshopper_personalised_message/actions/workflows/cicd.yml/badge.svg)](https://github.com/gotreasa/grasshopper_personalised_message/actions/workflows/cicd.yml)
[![Can I Deploy main to test](https://gotreasa.pactflow.io/pacticipants/grasshopper_personalised_message_app/branches/main/latest-version/can-i-deploy/to-environment/test/badge)](https://gotreasa.pactflow.io/hal-browser/browser.html#https://gotreasa.pactflow.io/pacticipants/grasshopper_personalised_message_app/branches/main/latest-version/can-i-deploy/to-environment/test/badge)

Welcome to the Python Template created via a cookiecutter recipe. The project template is designed for a development via a `Double Loop approach` (BDD-TDD) using pytest and several other pytest libs.

## Description

Create a function that gives a personalized greeting. This function takes two parameters: `name` and `owner`.

Use conditionals to return the proper message:

| case              | return        |
| ----------------- | ------------- |
| name equals owner | 'Hello boss'  |
| otherwise         | 'Hello guest' |
