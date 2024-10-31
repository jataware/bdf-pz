FROM python:3.11.5
RUN useradd -m jupyter
EXPOSE 8888

RUN apt update && apt install -y lsof

# Install Python requirements
RUN pip install --upgrade --no-cache-dir hatch pip

RUN pip install git+https://github.com/mitdbg/palimpzest.git@main

COPY --chown=1000:1000 src/ /jupyter/src
COPY --chown=1000:1000 pyproject.toml /jupyter/pyproject.toml
COPY --chown=1000:1000 README.md /jupyter/README.md
RUN chown -R 1000:1000 /jupyter
RUN pip install -e /jupyter

# Switch to non-root user. It is crucial for security reasons to not run jupyter as root user!
USER jupyter
WORKDIR /jupyter

# Service
CMD ["python", "-m", "beaker_kernel.server.main", "--ip", "0.0.0.0"]