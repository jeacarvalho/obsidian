---
topic_classification:
  version: '2.0'
  classified_at: '2026-03-06T07:39:00.545550+00:00'
  model: gemini-2.5-flash-lite
  topics:
  - name: linguagem_rust_preferida_desenvolvedores
    weight: 10
    confidence: 0.98
  - name: performance_rust
    weight: 9
    confidence: 0.95
  - name: seguranca_rust
    weight: 9
    confidence: 0.95
  - name: confiabilidade_rust
    weight: 9
    confidence: 0.95
  - name: conceitos_ownership_rust
    weight: 8
    confidence: 0.9
  - name: compilador_rust_validador_codigo
    weight: 8
    confidence: 0.9
  - name: rust_vs_pandas_manipulacao_dados
    weight: 7
    confidence: 0.85
  - name: aws_lambdas_com_rust
    weight: 7
    confidence: 0.8
  - name: execucao_codigo_rust_a_partir_binario
    weight: 6
    confidence: 0.75
  - name: desenvolvimento_seguro_rust
    weight: 7
    confidence: 0.88
  cdu_primary: '004.43'
  cdu_secondary:
  - '004.6'
  - '004.7'
  - '005.3'
  - '005.8'
  cdu_description: Programação de computadores; Linguagens de programação; Linguagens de programação de sistemas; Linguagens de programação de alto nível; Linguagens de programação de sistemas de tempo real; Linguagens de programação de sistemas de segurança; Linguagens de programação de sistemas de alto desempenho
---
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