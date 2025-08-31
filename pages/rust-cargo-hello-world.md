---
title: "Hello World with Rust and Cargo"
timestamp: 2022-10-21T13:00:01
tags:
  - Rust
types:
  - screencast
published: true
books:
  - rust
author: szabgab
archive: true
show_related: true
---


In this short video we'll see how to create a <b>Hello World!</b> program using the [Rust Programming language](https://www.rust-lang.org/)
and the [Cargo](https://doc.rust-lang.org/cargo/) package manager.


Create a new project with the brilliant name "abcd"

```
cargo new abcd
```

```
cd abcd
```

The directory layout:

```
.
├── Cargo.toml
└── src
    └── main.rs
```

{% include file="examples/rust/abcd/Cargo.toml" %}

{% include file="examples/rust/abcd/src/main.rs" %}

Compile and run your program:

```
cargo run
```


{% youtube id="_JNhVlHot4k" file="rust-cargo-hello-world.mp4" %}
