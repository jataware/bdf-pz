FROM python:3.11.5
RUN useradd -m jupyter
EXPOSE 8888

RUN apt update && apt install -y lsof

# Install Python requirements
RUN pip install --upgrade --no-cache-dir hatch pip

COPY beaker_kernel-1.7.3a0-py3-none-any.whl /jupyter/
COPY --chown=1000:1000 . /jupyter/
RUN chown -R 1000:1000 /jupyter
RUN pip install -e /jupyter
RUN pip uninstall beaker_kernel -y
RUN pip install /jupyter/beaker_kernel-1.7.3a0-py3-none-any.whl

# Switch to non-root user. It is crucial for security reasons to not run jupyter as root user!
USER jupyter
WORKDIR /jupyter

RUN pip install git+https://github.com/mitdbg/palimpzest.git@main
RUN python -c "import palimpzest"


# Service
CMD ["python", "-m", "beaker_kernel.server.main", "--ip", "0.0.0.0"]