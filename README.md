# gateway: Wicked Async Services Platform API Gateway

[![Build Status](https://travis-ci.org/wickedasp/gateway.svg?branch=master)](https://travis-ci.org/wickedasp/gateway)

An API Gateway serves as a common entry point to a grouping of microservices composing a larger system. This project is a fully asynchronous gateway that proxies requests to services, fully baked by the Python ecosystem.

A large win of using a gateway is that all services appear to be from a single domain, getting around a number of issues including CORS. It also unifies the system, making it much easier to reason about from the outside and refactor, maintaining contracts.

...in progress...

**This is a preliminary summary, and is not ready to be used yet.**

Goals:

* Easy dev experience, no need to start up the full system.
* Cohesive micro-service oriented system baked fully by the Python community.
* Extensible, via filters, and dispatching strategies (optional)
* Simple, we give a simple default but all config is easy to override to alter functionality.

# Routing

## Path Handling

Routes are determined based on path segments in the url:

    https://gateway.wasp.com/{service:[^/]+}{path:/.*$}

* service: This is what service you are calling
* path: Path on the service to be calling

Any query strings on the url will be included to the remote services. This is just an interface to the gateway, the various Dispatch Strategies define how requests/responses flow in and out of the backend services.

## Dispatch Strategy

We support a number of strategies for how to delegate work to the system, with an easy to use ABC to add others.

Maybe something like this:

* Message Bus: `pip install wasp-gateway[bus]`: Backlogged
* HTTP Rest: `pip install wasp-gateway[http]`

### Message Bus

BACKLOGGED

### HTTP Rest

This is a fairly simple HTTP proxy, it relies on the service discovery system to know about available services that it can proxy to. If a service is unavailable, a 503 will be returned.

TODO: define abc, we will have our own discovery service client, have adapters for consul, eureka, etc.

# Security

## Protected Headers

Formulate how to hide internal headers from the outside, allowing backend services to pass them around freely.

## Filters

Easy middleware filters to edit/block/record requests coming in and out. Users could handle mobile traffic differently or do some sort of AB test or metrics?

