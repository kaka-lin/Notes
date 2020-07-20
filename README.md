# My Learning Notes

My Medium: [AIoT Taipei](https://medium.com/aiot-taipei)

- [Python](https://github.com/kaka-lin/Notes/tree/master/Python)

- [Go](https://github.com/kaka-lin/Notes/tree/master/Go)

- [Data Structure and Algorithms (DSA)](https://github.com/kaka-lin/Notes/tree/master/DSA)

- [Database](https://github.com/kaka-lin/Notes/tree/master/DB)

- [DevOps](https://github.com/kaka-lin/Notes/tree/master/DevOps)

- [Data Science](https://github.com/kaka-lin/Notes/tree/master/Data_Science)

## Scripts

1. Convert `ipynb` to `md`

    ```bash
    # all `ipynb` files
    $ python convert_ipynb_to_md.py

    # the specific `ipynb` file
    python convert_ipynb_to_md.py --ipynb_file {specific ipynb file}
    ```

2. Adding `Front Matter` to `Markdown` file

    ```bash
    # all `md` files except `REAMDE.md`
    $ python3 add_front_matter_to_md.py

    # the specific `md` file
    $ python3 add_front_matter_to_md.py --file_path {specific md file}
    ```
