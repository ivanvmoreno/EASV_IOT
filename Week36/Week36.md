## GPIO
Stands for "General Purpose Input/Output." GPIO is a type of pin found on an integrated circuit that does not have a specific function. While most pins have a dedicated purpose, such as sending a signal to a certain component, the function of a GPIO pin is customizable and can be controlled by software.

## Connection of IOT devices
Not all IOT devices have direct access to internet. Instead, there are several IOT devices which make use of a gateway in order to connect them to the internet because they don't implement technologies capable of establishing a direct connection to internet.

![protocols](https://imgur.com/xCyI8P8.jpg)

## MQTT
MQTT stands for Message Queuing Telemetry Transport. It is a lightweight publish and subscribe system where you can publish and receive messages as a client, so producer and consumer are decoupled. MQTT uses TCP to establish the connection between the clients and the server.

It's designed for constrained devices with low-bandwidth. So, it’s the perfect solution for Internet of Things applications. MQTT allows you to send commands to control outputs, read and publish data from sensor nodes and much more.

In a publish and subscribe system, a device can publish a message on a topic, or it can be subscribed to a particular topic to receive messages.

Topics are the way you register interest for incoming messages or how you specify where you want to publish the message and are represented with strings separated by a forward slash. Each forward slash indicates a topic level (`/home/office/lamp`, where `home` and `office` are topics).

The broker is primarily responsible for receiving all messages, filtering the messages, decide who is interested in them and then publishing the message to all subscribed clients.

MQTT has support for persistent messages stored on the broker. When publishing messages, clients may request that the broker persists the message. Only the most recent persistent message is stored. When a client subscribes to a topic, any persisted message will be sent to the client.

## CoAP
CoAP stands for Constrained Application Protocol.

Like HTTP, CoAP is a document transfer protocol. Unlike HTTP, CoAP is designed for the needs of constrained devices. CoAP packets are much smaller than HTTP TCP flows.

CoAP runs over UDP, not TCP. Retries and reordering are implemented in the application stack.

CoAP follows a client/server model. Clients make requests to servers, servers send back responses. Clients may `GET`, `PUT`, `POST` and `DELETE` resources.

CoAP is designed to interoperate with HTTP and the RESTful web at large through simple proxies.

Like HTTP, CoAP supports content negotiation. Clients use `Accept` options to express a preferred representation of a resource and servers reply with a `Content-Type` option to tell clients what they’re getting. As with HTTP, this allows client and server to evolve independently, adding new representations without affecting each other.

CoAP requests may use query strings in the form `?a=b&c=d` . These can be used to provide search, paging and other features
