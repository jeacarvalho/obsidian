Rust vs Go in Backend Web Development - Qvault

.![f98a847cc2002dddffd38aebdcdc9f4d.jpg](../_resources/44fd3bdcaf63f90a8d706e1422340055.jpg).

# Rust vs Go in Backend Web Development

[July 17, 2020](https://qvault.io/2020/07/17/rust-vs-go-in-backend-web-development/)  by [Lane Wagner](https://qvault.io/author/lane-c-wagner/)

Rust and Go are two huge successes in the realm of modern programming language development. The two languages compete in terms of backend web development… and it’s a *fierce* competition. For example, the popular communication app Discord just started [swapping out Go services for Rust](https://blog.discord.com/why-discord-is-switching-from-go-to-rust-a190bbca2b1f) to boost performance.

Both languages are new, have growing communities, and are fast and efficient. When it comes to microservice architectures, frameworks, and apps, Rust and Go are household names.

## Similarities

Rust and Go share many traits, especially when it comes to web engineering. They both have **rich standard libraries**, though Go tends to have more internet-focused protocols such as [HTTP](https://golang.org/pkg/net/http/) supported of out the box. Both languages are **open-source**, meaning no company will be yanking the source code out from under us anytime soon. Go and Rust are both new which means they don’t come with the legacy and backward-compatibility baggage that you find with languages like Java and Javascript.

Having said that, there are a few key differences as well:

## Performance

Performance metrics generally put Rust squarely ahead of Go, but not by a lot. The Rust compiler and language design allow developers to easily take advantage of optimizations that achieve speeds comparable to the likes of C. On the other hand, Go trades a small amount of speed for simplicity and elegant syntax.

## Memory Management

![1165ea7deed9fc2a2faca45741db7fcf.jpg](../_resources/ef91bc71f666da6e4c9d1addd35f5ad5.jpg)

Both languages claim the title of “memory-safe” but take different approaches to achieve it. Rust catches memory errors at compile-time while Go uses a garbage collector at runtime.

Rust makes use of compile-time ownership strategy through [zero-cost abstractions](https://boats.gitlab.io/blog/post/zero-cost-abstractions/). If a Rust program is not memory safe, it will fail to compile. To anyone who frequently deals with memory errors in C languages, this is recognized as an amazing feature. Instead of clever compiler optimizations, the Go compiler adds a small runtime to the completed executable that manages the allocation and release of memory.

While both approaches have their pros and cons, generally speaking Rust’s compiler optimizations result in more performant programs. Alternatively, Go’s application code is cleaner because memory management is fully handled by the runtime.

## Development Speed

There are times during the development of a web application that development speed is more important than app speed. Python is a great example, it is one of the slowest languages but has some of the cleanest syntax. While Go is generally faster and uses less memory than languages like Java, C#, JavaScript, Python, and Ruby, it makes a performance trade-off to allow for fast and simple development.

## Concurrency

Concurrency is a necessity in backend applications. Some languages run in single-threaded environments which means they use some clever tricks to simulate concurrency without achieving true parallelism. Both [Rust and Go have elegant solutions to build fully parallel](https://qvault.io/2020/05/11/concurrency-in-rust-can-it-stack-up-against-gos-goroutines/) applications, but Go takes the cake again in terms of simplicity, with the go keyword being the only syntax necessary to spin up a new thread:

`go someFunc()`

## The Winner

As usual, there is no outright winner, the results are more nuanced than that.
Rust wins at:

- Speed
- Memory usage
- Fine-tuning and control over final executable

Go wins at:

- Simple syntax
- Developer speed

## Thanks For Reading!

Follow us on Twitter [@q_vault](https://twitter.com/q_vault) if you have any questions or comments

Take game-like coding courses on [Qvault Classroom](https://classroom.qvault.io/#/)

[Subscribe](https://mailchi.mp/5c7f5c281bbe/qvault-newsletter-subscribe) to our Newsletter for more educational articles

### ****Share this:

- [(L)](https://qvault.io/2020/07/17/rust-vs-go-in-backend-web-development/?share=twitter&nb=1)