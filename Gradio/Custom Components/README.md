# Gradio: Custom Components

Create the custom components and can publish them as Python packages.

If you are familiar with Custom Components workflow, please jump to [Examples](#examples).

## Installation

You will need to have:

- Python 3.9+
- Node.js v16.14+
- npm 9+
- Gradio 4.0+

## The Workflow

The Custom Components workflow consists of *4 steps*:

1. `create`: creates a template for you to start developing a custom component.

2. `dev`: launches a development server with a sample app & hot reloading.

3. `build`: builds a python package containing to your custom component’s **Python** and **JavaScript** code

4. `publish`: uploads your package to `PyPi` and/or a sample app to `HuggingFace Spaces`.

Each of these steps is done via the **Custom Component CLI**. You can invoke it with `gradio cc` or `gradio component`

> ```
> $ gradio cc --help
>
> $ gradio cc create --help
> ```

### 1. create

Bootstrap a new template by running the following in any working directory:

```sh
$ gradio cc create <Component name> --template <The Template you want to use>

# Example
$ gradio cc create MyComponent --template SimpleTextbox
```

- --template: using `gradio cc show` to get a list of available component templates.

### 2. dev

Once you have created your new component, you can start a development server by **entering the directory** and running

```sh
$ gradio cc dev
```

You’ll see several lines that are printed to the console. The most important one is the one that says:

> Frontend Server (Go here): http://localhost:7861/

### 3. build

Once you are satisfied with your custom component’s implementation, you can build it to use it outside of the development server.

```sh
$ gradio cc build
```

This will create a **tar.gz** and **.whl** file in a **dist/** subdirectory. If you or anyone installs that **.whl** file (**pip install <path-to-whl>**) they will be able to use your custom component in any gradio app!

### 4. publish

Right now, your package is only available on a **.whl** file on your computer. You can share that file with the world with the publish command!

```sh
$ gradio cc publish
```

## Examples

- [gradio-image-prompter](https://github.com/kaka-lin/gradio-image-prompter)
