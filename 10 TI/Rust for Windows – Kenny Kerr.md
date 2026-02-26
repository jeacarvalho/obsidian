Rust for Windows – Kenny Kerr

# Rust for Windows

![71d4efa35b3d11457c35543f9f55fba3](../_resources/d50d52377d934d2af0231e11f453f15c.jpg)Kenny Kerr

19 hours ago

I am excited to finally talk about the grand plan we have been working on for some time, namely the unification of the Windows API. No more Win32 here, WinRT there, COM this, UWP that. Just stop it. [Rust for Windows](https://github.com/microsoft/windows-rs) lets you use any Windows API directly and seamlessly via the [windows](https://crates.io/crates/windows) crate.

Whether its timeless functions like CreateEvent and WaitForSingleObject, powerful graphics engines like Direct3D, traditional windowing functions like CreateWindowEx and DispatchMessage, or more recent UI frameworks like Composition and Xaml, the [windows](https://crates.io/crates/windows) crate has you covered.

This is an early preview, but finally having [metadata](https://github.com/microsoft/win32metadata) for the entire Windows API is a huge step toward making Windows development easier and more approachable for all developers.

The repo has everything you need to get started:
https://github.com/microsoft/windows-rs/

In particular, the [readme](https://github.com/microsoft/windows-rs/) has a short guide to getting started. There are also [some simple examples](https://github.com/kennykerr/samples-rs) that you can follow. And of course, we have updated Robert Mikhayelyan’s [Minesweeper](https://github.com/robmikh/minesweeper-rs) port.

If having the entire Windows API at your fingertips seems a little daunting, I have also published some [Rust documentation for the Windows API](https://microsoft.github.io/windows-docs-rs/). This lets you browse or search for just the API you need and makes it a lot easier to find what you are looking for.

If you have questions or run into issues, please use the GitHub repo to get in touch.

**Repo**: https://github.com/microsoft/windows-rs
**API docs**: https://microsoft.github.io/windows-docs-rs
**Samples**: https://github.com/kennykerr/samples-rs

https://blogs.windows.com/windowsdeveloper/2021/01/20/making-win32-apis-more-accessible-to-more-languages

### Share this:

### *Related*

- [Rust/WinRT coming soon](https://kennykerr.ca/2020/02/22/rust-winrt-coming-soon/)
- 22 February 2020
- With 27 comments
- [The State of C++ on Windows](https://kennykerr.ca/2019/01/25/the-state-of-cpp-on-windows/)
- 25 January 2019
- With 19 comments
- [The road to Windows 8](https://kennykerr.ca/2011/10/18/the-road-to-windows-8/)
- 18 October 2011
- With 39 comments

Categories: [Uncategorized](https://kennykerr.ca/category/uncategorized/)