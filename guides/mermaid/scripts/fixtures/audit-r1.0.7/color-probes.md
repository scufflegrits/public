# Theme color contract probes

## named
```mermaid
---
config:
  theme: base
  look: classic
  themeVariables:
    primaryColor: red
---
flowchart LR
  COLOR_NODE["Color control"]
```

## hex
```mermaid
---
config:
  theme: base
  look: classic
  themeVariables:
    primaryColor: "#ff0000"
---
flowchart LR
  COLOR_NODE["Color control"]
```

## unquoted
```mermaid
---
config:
  theme: base
  look: classic
  themeVariables:
    primaryColor: #ff0000
---
flowchart LR
  COLOR_NODE["Color control"]
```

## unknown
```mermaid
---
config:
  theme: base
  look: classic
  auditUnknownKey: true
  themeVariables:
    primaryColor: "#ff0000"
---
flowchart LR
  COLOR_NODE["Color control"]
```

## Class definition CSS formats
```mermaid
---
config:
  theme: base
  look: classic
---
flowchart LR
  COLOR_NAMED["Named"]
  COLOR_HEX["Short hex"]
  COLOR_RGB["RGB function"]
  classDef nodeNamed fill:aliceblue,stroke:steelblue,color:midnightblue
  classDef nodeHex fill:#abc,stroke:#123456,color:#123
  classDef nodeRgb fill:rgb(240,248,255),stroke:steelblue,color:midnightblue
  class COLOR_NAMED nodeNamed
  class COLOR_HEX nodeHex
  class COLOR_RGB nodeRgb
```
