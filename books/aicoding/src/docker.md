# In Docker container

In order to allow the CLI tools to roam freely on the code-base without the fear of them making changes in other places of
the disk or the operating system we can use them inside Docker containers.


See my [Rust](https://github.com/szabgab/rust-docker-on-ubuntu/), [Python](https://github.com/szabgab/python-docker-on-ubuntu/), and [Perl](https://github.com/szabgab/perl-docker-on-ubuntu/) containers.


## Antigravity (in place of Gemini)

Add the following lines to your Dockerfile:

```Dockerfile
RUN echo Install Antigravity   && \
    curl -fsSL https://antigravity.google/cli/install.sh | bash  && \
    echo done
```

Add the following line to the `.bashrc` file of the container.

```
export PATH="/home/ubuntu/.local/bin:$PATH"
```

When you start Antigravity inside the container you'll need to authenticate. It shows you a link that when I tried was brokent.
It inserted spaces in the URL. So I had to copy the URL, remove the spaces and only then I could use it.


## GitHub Co-pilot CLI


```Dockerfile
RUN echo Install GitHub co-pilot CLI   && \
    curl -fsSL https://gh.io/copilot-install | bash  && \
    echo done
```


## Codex CLI

```
apt install -y gawk
```

```
RUN echo Install Codex   && \
    curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_NON_INTERACTIVE=1 sh && \
    echo done
```



