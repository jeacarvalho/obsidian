---
created: 2021-02-19T16:51:45 (UTC -03:00)
tags: [rust]
source: https://medium.com/tenable-techblog/building-a-microservice-with-rust-23a4de6e5e14
author: Mikhail Medvedev
---

# Building a microservice with Rust | by Mikhail Medvedev | Tenable TechBlog | Feb, 2021 | Medium


---
[![Mikhail Medvedev](https://miro.medium.com/fit/c/96/96/1*qwYWGS0R21Gn4QCwNdvyVQ.jpeg)](https://medium.com/@mmedvedev_18854?source=post_page-----23a4de6e5e14--------------------------------)

_Can you build a microservice using Rust? Or more importantly, should you?_

![Image for post](https://miro.medium.com/max/60/0*uy0hT5dVlsDsS12B?q=20)

![Image for post](https://miro.medium.com/max/12480/0*uy0hT5dVlsDsS12B)

Photo by [Aaron Chavez](https://unsplash.com/@slickmctrick?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

While Kotlin and Python are the dominant languages in Tenable we do dedicate time to investigate what emerging technologies are worth considering for our tech stack. Rust is one of them. It has proved itself as a powerful instrument and a great replacement for older, memory error-prone languages like C. Rust is expressive, modern and provides excellent tooling. But the most remarkable feature is, of course, its innovative ownership model that can prevent most memory-related bugs at compile-time, and without a garbage collector.

Also, we develop and maintain a range of microservice oriented architectures. Love them or hate them, microservices are extremely useful for building scalable and resilient applications.

Traditionally, teams develop microservices using languages like Java or Python and benefit from their ecosystems. You can just google “Java microservice” or “Python microservice” to find dozens of recipes on how to do that.

Can you build a microservice using Rust, though? Or more importantly, should you?

We decided to run an experiment and create a simple microservice written in Rust to see for ourselves if it’s worth it. The thinking was: if we failed, we would learn something useful anyway, if we succeeded, we would add a new awesome device to our team’s toolbox.

A typical microservice is made of:

-   HTTP API: most microservices will have to provide a REST API. At the very least a service should be able to respond to basic health check requests from a larger management service.
-   Code to work with the database: usually some form of an ORM.
-   Code to read messages from a queue, such as Kafka.
-   A Dockerfile to build the service so it could be deployed (e.g. to Kubernetes).

That’s what we need to put together a microservice, regardless of the language used. For Java or Python, these points are relatively well-researched and a few time-proven libraries are available. For Rust, as a newer language, we needed to find and choose the crates, and then write code to glue them together.

First, let’s create our project. We will use the Rust CLI, Cargo:

mkdir service\_rust && cd service\_rust  
cargo init

This creates two files: Cargo.toml which holds various project metadata, and src/main.rs that is the entry point of our code. The program starts with running the main() function.

That’s very easy to compile and run:

cargo run

There are several advanced and mature Rust web frameworks — any of which can be used for a microservice. Most include features like asynchronous execution and high performance. They also don’t normally require a separate web server, unlike many Python or Java frameworks, which is very handy when it comes to deployment.

After some research, we narrowed the list down to Actix-web, Rocket, and Warp.

We eventually chose Actix-web: it is popular, easy to use, has all the features and comes together with the Actor system library which we could use for a Kafka consumer thread.

The syntax somewhat resembles Flask and integrates with our main() function:

Among Rust ORMs, Diesel is king — so it was an obvious choice. It features a nice query syntax and supports all popular databases. We can integrate it with Actix using data() and then it becomes available to use by the handlers:

For a Kafka client, we chose rust-rdkafka — this one isn’t written entirely in Rust but based on librdkafka, a C library. It does, however, feature asynchronous data processing and integrates with Actix nicely. There are other, full-Rust options if you like.

Here we run a Kafka processor in a thread parallel to the API:

Serialization/deserialization of JSON is handled seamlessly by Serde, which is another amazing feature of Rust.

Finally, we would like to compile the code and wrap it up in a Docker container so it can be shipped in our dev environment. We will use multi-stage Docker build as the code compiles to a single binary:

Now, I have to admit: this doesn’t work. It builds the image, but if we try to run it, it will crash with an error message something like this:

standard\_init\_linux.go:219: exec user process caused: no such file or directory

The reason is that some Rust crates depend on external libraries. In order to make them work, we’ll have to either install them on the resulting image or build them statically into our binary. To implement the latter, we can use a custom “builder” image, for example, rust-musl-builder (https://github.com/emk/rust-musl-builder):

Now the service builds and even runs.

For simplicity, some boring but easier-to-implement things are omitted from this article, notably:

-   Testing: Rust features a built-in unit testing facility. Just try it — it’s amazing.
-   Configuration: this is trivial to implement, but at the same time, very environment-specific.
-   Logging: it is pretty straightforward.
-   SSL: although we touched on this with regards to the building stage, usually you also have to deal with certificates and `openssl` initialisation code. However, exploring this topic may require another full-sized article.
-   Other things that are specific to our environment.

All in all, we consider our experiment successful. Yes, you definitely can build microservices with Rust. Some aspects turned out to be easier than expected, some required more tinkering.

However, in a limited period of time, we built a service that is ready to be shipped, doesn’t need any web or application server, and features advanced functionality like asynchronous execution — that is very encouraging.

A microservice made with Rust has a few distinctive advantages:

-   It enjoys great performance compared to traditional alternatives.
-   It is free from most of the memory-related bugs which plague lower-level languages.
-   It takes advantage of a powerful type system of Rust: many bugs can be caught at compile time.
-   It requires no additional runtime (the runtime is compiled into a binary that is easily shipped.)
-   This binary doesn’t run a garbage collector. This makes it easier to control the resources utilized by the service.

We must mention the downsides as well:

-   Rust has a steeper learning curve than Python or Java.
-   It is also a relatively new language, so the ecosystem isn’t so established.
-   The community, as welcoming as it is, is also significantly smaller.

Rust is an extremely useful tool in building reliable and performant architectures. Even though it’s still a relatively new technology, the results are promising. It’s definitely worth it to have it in your toolbox.
