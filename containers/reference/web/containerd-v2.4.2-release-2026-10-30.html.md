---
title: Release containerd 2.4.2 · containerd/containerd
description: Welcome to the v2.4.2 release of containerd! The second patch release for containerd 2.4 contains various fixes and updates including security patches. Security Updates containerd CVE-2026-95839 ...
sitename: GitHub
date: "2026-10-13"
categories: ['repository:46089560']
fingerprint: b46354a3082085ea
---
## Repository navigation

Welcome to the v2.4.2 release of containerd!

The second patch release for containerd 2.4 contains various fixes

and updates including security patches.

### Security Updates

- **containerd**

### Highlights

#### Container Runtime Interface (CRI)

- Apply hardening to not follow symlinks for container log files (#14302)

#### Image Distribution

- Fix excessive memory usage during image pulls when registry downloads outpace content writes (#14342)
- Apply hardening to reject image references with ".." path components (#14282)

#### Runtime

- Apply hardening to allowlist socket domains in the default seccomp profile (#14247)

Please try out the release binaries and report any issues at

https://github.com/containerd/containerd/issues.

### Contributors

- Samuel Karp
- Maksym Pavlenko
- Sebastiaan van Stijn
- Derek McGowan
- LEI WANG
- Paweł Gronowski
- Phil Estes
- Wei Fu
- syed abdul khaliq

### Changes

## 25 commits


- `4b342aeaf` Prepare release notes for v2.4.2
- Update to go1.26.9 / go1.27.2 (security) (#14350)
  - `9c06c813e` Update to go1.26.9 / go1.27.2
- ci: update to golangci-lint v2.14.0 (go1.27.2 compatibility) (#14347)
  - `3fb9faa68` ci: update to golangci-lint v2.14.0 (go1.27.2 compatibility)
  - `187caba38` Merge commit from fork
  - `44fd201a8` remotes/docker: bound parallel fetch readers
  - `fc7adbfab` Merge commit from fork
  - `a2eb01f66` images: skip malformed digests when computing referrer labels
  - `39cff482d` Merge commit from fork
  - `7f0c0b822` content, remotes: bound reads to expected size
- remotes/docker: throttle worker chunk buffers (#14342)
  - `6a78f854a` remotes/docker: limit chunk buffers per layer
- cri: should not follow log file (#14302)
  - `098de667d` cri: should not follow log file
- reference: reject `..` path components that rewrite the host (#14282)
  - `6b631559b` reference: reject `..` path components that rewrite the host
- seccomp: Use an allow-list for socket domains (#14247)
  - `7936ee578` seccomp: Use an allow-list for socket domains
- update runc binary to v1.5.2 (#14241)
  - `54a82dcf0` update runc binary to v1.5.2
- Conditional actions (#14237)

### Dependency Changes

This release has no dependency changes

Previous release can be found at v2.4.1

### Which file should I download?

- `containerd-<VERSION>-<OS>-<ARCH>.tar.gz`:         ✅Recommended. Dynamically linked with glibc 2.35 (Ubuntu 22.04).
- `containerd-static-<VERSION>-<OS>-<ARCH>.tar.gz`:  Statically linked. Expected to be used on Linux distributions that do not use glibc >= 2.35. Not position-independent.

In addition to containerd, typically you will have to install runc

and CNI plugins from their official sites too.

See also the Getting Started documentation.
