- Linguagem de desenvolvimento mais amada pelos desenvolvedores que responderam pesquisa da stackoverflow
- Performance, segurança e confiabilidade
- tem conceitos importantes como ownership, compilador que é quase um validador de teu código
- fontes: https://www.rust-lang.org/pt-BR, https://doc.rust-lang.org/book/


Citação interessante:
>*It's a great example of the different attitudes of C/C++ and Rust: In C/C++ something is correct when someone can use it correctly, but in Rust something is correct when someone can't use it incorrectly.*
fonte: https://www.reddit.com/r/rust/comments/lt4u85/const_generics_mvp_hits_beta/goyg3v4/
# Referências
- [Types and patterns - Rust for the Polyglot Programmer (greenend.org.uk)](https://www.chiark.greenend.org.uk/~ianmdlvl/rust-polyglot/types.html)
- [Rust Language Cheat Sheet](https://cheats.rs/)
- https://github.com/joaocarvalhoopen/How_to_learn_modern_Rust#learn-rust-deeply-one-step-after-the-other

# Sobre performance de operações em arquivos Pandas x Rust:
>1.Use Pandas when you can: small CSV(<1M lines), simple operation, data cleaning; 2. Use Rust when you have: complex operations, memory heavy or time-consuming pipelines, custom build functions, scalable software…
fonte: https://able.bio/haixuanTao/data-manipulation-pandas-vs-rust--1d70e7fc

# AWS Lambdas com Rust
- Tem alguns ajustes para rodar async direito
- Tem que desenvolver com target correto, o linux da Amazon. 
O [artigo](https://beanseverywhere.xyz/blog/rust-lambda) fonte desses pontos traz orientações maiores

# [Lendo arquivo .bin e executando via rust](https://kerkour.com/blog/rust-execute-from-memory/)
- É possível ler um arquivo binário com código executável para posteriormente ler o .bin via rust
- Esse comando gera um .bin que é um hello world para x86_64:
	- echo '488d35140000006a01586a0c5a4889c70f056a3c5831ff0f05ebfe68656c6c6f20776f726c640a' | xxd -r -p > shellcode.bin
- Posteriormente vc pode ler via `include_bytes!` ou usar um mapa de memória no rust

# Links
[[Rust for Windows – Kenny Kerr]]
[[Rust for Java Devs]]
[[Rust vs Go in Backend Web Development - Qvault]]
[[Building a microservice with Rust]]
[[17 Resources To Help You Learn Rust In 2021]]
[Livro sobre desenvolvimento seguro em Rust](https://highassurance.rs/)
[[Building a web service with Rust, Postgres and Kafka]]
[[Aprendendo rust por estágios]]
- Vídeo bem legal falando sobre o que acontece antes de chegar no "main". COm vários resources interessantes no final: https://www.youtube.com/watch?v=q8irLfXwaFM
- [[Rust + nails + cornucopia + dioxius + devcontainers]]
- [Esse link](https://rust-lang.guide/) dá um learning path muito legal sobre como aprender, até um ponto de conhecimento bem aprofundado