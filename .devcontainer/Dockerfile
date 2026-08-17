FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# The upstream image currently carries an obsolete Yarn apt source whose
# missing signing key breaks any later feature that runs apt-get update.
# The Node feature installs the course's Node and Yarn toolchain separately.
RUN if [ -f /etc/apt/sources.list.d/yarn.list ]; then \
        mv /etc/apt/sources.list.d/yarn.list \
            /etc/apt/sources.list.d/yarn.list.disabled; \
    fi
