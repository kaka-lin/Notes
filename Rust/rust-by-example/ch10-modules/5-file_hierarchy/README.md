# File hierarchy

## Example

```
$ tree .
.
|-- main.rs
|-- my
|   |-- inaccessible.rs
|   |-- mod.rs
|   `-- nested.rs
`-- split.rs
```

### build && run 

```bash
$ rustc src/split.rs && ./split
```
