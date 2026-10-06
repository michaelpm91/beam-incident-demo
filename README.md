# Beam incident demo application

A deliberately failing, dependency-free HTTP service for a Teleport Beam
incident-investigation demo. The service listens on the port in `config.json`;
the health monitor and regression test require port 8080.

Run `python3 server.py` to start the service and `python3 healthcheck.py` to
probe it. Run `python3 -B test_service.py` in an isolated checkout (port 8080
must be available). The initial main-branch test is intentionally failing.

An automated investigator proposes a configuration-only patch in an incident
branch and opens a draft PR. Humans review and deploy; the agent does not
modify the running target. This repository contains no infrastructure state,
credentials, or incident evidence.
